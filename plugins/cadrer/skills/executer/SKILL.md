---
name: executer
description: "Construire les tranches. À utiliser quand les tranches existent. Enchaîne seul chaque tranche ouverte : un sous-agent la construit, un autre l'audite comme la compétence reviser, un troisième corrige si l'audit le demande, puis la suivante — jusqu'au bout, ou jusqu'à une décision qui revient à la personne. Une tranche nommée : celle-là seule. `parallele` : les tranches ouvertes en même temps, chacune dans son worktree."
argument-hint: "[dossier] [tranche | parallele]"
---

You run the build loop; the building and the auditing happen in sub-agents, never in this window. Read `builds/<NN>-<slug>/tranches.md` (first argument picks the folder, else the only one, else ask). **Open** slices are those not yet audited *fusionner* whose **Bloqué par** all are — the **Audit :** lines say which. A slice number after the folder: that slice only — built, audited, fixed and audited again if the audit asks — then stop. `parallele`: see below. Otherwise one open slice at a time, first open first, until none is left. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

This window keeps only reports, so it lasts the whole run: never read the code, the diffs or the screenshots here until the end. Before each slice, re-read `tranches.md` and take the next open slice from it, not from memory — a run that stopped, or was compacted, picks up where the file says: a slice with ticked boxes and no **Audit :** line starts at 2, one with an Audit line not yet committed — a typed `/cadrer:reviser` leaves it so — starts at 3, one whose Audit line says *corriger d'abord* starts at 1 as a fix pass.

Each slice, on the branch you are on:

1. **Build.** Start one sub-agent. Brief: the folder, the slice number, whether this is a fix pass, and to read `${CLAUDE_SKILL_DIR}/construire.md` and follow it. Wait for its report. If it returns a question, put it to the person, send the answer to that same sub-agent, and wait again.
2. **Audit.** Start one sub-agent. Brief: the folder, the slice number, and to read `${CLAUDE_PLUGIN_ROOT}/skills/reviser/SKILL.md` and follow it — it starts the two axis sub-agents itself. Wait for its verdict. A question it returns goes to the person the same way.
3. **Record.** Commit `audits/<NN>.md` and `tranches.md` as `audit <NN> — <verdict>`.
4. **Next.** *fusionner*: the next open slice. *corriger d'abord*: back to 1 on the same slice as a fix pass, then 2 — a second pass. *retour à la tranche*: start no new slice.

With `parallele`: every open slice at once, one worktree each — `git worktree add ../<slug>-<NN> -b tranche-<NN>` from the branch you are on — and every brief names its worktree, where the sub-agent works and commits. On *fusionner*, `git merge --no-ff tranche-<NN>` into your branch, `git worktree remove ../<slug>-<NN>`, then start the slices that merge opened. A merge that conflicts: `git merge --abort`, start nothing new, let running slices finish their audit, and stop naming the files both slices changed.

Stop when no slice is open, on *retour à la tranche*, on a merge conflict, or when the person leaves a returned question unanswered. Then look at the screenshots the reports named, and end with:

- a table — slice · title · verdict · how to try it (its **Pour lancer**);
- the screenshots, one line each on what it shows;
- every box left open and why, every **Choisi :** line, the **Plus tard** items;
- why it stopped and what comes next — after *retour à la tranche*, the repartir skill on the line the audit named; slices still to build, `/cadrer:executer` again once that is done;
- in plain words, the first thing to try and how.

Never merge anything but a *fusionner* slice's worktree, never fix code here, never change a verdict.
