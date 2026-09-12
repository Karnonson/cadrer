---
name: {{slug}}
description: {{description}}
argument-hint: {{argument_hint}}
---

Read `builds/<NN>-<slug>/{{idea_file}}` and `decisions.md` first (a number or name given as argument picks the folder, else the only one, else ask). Everything you need is in those two files and, if present, `prototypes/`. Do not interview. If a decision is truly missing, ask that one question and nothing else; if merely unstated, fill it in and mark it {{h_assumed}}. {{language_line}}

Before writing, name the **seams**: the few places where the finished thing can be checked from the outside — what goes in, what must come out — without reading its insides. Fewer is better; one per kind of person who touches it is plenty. Put them to the person in plain words — "we test it by: <what happens> → <what they see>" — and wait for a yes. That is the only check-in.

Then write `spec.md` beside the other two with exactly these headings:

- **{{h_spec_problem}}** — from their side, two or three sentences, lifted from the frame.
- **{{h_solution}}** — what they will see and do. No technology words.
- **{{h_look}}** — only if it has a screen: the feel in three words, colours by name, type mood, imagery, one reference site. {{h_assumed}} if the {{slug_refine}} step left it.
- **{{h_stories}}** — a long numbered list: "{{story_form}}". One story per behaviour, every settled decision covered, awkward cases included (not a client call, first run, empty list).
- **{{h_impl}}** — one line per decision that shapes the build, {{h_assumed}} ones included and marked, plus the parts to build and how they talk to each other. No file paths, no code — unless a prototype pinned a shape better than prose, or a name the person will type is itself the decision; then inline it and say where it came from.
- **{{h_testing}}** — the seams agreed above, and the rule: test what it does, never how.
- **{{h_out_of_scope}}** — {{h_dropped}} from `decisions.md` and {{h_not_yet}} from `{{idea_file}}`, verbatim.
- **{{h_open}}** — everything {{h_assumed}}, marked, so the next step can question it.

Re-read once: every {{h_settled}} row must appear above; anything two-readable, or said two ways in two places, fix in place; report what changed. Stop; do not offer slices or code.
