---
name: slice
description: "Répartir — slice. Use after the spec exists and before any code. Cuts the spec into tracer-bullet slices, each saying what blocks it. Never builds."
argument-hint: "[build number or name]"
---

Read `builds/<NN>-<slug>/spec.md` first (a number or name given as argument picks the folder, else the only one, else ask); `idea.md` and `decisions.md` are there if a story needs its reason. If the project holds code, read it; tidying that eases the build is its own slice, before the ones it eases. Answer, and write the files' contents, in English; file names and headings stay as written here.

Cut the work into **tracer bullets**: each slice a narrow but complete path from what the person does to what they see, so that when done there is something to try. Never a layer on its own ("the database", "the window"). The first slice is the thinnest thing that runs end to end; later ones widen it. A slice may end where the next begins — a button that shows a placeholder — as long as it shows something. Each buildable in one sitting from a cold start: a few hours, one screen or one rule or one form.

Give every slice its **Blocked by**: the slices that must be done before it can start. None means it can start now. Number blocker-first.

Show the list — number, title, blocked by, what can be tried when done — then ask three things in plain words, each with an example from the list: any step too big to try in one go, or too small to be its own? Is the order right — could a step be done before the ones blocking it? Any two steps better as one, or one as two? End with your own answer to each, so "yes" is a real option. Wait. Fix, show again, until they say yes. That is the only check-in.

Then write `slices.md` beside the spec, one section per slice:

```
## <NN> — <title>

**What to build:** what works end to end when this is done, from their side.
**Blocked by:** <NN>, <NN> — or "nothing, can start now".
**Done when:**
- [ ] something they can see or try
- [ ] …
```

Every user story lands in exactly one slice's "Done when"; leftovers go under **Unplaced** at the end, with why. The first slice with a screen gets a Done when line that it looks the way the spec's **Look** says. No file paths, no code — unless a prototype pinned a shape better than prose; inline it and say so.

Run again after an audit says *back to slice*: built slices keep their numbers, ticks and lines; change only the line the audit named — in `spec.md` too when it says so — and cut findings that need new work into a slice numbered after the built ones. Same check-in.

Re-read once: any slice that cannot be tried on its own, re-cut; report what changed. Stop; do not offer to build.
