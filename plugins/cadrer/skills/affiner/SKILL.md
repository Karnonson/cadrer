---
name: affiner
description: "Trancher les décisions. À utiliser quand `idee.md` existe et avant toute spec. Interroge la personne une question à la fois jusqu'à ce que chaque décision derrière l'idée soit prise, ou laissée ouverte en connaissance de cause, puis les écrit dans `decisions.md`. Ne construit jamais, ne spécifie jamais."
argument-hint: "[numéro ou nom du dossier]"
---

Read `builds/<NN>-<slug>/idee.md` first (a number or name given as argument picks the folder, else the only one, else ask). Its "Encore ouvert" list plus the assumption named under "Pourquoi celle-ci" are your starting frontier — the assumption goes first, since everything rests on it. Interview the person until you share one understanding of what gets built. No code, no plan, no other files — this session ends with one decisions file. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

Map the work as a **design tree**: every decision branches into decisions that hang off it. The **frontier** is every decision whose prerequisites are settled — questions you can ask now without guessing at answers you have not heard. Ask **one question per message**, one per tool call: the frontier question that unblocks the most, numbered, with two or three concrete choices in plain words and your recommended answer. Wait for the answer before the next.

Without the tool, format each like so:

```
❓ **Q1** - **<question title>**: <question body, with choices>

➡️ <your recommended answer, one or two sentences, and why>
```

Each answer reshapes the tree: settled decisions push the frontier outward. Recompute, then ask the next. A question that depends on one still open must wait its turn. If a new answer pulls against an earlier one, say so and ask which wins before going on.

Finding *facts* is your job, never theirs: if a question needs the filesystem or the web, look it up (a sub-agent is fine) and ask something else meanwhile. The *decisions* are theirs: put each one to them and wait; fill in yourself only what they would not care to be asked, and mark it. Never ask what they cannot answer without knowing how software works — no file names, no formats; rephrase it as what they want to happen.

If it has a screen, one frontier question is how it should look: the feel in three words, colours they own or like, a site they would point at, image or none. Offer three concrete looks to pick from; never leave it to the build.

Small is a valid answer: if the answers show the idea shrinking, say so, and treat "then we do not build this" as a real option.

Done when the frontier is empty. Then write `decisions.md` beside it with exactly these headings: **Décidé** — table: question · answer · why they chose it; **Supposé** — anything you filled in yourself, marked as such; **Abandonné** — what the interview cut, and why. Re-read once for anything vague or two-readable, fix in place, report what changed. Stop; do not offer to spec or build.
