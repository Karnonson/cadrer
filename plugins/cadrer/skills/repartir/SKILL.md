---
name: repartir
description: "Découper en tranches. À utiliser quand la spec existe et avant tout code. Découpe la spec en tranches traçantes, chacune disant ce qui la bloque, dans `tranches.md`. Ne construit jamais."
argument-hint: "[numéro ou nom du dossier]"
---

Read `builds/<NN>-<slug>/spec.md` first (a number or name given as argument picks the folder, else the only one, else ask); `architecture.md` says what runs where, and `idee.md` and `decisions.md` are there if a story needs its reason. If the project holds code, read it; tidying that eases the build is its own slice, before the ones it eases. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

Cut the work into **tracer bullets**: each slice a narrow but complete path from what the person does to what they see, so that when done there is something to try. Never a layer on its own ("the database", "the window"). The first slice is the thinnest thing that runs end to end; later ones widen it. A slice may end where the next begins — a button that shows a placeholder — as long as it shows something. Each buildable in one sitting from a cold start: a few hours, one screen or one rule or one form. Every slice is built and tried on their computer, the way **En local** in `architecture.md` says: putting it online is not a slice, and neither is creating an account or a secret — that is theirs, under **À faire à la main**.

Give every slice its **Bloqué par**: the slices that must be done before it can start. None means it can start now. Number blocker-first.

Then write `tranches.md` beside the spec, one section per slice:

```
## <NN> — <title>

**À construire :** what works end to end when this is done, from their side.
**Bloqué par :** <NN>, <NN> — or "rien, peut démarrer".
**Fait quand :**
- [ ] something they can see or try
- [ ] …
```

Every user story lands in exactly one slice's "Fait quand"; leftovers go under **Non placé** at the end, with why. The first slice with a screen gets a Fait quand line that it looks the way the spec's **Apparence** says. No file paths, no code — unless a prototype pinned a shape better than prose; inline it and say so.

Then spawn one read-only sub-agent given only `idee.md`, `decisions.md`, `architecture.md`, `spec.md` and `tranches.md` — not this conversation, so it reads them cold, as the build will. Brief: where the files disagree — a Décidé row missing from the spec or said differently there, a user story in no Fait quand line or in two, a Fait quand line no story or decision asks for, a slice going against **Décisions de réalisation**, **Décisions de test** or `architecture.md` (a part it does not name, something that cannot be tried the way **En local** says, an account or secret a slice needs with no *avant la construction* item under **À faire à la main**), **Hors périmètre** not matching Abandonné and Pas encore, a first screen slice without its Apparence line; and whether the cut holds — a slice that is a layer or cannot be tried on its own, one too big for one sitting or too thin to be its own, a **Bloqué par** missing or not needed, two slices better as one. Quote the lines each finding answers, file and heading. Under 1000 words.

Fix what the cut got wrong in `tranches.md` yourself — these are your calls, never the person's. A disagreement between the earlier files is theirs: put it to them as what they want to happen, what each file says, which wins; then fix the file that lost. Show the list — number, title, needs which steps, what can be tried when done — and what the review changed. Then ask two things they can answer without knowing how software is built, in one tool call if you have it: is this the order they want to try things in (offer only orders the Bloqué par lines allow)? Is anything they expected missing — it goes into `spec.md` as a story and into a slice — or here they would rather leave for later — it goes under **Non placé**, with their reason? Wait. Fix, show again, until they say yes. That is the only check-in. Stop; do not offer to build.

Run again after an audit says *retour à la tranche*, when answers in `a-trancher.md` change what gets built, or on **Reste à faire** in `livraison.md` — its lines not marked *à la main*: built slices keep their numbers, ticks and lines; change only the line the audit, the answer or the livraison named — in `spec.md` too when it says so — and cut what needs new work into a slice numbered after the built ones, adding a story to `spec.md` for an answer. After each answer you placed, add `→ <NN>`, the slice it went to. Same review, same check-in.
