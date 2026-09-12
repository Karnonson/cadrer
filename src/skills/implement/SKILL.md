---
name: implement
description: {{description}}
argument-hint: {{argument_hint}}
---

Read `builds/<NN>-<slug>/{{slices_file}}` first (first argument picks the folder, second the slice; else the only folder, else ask). **Open** slices are those whose **{{m_blocked_by}}** are all done — done means audited *{{v_merge}}*. Take the one named, else the first open. Build on the branch you are on; only when told to run open slices in parallel, one window each, take a worktree — `git worktree add ../<slug>-<NN> -b {{slice_word}}-<NN>`. Then read `spec.md` — **{{h_impl}}** and **{{h_testing}}** are rules, **{{h_open}}** ones hold until someone says otherwise — and the code already there. An earlier audit's **{{h_later}}** list is not this slice's work; an item in lines you change anyway may come along, under **{{m_chosen}}{{colon}}**. {{language_line}}

If the slice carries an **{{m_audit}}{{colon}}** line with *{{v_fix}}*, the work is that list in `audits/<NN>.md` and nothing else — each fix the smallest edit that closes its item; one that would add a new block, file or behaviour is a new slice: say so under the item, skip it. Then tick any box a fix made true and replace the {{m_audit}} line with **{{m_fixed}}{{colon}}** the fix commit — `audits/<NN>.md`. Everything below still holds.

Before any code, say in plain words, under ten lines: what you will make, what it looks like from their side, the exact command or click that starts it, and how each **{{m_done_when}}** line — on a fix pass, each item on that list — will be tried. Then start: no check-in, the slice was agreed when the slices were cut. Stuck later: one question, two or three choices, your pick.

Build this slice only, nothing for later slices: the smallest thing that makes every {{m_done_when}} line true. Install nothing the spec did not imply; a tool only the checks need is allowed, said out loud. If the spec has a **{{h_look}}** heading, match it. Where its **{{h_testing}}** name a seam this slice touches, write that check first, from outside, then the code that passes it. A check that cannot be made from outside: say so, never fake one.

Run it the way they would — the real command, the real click — and try every {{m_done_when}} line as a person would: something in the code they cannot reach does not make a line false. Tick a box only after you saw it pass; a check you ran that covers the line counts. A box you could not try stays open, one line saying why. A line that cannot be made true as written: build what it meant, leave the box open, say why — the audit corrects it. Anything the spec did not foresee: smallest reasonable choice, one line each under the slice starting **{{m_chosen}}{{colon}}**.

Finish: under the slice add **{{m_how_to_run}}{{colon}}** the command and **{{m_files}}{{colon}}** what you made or changed. If it has a screen, screenshot what this slice added — on a fix pass, the behaviour that changed — one per state, look at each yourself, put them in your message. Commit the code, `{{slices_file}}` and anything still untracked under `builds/`, with the slice number and title as the message, `— {{v_fix}}` after it on a fix pass. Stop and say: run the audit skill in a new window before merging or starting the next slice.
