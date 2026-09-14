# cadrer

**CADRER** is the six-step build loop taught in the free course **Première Livraison**. This repo is
its Claude Code marketplace, with the loop as one plugin, `cadrer`: six French commands, French file
names and headings, and Claude answering and writing in the language you write to it in.

| Step | Command | Writes |
| --- | --- | --- |
| **C**hoisir | `/cadrer:choisir` | `idee.md` |
| **A**ffiner | `/cadrer:affiner` | `decisions.md`, `architecture.md` |
| **D**étailler | `/cadrer:detailler` | `spec.md` |
| **R**épartir | `/cadrer:repartir` | `tranches.md` |
| **E**xécuter | `/cadrer:executer` | the code, ticks under each slice, and an audit per slice through réviser |
| **R**éviser | `/cadrer:reviser` | `audits/<NN>.md` |

All six write into one folder per idea, `builds/<NN>-<slug>/`, and each reads what the last one left.
`affiner` settles what gets built, then where it runs, what it costs and what the person prepares by
hand, in `architecture.md`. `/cadrer:executer` checks those chores are done, then runs the rest on its
own, on the computer, never online: each open slice is built by one sub-agent, audited by another
following `reviser`, fixed and audited again if the audit finds a defect, then the next. A choice only
the person can make does not stop it: the build takes its pick and writes the question into
`a-trancher.md`, asked at the end. One code review covers the whole run, in `audits/code.md`.
`/cadrer:executer <dossier> <NN>` does one slice; `parallele` builds open slices at once, one git
worktree each, merged back when audited. A full run spends tokens on every slice, two to four
sub-agents each. `/cadrer:reviser` still runs alone, in its own sub-agent with two reviewers of its
own, on a slice built by hand.

Putting it online is `/cadrer:livrer`, a command outside the six letters, run with the person at the
keyboard once every slice is audited *fusionner*. It asks for the *avant la livraison* chores, where
secrets are typed by the person and never shown, then shows a table of what it will create, pay or
send and how to undo each, and waits for a yes. It then puts the build where `architecture.md` says,
follows the architecture's **Trajet** on the real address, and writes `livraison.md`: the address, how
to do it again, what was seen online, how to go back, and what is left for `repartir`.

Command names carry no accents — a skill name is lowercase letters, digits and hyphens — so you type
`detailler`, `repartir`, `executer`, `reviser`.

## Install

In a terminal, standing in the project you want the loop in:

```
claude plugin marketplace add Karnonson/cadrer
claude plugin install cadrer@cadrer --scope project
```

`--scope project` switches the plugin on for that folder only (it writes `.claude/settings.json`
there); leave it off and it switches on for every project on your machine. Then `/cadrer:choisir` and
the rest answer by name in any Claude Code window opened in that folder. `claude plugin details
cadrer` shows what it costs you per session; `claude plugin uninstall cadrer --scope project` removes
it.

Before 0.3.0 the plugin was called `workflow` (`/workflow:ideate`, from the marketplace
`workflow-skills`). Uninstall that one and install `cadrer`. Build folders started with `workflow`
use the English file names (`idea.md`, `slices.md`), so start new builds with `cadrer`.

## Languages

Three layers, three readers:

- **What the learner sees is French.** Commands, `/` menu descriptions and argument hints, file names,
  the headings inside each file, the markers the later steps look for (`Fait quand`, `Bloqué par`…)
  and the verdicts (`fusionner`, `corriger d'abord`, `retour à la tranche`). These are fixed: the
  next skill and the course's file checks read them by string.
- **What Claude writes follows the person.** Each skill says: answer, and write the files' contents,
  in the person's language; file names and headings stay as written here. A learner who writes in
  French gets French. To pin it for every window, set `"language": "French"` in
  `~/.claude/settings.json`, or pick it in `/config`.
- **What only Claude reads is English.** The skill bodies. A skill is read by the agent, never by the
  learner, and French costs more tokens for the same instruction.

Measured with `tools/token_estimate.py` on 2026-09-12, o200k tokenizer, against an English-vocabulary
render of the same bodies (commit `f9eb4f1`):

| | English vocabulary | `cadrer` |
| --- | --- | --- |
| Six skills, loaded when one runs | 4,448 | 4,657 (1.05×) |
| Six descriptions, always loaded | 318 | 416 (1.31×) |

A fully translated French body was 1.27–1.41× instead. `NAMING.md` records the decisions.

The skills under `plugins/cadrer/skills/` are the source. Edit them by hand; `claude plugin validate
plugins/cadrer` checks the manifest.

## Tools

`tools/token_estimate.py` counts what a skill set costs in tokens, and can compare two sets (paired
through the CADRER slugs, or `--map EN=FR`). Claude's tokenizer is not public, so it counts with public
ones — OpenAI's, Llama 3, Qwen 3, DeepSeek V3, Mistral Nemo, Gemma 3 — and reports the FR/EN ratio
across them; with `ANTHROPIC_API_KEY` set it adds Claude's exact count from `count_tokens`.

```
uv run tools/token_estimate.py plugins/cadrer/skills              # one set
uv run tools/token_estimate.py path/to/en/skills plugins/cadrer/skills   # EN against FR
```

`--detail o200k` breaks it down per skill, `--json` prints the numbers. The public page for
non-technical readers, *Le prix du français*, lives in its own repo, `~/Desktop/prix-du-francais`.

## Credits

`affiner` is adapted from Matt Pocock's `grilling` (MIT) — github.com/mattpocock/skills.
