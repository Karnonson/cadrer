# workflow-skills

A Claude Code marketplace holding one plugin, `cadrer`: **CADRER**, the six-step build loop taught in
the free course **Première Livraison**. The six steps spell the name.

| Step | Skill | English name | Writes |
| --- | --- | --- | --- |
| **C**hoisir | `/cadrer:choisir` | ideate | `idea.md` |
| **A**ffiner | `/cadrer:affiner` | refine | `decisions.md` |
| **D**étailler | `/cadrer:detailler` | spec | `spec.md` |
| **R**épartir | `/cadrer:repartir` | slice | `slices.md` |
| **E**xécuter | `/cadrer:executer` | implement | the code, plus ticks under the slice |
| **R**éviser | `/cadrer:reviser` | audit | `audits/<NN>.md` |

All six write into one folder per idea, `builds/<NN>-<slug>/`, and each reads what the last one left.
Skill names carry no accents — a skill name is lowercase letters, digits and hyphens — so you type
`detailler`, `repartir`, `executer`, `reviser`.

## Install

In a terminal, standing in the project you want the loop in:

```
claude plugin marketplace add Karnonson/workflow-skills
claude plugin install cadrer@workflow-skills --scope project
```

`--scope project` switches the plugin on for that folder only (it writes `.claude/settings.json`
there); leave it off and it switches on for every project on your machine. Then `/cadrer:choisir`
and the rest answer by name in any Claude Code window opened in that folder. `claude plugin details
cadrer` shows what it costs you per session; `claude plugin uninstall cadrer --scope project`
removes it.

Before 0.3.0 the plugin was called `workflow` and the skills had their English names
(`/workflow:ideate` …). Uninstall that one and install `cadrer`; the build folders are the same.

## Names, and why the skills are in English

The names are French because the method is: **CADRER** — the verb *cadrer*, to keep something in
frame — and the six steps spell it. `NAMING.md` records the decisions.

The skill *bodies* stay in English on purpose, and there is no French translation of them:

- A skill is read by the agent, never by the learner. Its text is a standing instruction, loaded on
  every run.
- French costs more tokens for the same instruction — about a quarter more, measured with
  `tools/token_estimate.py` across eight public tokenizers. A learner would pay that on every run.
- Every skill ends its opening paragraph with one line: answer, and write every file, in the language
  the person writes in. A learner who writes in French gets French questions and French build files
  from an English skill.
- One set to maintain. Two sets drift.

## Tools

`tools/token_estimate.py` counts what a skill set costs in tokens, and can compare the English set
with a French translation (paired through the CADRER names, or `--map EN=FR`). Claude's tokenizer is
not public, so it counts with public ones — OpenAI's, Llama 3, Qwen 3, DeepSeek V3, Mistral Nemo,
Gemma 3 — and reports the FR/EN ratio across them; with `ANTHROPIC_API_KEY` set it adds Claude's
exact count from `count_tokens`.

```
uv run tools/token_estimate.py plugins/cadrer/skills                            # one set
uv run tools/token_estimate.py plugins/cadrer/skills path/to/translation/skills  # EN against FR
```

`--detail o200k` breaks it down per skill, `--json` prints the numbers. The public page for non-technical
readers, *Le prix du français*, lives in its own repo, `~/Desktop/prix-du-francais`.

## Where these come from

The skills in this repo are **copies**. They are written and revised in `~/Desktop/skill-hub/skills`, which is the
source of truth, and copied here to be published. Do not edit them here — the next copy out will overwrite it.

`refine` is adapted from Matt Pocock's `grilling` (MIT) — github.com/mattpocock/skills.
