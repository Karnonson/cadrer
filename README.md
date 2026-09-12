# cadrer

**CADRER** is the six-step build loop taught in the free course **Première Livraison**. This repo is
its Claude Code plugin, `cadrer`, in two languages: the six French steps spell the name, the six
commands are English and the same in both, and what the skills write and show follows the language you
picked at install.

| Step | Command | Writes (French) | Writes (English) |
| --- | --- | --- | --- |
| **C**hoisir | `/cadrer:ideate` | `idee.md` | `idea.md` |
| **A**ffiner | `/cadrer:refine` | `decisions.md` | `decisions.md` |
| **D**étailler | `/cadrer:spec` | `spec.md` | `spec.md` |
| **R**épartir | `/cadrer:slice` | `tranches.md` | `slices.md` |
| **E**xécuter | `/cadrer:implement` | the code, plus ticks under the slice | same |
| **R**éviser | `/cadrer:audit` | `audits/<NN>.md` | `audits/<NN>.md` |

All six write into one folder per idea, `builds/<NN>-<slug>/`, and each reads what the last one left.

## Install

In a terminal, standing in the project you want the loop in. In French:

```
claude plugin marketplace add Karnonson/cadrer
claude plugin install cadrer@cadrer --scope project
```

In English:

```
claude plugin marketplace add Karnonson/cadrer-en
claude plugin install cadrer@cadrer-en --scope project
```

One language per project: both are the same plugin, `cadrer`, so the second replaces the first.
`--scope project` switches the plugin on for that folder only (it writes `.claude/settings.json`
there); leave it off and it switches on for every project on your machine. Then `/cadrer:ideate` and
the rest answer by name in any Claude Code window opened in that folder. `claude plugin details
cadrer` shows what it costs you per session; `claude plugin uninstall cadrer --scope project`
removes it.

Before 0.3.0 the plugin was called `workflow` (`/workflow:ideate`, from the marketplace
`workflow-skills`). Uninstall that one and install `cadrer`; the build folders are the same.

## Two languages, one source

The skills are generated. `src/` is the source of truth:

- `src/skills/<slug>/SKILL.md` — one English body per step, with `{{placeholders}}` where the
  language shows.
- `src/vocab/fr.json` and `src/vocab/en.json` — what the placeholders become: the description and
  argument hint shown in the `/` menu, the file names, the headings inside each file, the markers the
  later steps look for (`Fait quand` / `Done when`, `Bloqué par` / `Blocked by`…), the verdicts
  (`fusionner`, `corriger d'abord`, `retour à la tranche` / `merge`, `fix first`, `back to slice`),
  and one line telling the agent which language to answer and write in.
- `python3 tools/render.py` writes the French render at the root of this repo (`plugins/cadrer/`,
  `.claude-plugin/marketplace.json`, marketplace `cadrer`) and the English one in `en/`, a whole
  second marketplace named `cadrer-en`. Two marketplaces because Claude Code keys plugins by name and
  the command prefix is the plugin name: this is what lets both languages type `/cadrer:ideate`.
  `--check` reports a stale render.
- `./deploy-en.sh` force-pushes `en/` as the `main` branch of `Karnonson/cadrer-en`, the way a
  static site is deployed. Run it after committing here.

Edit `src/`, render, commit both renders. Never edit `plugins/` or `en/` by hand: the next render
overwrites them, and `tools/render.py --check` will say so.

The bodies stay English in both renders on purpose: a skill is read by the agent, never by the
learner, and French costs more tokens for the same instruction. Measured with `tools/token_estimate.py`
on 2026-09-12, o200k tokenizer:

| | English render | French render |
| --- | --- | --- |
| Six skills, loaded when one runs | 4,448 | 4,657 (1.05×) |
| Six descriptions, always loaded | 318 | 416 (1.31×) |

A fully translated French body was 1.27–1.41× instead. `NAMING.md` records the decisions.

## Tools

`tools/token_estimate.py` counts what a skill set costs in tokens, and can compare two sets (paired by
folder name, or `--map EN=FR`). Claude's tokenizer is not public, so it counts with public ones —
OpenAI's, Llama 3, Qwen 3, DeepSeek V3, Mistral Nemo, Gemma 3 — and reports the FR/EN ratio across
them; with `ANTHROPIC_API_KEY` set it adds Claude's exact count from `count_tokens`.

```
uv run tools/token_estimate.py en/plugins/cadrer/skills                        # one set
uv run tools/token_estimate.py en/plugins/cadrer/skills plugins/cadrer/skills  # EN against FR
```

`--detail o200k` breaks it down per skill, `--json` prints the numbers. The public page for
non-technical readers, *Le prix du français*, lives in its own repo, `~/Desktop/prix-du-francais`.

## Credits

`refine` is adapted from Matt Pocock's `grilling` (MIT) — github.com/mattpocock/skills.
