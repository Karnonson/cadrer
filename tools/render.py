#!/usr/bin/env python3
"""Render the CADRER plugins from src/: one English body per step, two vocabularies, two plugins.

    src/skills/<step>/SKILL.md   the six bodies, with {{placeholders}}; folders carry the English step names
    src/vocab/fr.json, en.json   what each placeholder becomes, plus each language's plugin name and skill slugs
    src/plugin.json              plugin manifest template
    src/marketplace.json         marketplace manifest template; {{plugins}} becomes the list of both plugins

    python3 tools/render.py          # write plugins/<plugin_name>/ for each language and .claude-plugin/marketplace.json
    python3 tools/render.py --check  # exit 1 if a render is stale (release check)

Placeholders under "vocab" are pasted as they are, and so are the slugs:
{{slug}} is the skill's own command name, {{slug_<step>}} another skill's.
plugin_name, plugin_description, and the per-skill description and
argument_hint are pasted as quoted strings, so a template writes them bare:
`description: {{description}}`. Every vocabulary key must be used and every
placeholder must be known, or the render stops.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
LANGUAGES = ("fr", "en")
PLACEHOLDER = re.compile(r"\{\{(\w+)\}\}")


def fill(template: str, values: dict[str, str], where: str, used: set[str]) -> str:
    def sub(match: re.Match) -> str:
        key = match.group(1)
        if key not in values:
            sys.exit(f"{where}: unknown placeholder {{{{{key}}}}}")
        used.add(key)
        return values[key]

    return PLACEHOLDER.sub(sub, template)


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def pretty(text: str) -> str:
    return json.dumps(json.loads(text), indent=2, ensure_ascii=False) + "\n"


def render_plugin(vocab: dict) -> dict[str, str]:
    """Return {relative path: content} for one language's plugin."""
    lang, plugin = vocab["language"], vocab["plugin_name"]
    words = vocab["vocab"]
    steps = sorted(p.parent.name for p in (SRC / "skills").glob("*/SKILL.md"))
    if set(steps) != set(vocab["skills"]):
        sys.exit(f"{lang}: steps in src/skills {steps} and in vocab {sorted(vocab['skills'])} differ")
    slugs = {f"slug_{step}": vocab["skills"][step]["slug"] for step in steps}

    files: dict[str, str] = {}
    used: set[str] = set()
    for step in steps:
        skill = vocab["skills"][step]
        values = {**words, **slugs, "slug": skill["slug"],
                  "description": quoted(skill["description"]), "argument_hint": quoted(skill["argument_hint"])}
        template = (SRC / "skills" / step / "SKILL.md").read_text(encoding="utf-8")
        files[f"plugins/{plugin}/skills/{skill['slug']}/SKILL.md"] = fill(template, values, f"{lang}/{step}", used)
    unused = set(words) - used
    if unused:
        sys.exit(f"{lang}: vocabulary keys no skill uses: {sorted(unused)}")

    manifest = {k: quoted(vocab[k]) for k in ("plugin_name", "plugin_description")}
    text = fill((SRC / "plugin.json").read_text(encoding="utf-8"), manifest, "plugin.json", set())
    files[f"plugins/{plugin}/.claude-plugin/plugin.json"] = pretty(text)
    return files


def render() -> dict[str, str]:
    vocabs = [json.loads((SRC / "vocab" / f"{lang}.json").read_text(encoding="utf-8")) for lang in LANGUAGES]
    files: dict[str, str] = {}
    for vocab in vocabs:
        files.update(render_plugin(vocab))
    plugins = [{"name": v["plugin_name"], "source": f"./plugins/{v['plugin_name']}",
                "description": v["plugin_description"]} for v in vocabs]
    template = (SRC / "marketplace.json").read_text(encoding="utf-8")
    text = fill(template, {"plugins": json.dumps(plugins, ensure_ascii=False)}, "marketplace.json", set())
    files[".claude-plugin/marketplace.json"] = pretty(text)
    return files


def stale(files: dict[str, str]) -> list[str]:
    problems = []
    for rel, content in files.items():
        path = ROOT / rel
        if not path.exists():
            problems.append(f"missing {rel}")
        elif path.read_text(encoding="utf-8") != content:
            problems.append(f"differs {rel}")
    for stray in (ROOT / "plugins").rglob("*"):
        if stray.is_file() and str(stray.relative_to(ROOT)) not in files:
            problems.append(f"stray {stray.relative_to(ROOT)}")
    return problems


def write(files: dict[str, str]) -> None:
    shutil.rmtree(ROOT / "plugins", ignore_errors=True)
    for rel, content in files.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="compare instead of writing; exit 1 if stale")
    args = parser.parse_args()

    files = render()
    if args.check:
        problems = stale(files)
        print("\n".join(problems) if problems else "up to date")
        sys.exit(1 if problems else 0)
    write(files)
    print(f"{len(files)} files written under plugins/ and .claude-plugin/")


if __name__ == "__main__":
    main()
