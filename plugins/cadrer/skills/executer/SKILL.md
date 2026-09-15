---
name: executer
description: "Construire les tranches. À utiliser quand les tranches existent. Vérifie ce que la personne devait préparer, puis enchaîne seul chaque tranche ouverte : un sous-agent la construit en local, un autre l'audite comme la compétence reviser, un troisième corrige un défaut trouvé, puis la suivante. Les questions pour la personne vont dans `a-trancher.md` sans arrêter la construction. Une tranche nommée : celle-là seule. `parallele` : les tranches ouvertes en même temps, chacune dans son worktree."
argument-hint: "[dossier] [tranche | parallele]"
---

You run the build loop; the building and the auditing happen in sub-agents, never in this window. Read `builds/<NN>-<slug>/tranches.md` (first argument picks the folder, else the only one, else ask). **Open** slices are those not yet audited *fusionner* whose **Bloqué par** all are — the **Audit :** lines say which. A slice number after the folder: that slice only — built, audited, fixed and audited again if the audit asks — then stop. `parallele`: see below. Otherwise one open slice at a time, first open first, until none is left. Answer, and write the files' contents, in the person's language; file names and headings stay as written here. Put questions to the person through the AskUserQuestion tool when you have it: your pick as the first option, the context it needs in your message just before.

This window keeps only reports, so it lasts the whole run: never read the code, the diffs or the screenshots here until the end. Before each slice, re-read `tranches.md` and take the next open slice from it, not from memory — a run that stopped, or was compacted, picks up where the file says: a slice with ticked boxes and no **Audit :** line starts at 2, one with an Audit line not yet committed — a typed `/cadrer:reviser` leaves it so — starts at 3, one whose Audit line says *corriger d'abord* starts at 1 as a fix pass.

**Before the first slice**, note the commit you start on — when that slice picks up where a stopped run left it, the commit before its first build instead — then read **À faire à la main** in `architecture.md`. No `architecture.md`: the builds and audits need it — say the affiner step writes where it runs, and stop. Put every unticked *avant la construction* item to the person in one message — what to do, where, why it is needed — and wait until they say it is done. Check each one you can from here without showing a secret's value — the variable is named where **Comptes et secrets** says, the command answers, the account lets you in — and tick it; one nothing here can check, tick on their word with *confirmé par la personne* after it; commit `architecture.md` as `À faire à la main : <what was checked>`. One that fails: say what you saw, and start no slice until it passes or they cut it.

Each slice, on the branch you are on:

1. **Build.** Start one sub-agent. Brief: the folder, the slice number, whether this is a fix pass, and to read `${CLAUDE_SKILL_DIR}/construire.md` and follow it. Wait for its report. If it returns a question, put it to the person, send the answer to that same sub-agent, and wait again.
2. **Audit.** Start one sub-agent. Brief: the folder, the slice number, that the executer skill started it, and to read `${CLAUDE_PLUGIN_ROOT}/skills/reviser/SKILL.md` and follow it. Wait for its verdict. A question it returns goes to the person the same way.
3. **Record.** Commit `audits/<NN>.md`, `tranches.md` and `a-trancher.md` if it changed, as `audit <NN> — <verdict>`.
4. **Next.** *fusionner*: the next open slice. *corriger d'abord*: back to 1 on the same slice as a fix pass, then 2 — a second pass. *retour à la tranche*: start no new slice.

An audit that found a secret's value in a tracked file stops the run before any fix pass: tell the person which secret and which commit — never the value — that its value must be changed where it was issued, since a later commit leaves it in git history, and that the branch must not be pushed until that commit is taken out of it; offer to do that, and do it only with their yes.

A new entry in `a-trancher.md` never stops the run and never starts a fix pass: the slice goes on with what was built.

With `parallele`: every open slice at once, one worktree each — `git worktree add ../<slug>-<NN> -b tranche-<NN>` from the branch you are on — and every brief names its worktree, where the sub-agent works and commits. On *fusionner*, `git merge --no-ff tranche-<NN>` into your branch, `git worktree remove ../<slug>-<NN>`, then start the slices that merge opened. A merge whose only conflict is `a-trancher.md`: keep both slices' entries in that file, `git add` it and finish the merge. Any other conflict: `git merge --abort`, start nothing new, let running slices finish their audit, and stop naming the files both slices changed.

Stop when no slice is open, on *retour à la tranche*, on a merge conflict, on a committed secret, or when the person leaves a returned question unanswered. If a slice was built or resumed in this run, start one sub-agent for the **Code** axis. Brief: the folder, and to read the Code axis paragraph in `${CLAUDE_PLUGIN_ROOT}/skills/reviser/SKILL.md` and follow it over `git diff <start commit>...HEAD` with the same excludes that file gives, never edit code, write the report under a heading naming the two commits at the end of `audits/code.md` beside `tranches.md`, return under 100 words. Commit that file as `audit code`. Then look at the screenshots the reports named, and end with:

- a table — slice · title · verdict · how to try it (its **Pour lancer**);
- the screenshots, one line each on what it shows;
- every box left open and why, every **Choisi :** line, the **Plus tard** items and what the Code axis found;
- why it stopped and what comes next — after *retour à la tranche*, the repartir skill on the line the audit named; slices still to build, `/cadrer:executer` again once that is done; every slice *fusionner* and every a-trancher answer placed, `/cadrer:livrer` puts it online;
- in plain words, the first thing to try and how.

Then put each `a-trancher.md` entry with an empty **Réponse :** to the person — up to four per tool call, what was built as the first choice — and write each answer there. If an answer changes what was built, commit the file and say the repartir skill turns it into slices; if none does, commit it and say so.

Never merge anything but a *fusionner* slice's worktree, never fix code here, never change a verdict.
