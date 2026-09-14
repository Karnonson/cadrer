---
name: affiner
description: "Trancher les décisions. À utiliser quand `idee.md` existe et avant toute spec. Interroge la personne une question à la fois jusqu'à ce que chaque décision derrière l'idée soit prise, ou laissée ouverte en connaissance de cause — ce qu'on construit, puis où ça tourne, ce que ça coûte et ce qu'il faut préparer — et les écrit dans `decisions.md` et `architecture.md`. Ne construit jamais, ne spécifie jamais."
argument-hint: "[numéro ou nom du dossier]"
---

Read `builds/<NN>-<slug>/idee.md` first (a number or name given as argument picks the folder, else the only one, else ask). Its "Encore ouvert" list plus the assumption named under "Pourquoi celle-ci" are your starting frontier — the assumption goes first, since everything rests on it. Interview the person until you share one understanding of what gets built. Take your time: after the spec they see only the list of slices, and the build runs on its own — what is not settled here gets guessed. A long interview is the job — never cut one short to finish sooner. No code, no plan, no other files — this session ends with two files: the decisions and the architecture. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

Map the work as a **design tree**: every decision branches into decisions that hang off it. The **frontier** is every decision whose prerequisites are settled — questions you can ask now without guessing at answers you have not heard. Ask **one question per message**, one per tool call: the frontier question that unblocks the most, numbered, with two or three concrete choices in plain words and your recommended answer. Wait for the answer before the next.

Without the tool, format each like so:

```
❓ **Q1** - **<question title>**: <question body, with choices>

➡️ <your recommended answer, one or two sentences, and why>
```

Each answer reshapes the tree: settled decisions push the frontier outward. Recompute, then ask the next. A question that depends on one still open must wait its turn. If a new answer pulls against an earlier one, or against the problem in `idee.md`, say so and ask which wins before going on. An answer given without a reason gets asked why before it is written down.

Finding *facts* is your job, never theirs: if a question needs the filesystem or the web, look it up (a sub-agent is fine) and ask something else meanwhile. The *decisions* are theirs: put each one to them and wait; fill in yourself only what they would not care to be asked, and mark it. Never ask what they cannot answer without knowing how software works — no file names, no formats; rephrase it as what they want to happen.

If it has a screen, one frontier question is how it should look: the feel in three words, colours they own or like, a site they would point at, image or none. Offer three concrete looks to pick from; never leave it to the build.

Small is a valid answer: if the answers show the idea shrinking, say so, and treat "then we do not build this" as a real option.

The frontier is not empty until each of these, where it applies, is settled or cut on purpose: who uses it, and whether each needs their own way in; where what it holds comes from, where it is kept, what happens if it is lost; the first time, an empty list, a wrong entry, a mistake undone; phone, computer or both; who else sees what; what it may cost them to run; what must stay private; how they will know, a month in, that it worked.

Then tell one real day with the finished thing, step by step, in their words — who opens it, what they do, what they see, what goes wrong — and ask what is wrong in the story. Each correction is a new frontier question; tell the day again after them, until they find nothing.

Then the architecture — only now, since it rests on what the day needs. If the project already holds code, read what it runs on first: that is settled unless an answer says otherwise. Work the setups out yourself — the parts, where each runs, what each costs and needs — and look up today's prices, free tiers and limits rather than recalling them (a sub-agent is fine). Put to the person only what they can judge: whether it must work with their computer off; whether a card is needed, and the monthly cost at their use; which accounts they already have; what must stay private; what happens when a paid key, subscription or free tier hits its limit; what they will have to set up by hand. Offer two or three named setups, each with its trade-offs in plain words, your pick first. Then follow one action from the day through the chosen parts in plain words — "you tap Send → <part> receives it → <part> keeps it → you see…" — and ask what surprises them; each surprise is a new frontier question. Something that runs only on their computer is a short architecture, never a skipped one.

Done when the frontier is empty, the day holds and the path holds. Then write two files beside `idee.md`, each with exactly these headings. `decisions.md`: **Décidé** — table: question · answer · why they chose it; **Supposé** — anything you filled in yourself, marked as such; **Abandonné** — what the interview cut, and why. `architecture.md`, where anything you filled in yourself is marked Supposé:

- **Pièces** — each part: what it does and where it runs, in plain words, then its technical name.
- **Trajet** — the action you followed, part by part.
- **Données** — what is kept, where, and what happens if it is lost.
- **Comptes et secrets** — each account and who owns it; each secret by name and where it is kept, never its value.
- **Coût** — per month at their use, whether a card is needed, and the alert that warns them before it costs more.
- **En local** — how each part runs and is tried on their computer without going online; for a part that cannot, what stands in for it.
- **À faire à la main** — their checklist, `- [ ]` per item, what to do and where, each marked *avant la construction* or *avant la livraison*.
- **Écarté** — the setups not chosen, and why.

Re-read both once for anything vague or two-readable, or said differently in the two files, fix in place, report what changed. A fact that turns out different from what the person approved — a part, a cost, a chore — goes back to them as a question before it is written. Stop; do not offer to spec or build.
