---
name: detailler
description: "Écrire la spec. À utiliser quand les décisions sont prises et avant tout découpage. Transforme `idee.md` et `decisions.md` en une seule spec — synthèse seulement, pas d'entretien. Ne construit jamais."
argument-hint: "[numéro ou nom du dossier]"
---

Read `builds/<NN>-<slug>/idee.md` and `decisions.md` first (a number or name given as argument picks the folder, else the only one, else ask). Everything you need is in those two files and, if present, `prototypes/`. Do not interview. If a decision is truly missing, ask that one question and nothing else; if merely unstated, fill it in and mark it Supposé. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

Before writing, name the **seams**: the few places where the finished thing can be checked from the outside — what goes in, what must come out — without reading its insides. Fewer is better; one per kind of person who touches it is plenty. Put them to the person in plain words — "we test it by: <what happens> → <what they see>" — and wait for a yes. That is the only check-in.

Then write `spec.md` beside the other two with exactly these headings:

- **Problème** — from their side, two or three sentences, lifted from `idee.md`.
- **Solution** — what they will see and do. No technology words.
- **Apparence** — only if it has a screen: the feel in three words, colours by name, type mood, imagery, one reference site. Supposé if the affiner step left it.
- **User stories** — a long numbered list: "En tant que <qui>, je veux <quoi>, afin de <bénéfice>". One story per behaviour, every settled decision covered, awkward cases included (not a client call, first run, empty list).
- **Décisions de réalisation** — one line per decision that shapes the build, Supposé ones included and marked, plus the parts to build and how they talk to each other. No file paths, no code — unless a prototype pinned a shape better than prose, or a name the person will type is itself the decision; then inline it and say where it came from.
- **Décisions de test** — the seams agreed above, and the rule: test what it does, never how.
- **Hors périmètre** — Abandonné from `decisions.md` and Pas encore from `idee.md`, verbatim.
- **Ouvert** — everything Supposé, marked, so the next step can question it.

Re-read once: every Décidé row must appear above; anything two-readable, or said two ways in two places, fix in place; report what changed. Stop; do not offer slices or code.
