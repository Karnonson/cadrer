---
name: detailler
description: Détailler — spec. Use after the decisions are settled and before any slices. Turns the Idea Frame and the decisions into one spec — synthesis only, no interview. Never builds.
---

Read `builds/<NN>-<slug>/idea.md` and `decisions.md` first (a number or name given as argument picks the folder, else the only one, else ask). Everything you need is in those two files and, if present, `prototypes/`. Do not interview. If a decision is truly missing, ask that one question and nothing else; if merely unstated, fill it in and mark it Assumed. Answer, and write every file, in the language the person writes in.

Before writing, name the **seams**: the few places where the finished thing can be checked from the outside — what goes in, what must come out — without reading its insides. Fewer is better; one per kind of person who touches it is plenty. Put them to the person in plain words — "we test it by: <what happens> → <what they see>" — and wait for a yes. That is the only check-in.

Then write `spec.md` beside the other two with exactly these headings:

- **Problem** — from their side, two or three sentences, lifted from the frame.
- **Solution** — what they will see and do. No technology words.
- **Look** — only if it has a screen: the feel in three words, colours by name, type mood, imagery, one reference site. Assumed if the affiner step left it.
- **User stories** — a long numbered list: "As <who>, I want <thing>, so that <benefit>". One story per behaviour, every settled decision covered, awkward cases included (not a client call, first run, empty list).
- **Implementation decisions** — one line per decision that shapes the build, Assumed ones included and marked, plus the parts to build and how they talk to each other. No file paths, no code — unless a prototype pinned a shape better than prose, or a name the person will type is itself the decision; then inline it and say where it came from.
- **Testing decisions** — the seams agreed above, and the rule: test what it does, never how.
- **Out of scope** — Dropped from `decisions.md` and Not yet from `idea.md`, verbatim.
- **Open** — everything Assumed, marked, so the next step can question it.

Re-read once: every Settled row must appear above; anything two-readable, or said two ways in two places, fix in place; report what changed. Stop; do not offer slices or code.
