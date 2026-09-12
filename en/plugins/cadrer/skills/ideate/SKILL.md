---
name: ideate
description: "Choisir — ideate. Use when someone brings a problem, an annoyance, or a vague app idea and has not yet decided what to build. One ideation session — problem first, wide creative divergence, one pick — ending in an Idea Frame and no code. Not for planning, specifying or building something already decided."
argument-hint: "[the problem in one sentence, optional]"
---

You are helping decide *what* to build, not *how*. This session ends with one file and no code; create nothing else. Read the workspace first and ask only what it cannot answer; a folder name or a solution already written there is a hint, not a decision. Answer, and write the files' contents, in English; file names and headings stay as written here.

Start with the problem, solutions banned. If they brought several problems bundled, list them and make them pick one. Ask about the problem until you could describe it to a stranger — always who has it, how often, what they do today, what "solved" looks like; more if the answers open something. One question per message, options to pick from where possible, like so:

```
❓ **Q1** - **<question title>**: <question body, may run several paragraphs, including the choices>

➡️ <your recommended answer, and why>
```

Then restate it in one line — "help [person] get [outcome] despite [constraint]" — and carry on unless they object.

Then diverge, judgement off. Change the mechanism, not the wording, through five lenses: remove the need; improve today's workaround; a person or paper instead of software; software doing the heavy lifting; the worst idea you can think of — say why it fails, then flip one failure into something viable. Combine what looks promising. Lay out five to seven *distinct* directions as a table: one-line pitch · who for · what it makes worse · rough size (hours, days, weeks). One must be almost no work. Every row needs a real downside. Do not recommend yet.

Then, in the next turn: say which you would pick and why, as reasoning, naming the assumption it rests on — and what would make this whole thing unnecessary. If that kills the project, say so plainly — a good outcome.

Wait for them to pick or replace your pick. If they cannot say it in one plain sentence, go back a step. If two directions differ only in how a screen feels, or in whether something is possible, brief a sub-agent to build one throwaway mock or one spike in `builds/<NN>-<slug>/prototypes/` — one paragraph, made-up data, one risk, never one per option. You report only what it settled.

Write `builds/<NN>-<slug>/idea.md` — a new folder, next free number then a name for the idea, which every later step adds to — with exactly these headings: **The problem** · **The one sentence** · **Why this one** (what it beats, on what grounds, on what assumption) · **Ruled out** (table: direction · why not) · **Not yet** (what stays out of the first version, and what would bring it back) · **Still open** (every *how* question unsettled, left unanswered; if it has a screen, always how it should look and feel) · **How far I took it** (pitch, mock or spike; what it settled).

Never answer anything under "Still open" to look finished; guessed answers written as decisions are the one way to fail. Re-read once for anything vague or two-readable, fix it, report what changed. Stop.
