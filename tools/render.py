#!/usr/bin/env python3
"""Render the CADRER plugin in each language from src/.

One English body per skill, two vocabularies, two installable marketplaces:

    src/skills/<slug>/SKILL.md   the six bodies, with {{placeholders}}
    src/vocab/fr.json, en.json   what each placeholder becomes
    src/plugin.json              plugin manifest template
    src/marketplace.json         marketplace manifest template
    src/README-en.md             README of the generated English repo

    python3 tools/render.py          # write the French render at the repo root, the English one in en/
    python3 tools/render.py --check  # exit 1 if either render is stale (release check)

Placeholders under "vocab" are pasted as they are. The manifest values
(marketplace_name, marketplace_description, plugin_description) and the
per-skill description and argument_hint are pasted as quoted strings, so a
template writes them bare: `description: {{description}}`. Every vocabulary key
must be used and every placeholder must be known, or the render stops.
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
PLUGIN = "cadrer"
TARGETS = {"fr": ROOT, "en": ROOT / "en"}
EXTRA_FILES = {"en": {"README.md": SRC / "README-en.md"}}
MANIFEST_KEYS = ("marketplace_name", "marketplace_description", "plugin_description")
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


def render(lang: str) -> dict[str, str]:
    """Return {relative path: content} for one language."""
    vocab = json.loads((SRC / "vocab" / f"{lang}.json").read_text(encoding="utf-8"))
    words = vocab["vocab"]
    skills = sorted(p.parent.name for p in (SRC / "skills").glob("*/SKILL.md"))
    if set(skills) != set(vocab["skills"]):
        sys.exit(f"{lang}: skills in src/skills {skills} and in vocab {sorted(vocab['skills'])} differ")

    files: dict[str, str] = {}
    used: set[str] = set()
    for slug in skills:
        per_skill = {k: quoted(v) for k, v in vocab["skills"][slug].items()}
        template = (SRC / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
        files[f"plugins/{PLUGIN}/skills/{slug}/SKILL.md"] = fill(
            template, {**words, **per_skill}, f"{lang}/{slug}", used)
    unused = set(words) - used
    if unused:
        sys.exit(f"{lang}: vocabulary keys no skill uses: {sorted(unused)}")

    manifests = {k: quoted(vocab[k]) for k in MANIFEST_KEYS}
    for template_name, out in (("plugin.json", f"plugins/{PLUGIN}/.claude-plugin/plugin.json"),
                               ("marketplace.json", ".claude-plugin/marketplace.json")):
        text = fill((SRC / template_name).read_text(encoding="utf-8"), manifests, template_name, set())
        files[out] = json.dumps(json.loads(text), indent=2, ensure_ascii=False) + "\n"
    for out, source in EXTRA_FILES.get(lang, {}).items():
        files[out] = source.read_text(encoding="utf-8")
    return files


def stale(target: Path, files: dict[str, str]) -> list[str]:
    problems = []
    for rel, content in files.items():
        path = target / rel
        if not path.exists():
            problems.append(f"missing {path.relative_to(ROOT)}")
        elif path.read_text(encoding="utf-8") != content:
            problems.append(f"differs {path.relative_to(ROOT)}")
    skills_dir = target / "plugins" / PLUGIN / "skills"
    if skills_dir.exists():
        for stray in skills_dir.rglob("*"):
            if stray.is_file() and str(stray.relative_to(target)) not in files:
                problems.append(f"stray {stray.relative_to(ROOT)}")
    return problems


def write(target: Path, files: dict[str, str]) -> None:
    shutil.rmtree(target / "plugins" / PLUGIN / "skills", ignore_errors=True)
    for rel, content in files.items():
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="compare instead of writing; exit 1 if stale")
    args = parser.parse_args()

    failed = False
    for lang, target in TARGETS.items():
        files = render(lang)
        if args.check:
            problems = stale(target, files)
            failed |= bool(problems)
            print(f"{lang}: {'up to date' if not problems else chr(10).join(problems)}")
        else:
            write(target, files)
            print(f"{lang}: {len(files)} files → {target.relative_to(ROOT) or '.'}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
