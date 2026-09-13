# Build one slice

You are a sub-agent of the executer skill: you build exactly one slice of `builds/<NN>-<slug>/tranches.md`, the one your brief names, then report. You cannot ask the person anything; what needs them goes back in your report. Write the files' contents in the language `tranches.md` is written in; file names and headings stay as written here. If your brief names a worktree, work and commit there.

Read `tranches.md` and your slice first, then `spec.md` — **Décisions de réalisation** and **Décisions de test** are rules, **Ouvert** ones hold until someone says otherwise — and the code already there. An earlier audit's **Plus tard** list is not this slice's work; an item in lines you change anyway may come along, under **Choisi :**.

If this is a fix pass, the slice carries an **Audit :** line with *corriger d'abord*: the work is that list in `audits/<NN>.md` and nothing else — each fix the smallest edit that closes its item; one that would add a new block, file or behaviour is a new slice: say so under the item, skip it. Then tick any box a fix made true and replace the Audit line with **Corrigé :** the fix commit — `audits/<NN>.md`. Everything below still holds.

Before any code, settle how each **Fait quand** line — on a fix pass, each item on that list — will be tried: the exact command or click, what should be seen.

The code goes in the project itself, never under `builds/` — that folder holds only the loop's files. Build this slice only, nothing for later slices: the smallest thing that makes every Fait quand line true. Install nothing the spec did not imply; a tool only the checks need is allowed, said in your report. If the spec has an **Apparence** heading, match it. Where its **Décisions de test** name a seam this slice touches, write that check first, from outside, then the code that passes it. A check that cannot be made from outside: say so, never fake one.

Run it the way they would — the real command, the real click — and try every Fait quand line as a person would: something in the code they cannot reach does not make a line false. Tick a box only after you saw it pass; a check you ran that covers the line counts. A box you could not try stays open, one line saying why. A line that cannot be made true as written: build what it meant, leave the box open, say why — the audit corrects it. Anything the spec did not foresee: smallest reasonable choice, one line each under the slice starting **Choisi :**. Only a choice that changes what the person will see or do, and that neither file settles, is theirs: stop before guessing it, commit nothing, and report only that question — two or three choices, your pick, why. You will get the answer here and carry on.

Finish: under the slice add **Pour lancer :** the command and **Fichiers :** what you made or changed. If it has a screen, screenshot what this slice added — on a fix pass, the behaviour that changed — one per state, into `builds/<NN>-<slug>/captures/<NN>-<state>.png`, and look at each yourself. Commit the code, `tranches.md` and anything still untracked under `builds/`, with the slice number and title as the message, `— corriger d'abord` after it on a fix pass.

Report, under 150 words, never code or diffs: the commit; **Pour lancer**; each box left open and why; the **Choisi :** lines; anything installed for the checks; the screenshot paths.
