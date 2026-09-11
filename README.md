# workflow-skills

A Claude Code marketplace holding one plugin, `workflow`: the six-step build loop taught in the
AI Coding Mini-Course.

| Step | Skill | Writes |
| --- | --- | --- |
| 1 | `/workflow:ideate` | `idea.md` |
| 2 | `/workflow:refine` | `decisions.md` |
| 3 | `/workflow:spec` | `spec.md` |
| 4 | `/workflow:slice` | `slices.md` |
| 5 | `/workflow:implement` | the code, plus ticks under the slice |
| 6 | `/workflow:audit` | `audits/<NN>.md` |

All six write into one folder per idea, `builds/<NN>-<slug>/`, and each reads what the last one left.

## Install

In a terminal, standing in the project you want the loop in:

```
claude plugin marketplace add Karnonson/workflow-skills
claude plugin install workflow@workflow-skills --scope project
```

`--scope project` switches the plugin on for that folder only (it writes `.claude/settings.json`
there); leave it off and it switches on for every project on your machine. Then `/workflow:ideate`
and the rest answer by name in any Claude Code window opened in that folder. `claude plugin details
workflow` shows what it costs you per session; `claude plugin uninstall workflow --scope project`
removes it.

## Names

The loop's French name is **CADRER** (Choisir, Affiner, Détailler, Répartir, Exécuter, Réviser), taught
in the free course **Première Livraison**. A rename of this plugin to `cadrer`, and a French twin for
the course's learners, are planned but not done — see `NAMING.md` for the decisions and the order they
happen in.

## Where these come from

The skills in this repo are **copies**. They are written and revised in `~/Desktop/skill-hub/skills`, which is the
source of truth, and copied here to be published. Do not edit them here — the next copy out will overwrite it.

`refine` is adapted from Matt Pocock's `grilling` (MIT) — github.com/mattpocock/skills.
