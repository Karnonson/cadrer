# cadrer

**CADRER** is the six-step build loop taught in the free course **Première Livraison**. This repo is
its Claude Code marketplace, with the loop as two plugins: `cadrer`, French commands and French files,
and `cadrer-en`, English commands and English files. Same skills, one source, pick one at install.

| Step | French | English | Writes (French) | Writes (English) |
| --- | --- | --- | --- | --- |
| **C**hoisir | `/cadrer:choisir` | `/cadrer-en:ideate` | `idee.md` | `idea.md` |
| **A**ffiner | `/cadrer:affiner` | `/cadrer-en:refine` | `decisions.md` | `decisions.md` |
| **D**étailler | `/cadrer:detailler` | `/cadrer-en:spec` | `spec.md` | `spec.md` |
| **R**épartir | `/cadrer:repartir` | `/cadrer-en:slice` | `tranches.md` | `slices.md` |
| **E**xécuter | `/cadrer:executer` | `/cadrer-en:implement` | the code, plus ticks under the slice | same |
| **R**éviser | `/cadrer:reviser` | `/cadrer-en:audit` | `audits/<NN>.md` | `audits/<NN>.md` |

All six write into one folder per idea, `builds/<NN>-<slug>/`, and each reads what the last one left.
Command names carry no accents — a skill name is lowercase letters, digits and hyphens — so you type
`detailler`, `repartir`, `executer`, `reviser`.

## Install

In a terminal, standing in the project you want the loop in:

```
claude plugin marketplace add Karnonson/cadrer
claude plugin install cadrer@cadrer --scope project        # French
claude plugin install cadrer-en@cadrer --scope project     # English
```

One language per project. `--scope project` switches the plugin on for that folder only (it writes
`.claude/settings.json` there); leave it off and it switches on for every project on your machine.
Then `/cadrer:choisir` and the rest answer by name in any Claude Code window opened in that folder.
`claude plugin details cadrer` shows what it costs you per session; `claude plugin uninstall cadrer
--scope project` removes it.

Before 0.3.0 the plugin was called `workflow` (`/workflow:ideate`, from the marketplace
`workflow-skills`). Uninstall that one and install `cadrer` or `cadrer-en`; the build folders are the
same.

## Two languages, one source

The plugins are generated. `src/` is the source of truth:

- `src/skills/<step>/SKILL.md` — one English body per step, with `{{placeholders}}` where the
  language shows.
- `src/vocab/fr.json` and `src/vocab/en.json` — what the placeholders become: the plugin name, the
  six command names, the description and argument hint shown in the `/` menu, the file names, the
  headings inside each file, the markers the later steps look for (`Fait quand` / `Done when`,
  `Bloqué par` / `Blocked by`…), the verdicts (`fusionner`, `corriger d'abord`, `retour à la tranche` /
  `merge`, `fix first`, `back to slice`), and one line telling the agent which language to answer and
  write in.
- `python3 tools/render.py` writes `plugins/cadrer/`, `plugins/cadrer-en/` and
  `.claude-plugin/marketplace.json`. `--check` reports a stale render.

Edit `src/`, render, commit. Never edit `plugins/` by hand: the next render overwrites it, and
`tools/render.py --check` will say so.

The bodies stay English in both plugins on purpose: a skill is read by the agent, never by the
learner, and French costs more tokens for the same instruction. Measured with `tools/token_estimate.py`
on 2026-09-12, o200k tokenizer:

| | `cadrer-en` | `cadrer` |
| --- | --- | --- |
| Six skills, loaded when one runs | 4,448 | 4,657 (1.05×) |
| Six descriptions, always loaded | 318 | 416 (1.31×) |

A fully translated French body was 1.27–1.41× instead. `NAMING.md` records the decisions.

## Tools

`tools/token_estimate.py` counts what a skill set costs in tokens, and can compare two sets (paired
through the CADRER slugs, or `--map EN=FR`). Claude's tokenizer is not public, so it counts with public
ones — OpenAI's, Llama 3, Qwen 3, DeepSeek V3, Mistral Nemo, Gemma 3 — and reports the FR/EN ratio
across them; with `ANTHROPIC_API_KEY` set it adds Claude's exact count from `count_tokens`.

```
uv run tools/token_estimate.py plugins/cadrer-en/skills                       # one set
uv run tools/token_estimate.py plugins/cadrer-en/skills plugins/cadrer/skills  # EN against FR
```

`--detail o200k` breaks it down per skill, `--json` prints the numbers. The public page for
non-technical readers, *Le prix du français*, lives in its own repo, `~/Desktop/prix-du-francais`.

## Credits

`refine` is adapted from Matt Pocock's `grilling` (MIT) — github.com/mattpocock/skills.
