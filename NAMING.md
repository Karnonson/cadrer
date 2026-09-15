# Naming — CADRER

Names decided 2026-09-10. Built in this repo on 2026-09-12 as plugin `cadrer`
0.3.0: one plugin, French commands, French file names and headings, English
skill bodies, and Claude answering in the person's language. This file records
what the names are, what was tried and dropped on the way, and what still has
to happen, in what order.

## The two names

| Level | Name | What it is |
| --- | --- | --- |
| Offer | **Première Livraison** | The free course this loop is taught in — 6 sections, 47 lessons, idea to a link you can send |
| Method | **CADRER** | This loop. The French verb *cadrer* — to keep something in frame — and the six steps spell it |

`CADRER` is an acronym, written in caps when it names the method. The plain verb
`cadrer` stays lowercase and free. It names the marketplace, the plugin and,
the GitHub repo.

| Letter | Step | Command | Writes |
| --- | --- | --- | --- |
| **C** | Choisir | `/cadrer:choisir` | `idee.md` |
| **A** | Affiner | `/cadrer:affiner` | `decisions.md`, `architecture.md` |
| **D** | Détailler | `/cadrer:detailler` | `spec.md` |
| **R** | Répartir | `/cadrer:repartir` | `tranches.md` |
| **E** | Exécuter | `/cadrer:executer` | the code, ticks under each slice, an audit per slice through réviser, `a-trancher.md` |
| **R** | Réviser | `/cadrer:reviser` | `audits/<NN>.md` |
| — | Livrer | `/cadrer:livrer` | the build online, `livraison.md` |

Typing the six commands spells the method. Step 1 is **choisir**, not
*cadrer* — otherwise the word names both the loop and its first step.

## Why deploying and monitoring never join the acronym

They are not steps of this loop. CADRER is re-run per idea and per slice; going
live happens once, when a loop closes, and monitoring never stops. A continuous
activity inside a numbered sequence misdescribes the mechanism.

**One name for the whole thing (decided 2026-09-13).** CADRER names everything
an agent does with the person, from the idea to the thing online and kept
running. There is no second method name: **TENIR**, proposed for Part 2 on
2026-09-10, is dropped — two names for one plugin and one way of working is one
too many. So:

- **The acronym stays the build loop.** Six letters, six steps, run per idea.
- **What happens once or never stops is a command with no letter**:
  `/cadrer:livrer` puts the finished loop online (built in 0.6.0; section 05
  of the course, until now a lesson, becomes it). Monitoring, if it ever is
  a command, joins it the same way.
- **Architecture, secrets and tests are not commands.** They are topics inside
  the steps: `affiner` settles the architecture and writes `architecture.md`,
  secrets are named in its **Comptes et secrets**, tests are `detailler`'s
  **Décisions de test**.
- **The course has parts, not methods.** Part 1 is Première Livraison — the
  loop and `livrer`. Part 2 uses the same plugin, under a plain title.

**The rule:** an acronym is a counting contract. If a seventh skill ever truly
belongs to the build loop, it goes inside one of the six letters or out into the
outer ring. CADRER is never renamed to make room.

## Done 2026-09-12 — `cadrer` 0.3.0: one plugin, three layers

The audience is francophone. English is how the course author works, not a
learner language. So the plugin splits by who reads what:

| Layer | Reader | Language |
| --- | --- | --- |
| Commands, `/` menu descriptions and argument hints, file names, headings, markers, verdicts | the learner | French, fixed |
| What Claude says and writes under the headings | the learner | the person's language |
| Skill bodies | Claude only | English |

The fixed French vocabulary, as it stands in the skills:

| Where | Words |
| --- | --- |
| Files | `idee.md`, `decisions.md`, `architecture.md`, `spec.md`, `tranches.md`, `a-trancher.md`, `audits/<NN>.md`, `audits/code.md`, `livraison.md` |
| `idee.md` headings | Le problème · En une phrase · Pourquoi celle-ci · Écartées · Pas encore · Encore ouvert · Jusqu'où on est allé |
| `decisions.md` headings | Décidé · Supposé · Abandonné |
| `architecture.md` headings | Pièces · Trajet · Données · Comptes et secrets · Coût · En local · À faire à la main · Écarté |
| Chore markers | *avant la construction* · *avant la livraison* |
| `livraison.md` headings | En ligne · Mise en ligne · Vérifié en ligne · Si ça casse · Reste à faire (lines marked *à la main* stay the person's) |
| `a-trancher.md` markers | Question · Choix · En attendant · Réponse |
| `spec.md` headings | Problème · Solution · Apparence · User stories · Décisions de réalisation · Décisions de test · Hors périmètre · Ouvert |
| Story form | En tant que <qui>, je veux <quoi>, afin de <bénéfice> |
| Slice markers | À construire · Bloqué par · Fait quand · Non placé · Choisi · Pour lancer · Fichiers · Audit · Corrigé |
| Audit headings | Deuxième passe · Rectifié · Plus tard |
| Verdicts | fusionner · corriger d'abord · retour à la tranche |
| Worktree branch | `tranche-<NN>` |
| Screenshots, commits | `captures/<NN>-<state>.png` · `captures/livraison-<state>.png` · `audit <NN> — <verdict>` · `audit code` · `À faire à la main : <what>` · `livraison — <address>` · `livraison — arrêtée : <row>` · `parallele` |

`builds/`, `prototypes/`, `audits/` and the words *Spec*, *Code*, *Verdict*
stay as they are. `User stories` stays English because the course already says
it that way. The French colon takes its space (`**Fait quand :**`).

The language line at the end of each opening paragraph reads: *Answer, and
write the files' contents, in the person's language; file names and headings
stay as written here.* The headings are fixed so the later skills and the
lessons' file checks can read them by string; the prose follows whoever is
typing. A learner who wants French pinned everywhere sets `"language":
"French"` in `~/.claude/settings.json` — a built-in Claude Code setting; a
plugin cannot ship it.

Bodies are English. Measured the same day with `tools/token_estimate.py`
(o200k): the French vocabulary costs 1.05× an English one when a skill runs,
1.31× for the always-loaded descriptions; a fully translated body cost
1.27–1.41×.

## Dropped 2026-09-12 — `cadrer-en`, and the render that fed it

For a day the loop was two plugins rendered from one source: `cadrer` with
French commands and files, `cadrer-en` with English ones, picked at install.
`src/` held one templated body per step and a vocabulary file per language, and
`tools/render.py` wrote both plugins. Both are removed; they are in commit
`f9eb4f1`.

Dropped because there are no English learners. The English plugin served only
the author, who does not need it to read English skill bodies, and the render
existed only to keep it in step. With it gone, the French plugin is the source
and is edited by hand.

Also weighed and not taken:

- **Fixing the language to French in the skills.** The prose now follows the
  person instead, so the author gets English under the same French headings.
- **Asking the language at install.** A plugin manifest can declare options
  Claude Code prompts for when the plugin is enabled, and a non-sensitive answer
  can be inserted into skill text. Not used: every learner would answer French,
  the question lands at the install step where beginners stall, and the option
  cannot restrict the answer to a list.

## Dropped 2026-09-12 — a second repo

For an hour both plugins were named `cadrer`, with English commands in both,
and the English one lived in a generated `cadrer-en` repo so that both could
type `/cadrer:ideate`. Dropped the same day: two repos to keep in step for one
prefix, and the French commands are the method — a French learner types
`choisir`, not `ideate`.

## Dropped 2026-09-12 — the French twin

A hand-translated French body for each skill. Dropped because the learner never
reads the skill, because French bodies cost about a quarter more on every run,
and because two hand-kept sets drift. What the twin was for — French questions,
French files — is now the plugin itself: English body, French vocabulary.

### Copy for the course — why the skills are in English

To paste into lesson 4.2 (`tu` register, like the rest of the French export):

> **Pourquoi les compétences sont écrites en anglais ?**
>
> Le fichier d'une compétence n'est pas pour toi : c'est une consigne que Claude
> lit à chaque fois que tu la lances, et que tu ne vois jamais. Trois raisons de
> la laisser en anglais.
>
> 1. **Ça coûte moins.** Pour la même consigne, le français demande environ un
>    quart de jetons en plus — des jetons que tu paies à chaque lancement. Fais
>    l'essai avec tes propres phrases : [Le prix du français](https://karnonson.github.io/prix-du-francais/).
> 2. **Tout ce que tu vois est en français.** Tu tapes `/cadrer:choisir`, tu
>    expliques ton problème en français, et `idee.md` sort en français, avec
>    des titres en français. La compétence dit à Claude de te répondre dans ta
>    langue ; les noms de fichiers et les titres, eux, ne changent jamais.
> 3. **Rien ne se perd.** Chaque étape relit les titres laissés par la
>    précédente. Comme ils sont fixés, la chaîne tient d'un bout à l'autre.
>
> Pour que Claude te réponde toujours en français, même en dehors de CADRER,
> ajoute `"language": "French"` dans `~/.claude/settings.json`, ou choisis-le
> dans `/config`.

## Done 2026-09-12 — merged and renamed

PR #1 merged into `main`, and the GitHub repo renamed `workflow-skills` →
`cadrer` (GitHub redirects the old address). `cadrer@cadrer` now installs;
`workflow@workflow-skills` no longer resolves.

## Done 2026-09-13 — `cadrer` 0.4.0: the build runs itself

Typing `executer` then `reviser` in a new window, slice after slice, was the
tiring part. `/cadrer:executer` now runs the loop from one window: a sub-agent
builds each open slice (`skills/executer/construire.md` is its brief), another
audits it by reading `skills/reviser/SKILL.md`, a third fixes when the verdict is
*corriger d'abord*, then the next slice. It stops when nothing is open, on
*retour à la tranche*, or on a question only the person can answer, and ends
with a table of what to try. The main window keeps only reports and re-reads
`tranches.md` before each slice, so a stopped run resumes. `reviser` stays a
command: `context: fork`, so it also runs in a sub-agent when typed.

- **Why the audit is read, not invoked.** Claude cannot call a `context: fork`
  skill through the Skill tool; only a person typing it can. The loop's audit
  sub-agent reads the same file, so there is one source.
- **Why one slice at a time by default.** Parallel builders need one worktree
  each and a merge back, and two unblocked slices often touch the same screen:
  a conflict a non-developer cannot fix, to save waiting nobody watches.
  `parallele` keeps the option; a conflict stops the run.
- **The grilling moved up.** With the build unattended, the list of slices is
  the last thing the person checks. `choisir` asks for the last real case, what
  was tried, why now, and has the problem line attacked rather than approved;
  `affiner` sweeps the branches beginners forget and tells one real day with
  the finished thing until it holds; `detailler` reads the user stories back.
  Each says a long interview is the job.

## Done 2026-09-13 — `cadrer` 0.5.0: architecture up front, fewer round trips

0.4.0 ran on a real project: seven slices, a Telegram bot with a scheduled
routine. Read from the session files, weighting cache writes 1.25, cache reads
0.1 and output 5: first builds 48% of the cost, audit conductors 18%, fix
passes 16%, axis sub-agents 11%, the main window 7%. An audit cost about 40% of
a build; a fix and its re-audit about 85%. Three of the five fix passes fixed no
defect: they carried a new answer from the person (a routine redesigned after a
billing question, two wording changes), and with their re-audits they were
about a fifth of the run. The builders also stopped about six times on slice
01 alone — hosting, billing, region, where a token lives — because nothing
before the build had asked, and they put every slice online.

- **Architecture moved into `affiner`.** After the day holds, Claude works out
  two or three setups and asks only what a non-developer can judge — computer
  off or not, card and monthly cost, accounts they have, limits of a key or a
  free tier, chores by hand — then follows one action through the parts.
  `architecture.md` holds it; `detailler` points to it instead of inventing
  parts, `repartir` checks slices against it, the build reads it as rules.
  Its **En local** says how each part is tried without going online, so the
  loop never deploys; **À faire à la main** is the person's checklist, which
  `executer` asks for all at once and checks before the first slice.
- **Questions go to a file, not back into the run.** A builder or an audit that
  meets a choice only the person can make builds its pick, writes it under
  **Choisi :** and adds an entry to `a-trancher.md`; `executer` asks the open
  entries at the end, and an answer that changes the build goes through
  `repartir`, never into a fix pass. Only money, a missing account or secret,
  or something that cannot be undone still stops a builder.
- **One audit agent per slice in the loop.** It does the spec check itself
  instead of briefing a sub-agent, runs the checks once, and adds the
  architecture to what it checks (a part in the wrong place, something online,
  a secret's value in a tracked file). The code check runs once per run over
  the whole diff, into `audits/code.md`. A second pass reads only the fix list
  and the fix diff, re-running what the fixer said it ran. A typed
  `/cadrer:reviser` keeps both axis sub-agents.

Measured the same day, headless, on one two-slice fixture (a to-do command
plus a daily send to a webhook, its address a secret in `.env.local`, a local
stand-in for the webhook, and one question the spec left open), run once with
0.4.0 and once with 0.5.0. Weighted tokens from the session files:

| | 0.4.0 | 0.5.0 |
| --- | --- | --- |
| First audit, slice 01 · 02 | 109k · 185k (1.7× its build) | 67k · 96k (0.5–0.7×) |
| Second pass | 172k | 62k · 81k |
| Code check | in every audit | 55k, once |
| All auditing, share of run | 56% | 35% |
| Outcome | 01 *fusionner*; 02 *retour à la tranche* after a fix | both *fusionner* after one fix each |

0.5.0 cost more in total (1.03M against 0.83M; $7.22 against $5.85 reported)
because it did two fix cycles and finished, where 0.4.0 stopped after one. Both
fixes fixed a crash, not an answer. The builders stopped for nothing, wrote two
`a-trancher.md` entries, asked at the end, and nothing went online. One run
each, so read the shares, not the totals.

## Done 2026-09-13 — `cadrer` 0.6.0: `livrer`

The loop never deploys, so something has to. `/cadrer:livrer` runs in the main
window with the person there, because this is where accounts, cards and real
messages come in. In order: it checks every slice is *fusionner* and every
a-trancher answer is placed, and re-runs each **Pour lancer** without touching
the person's data; it asks the *avant la livraison* chores, has the person type
every secret themselves (on the provider's page or in their own terminal, never
with `! `, which puts it in the conversation), and checks each without
showing a value — by name, or as "no longer the local stand-in"; it shows a
table of each action, what it creates or sends out there, the cost and the
undo, and waits for a yes (money gets its own); it goes online, follows the
architecture's **Trajet** on the real address, asks the person to look at what
only they can see, and writes `livraison.md`. Something broken online goes
under **Reste à faire** for `repartir`, never into a fix here.

Tested the same day, before writing it, in two runs with Claude playing a
non-developer through messages:

- **`affiner` on a made-up project** — a yoga teacher's class bookings, online
  with the computer off, e-mails, a web address in the teacher's name. 25 questions:
  18 on what gets built (an answer without a reason was asked why), the day
  told and corrected once, reasons confirmed before writing, then three named setups with prices looked up that day,
  the path of one booking through the parts, and the renewal of the paid
  address. `architecture.md` came out with the eight headings, secrets by name
  only, and twelve chores split two *avant la construction*, ten *avant la
  livraison*. One flaw: while writing, it found a fact the person had approved
  was wrong (who forwards replies once the address points elsewhere) and wrote
  the fix as *Supposé* instead of asking. `affiner` now asks first.
- **`livrer` on the 0.5.0 fixture**, dry: nothing was allowed to leave the
  computer, and the person said "done" without doing the chore. It caught the
  address still being the local stand-in without printing it, accepted the
  real-looking one, showed a three-row plan with the one real message as the
  last row, and on "not today" stopped with nothing written. Two fixes came
  from it: re-running **Pour lancer** created and deleted the person's data
  file, and a tick left uncommitted would fail the next run's clean-tree
  check. Still unseen: a real deploy, a paid row, the check online, and
  `livraison.md` itself.

Codex reviewed PRs #4 and #5 twice on 2026-09-14; all thirteen findings were
fixed. `executer` now stops without `architecture.md`, commits its ticked
chores, names the folder to the code review and runs it whenever a slice was
built, resolves a merge whose only conflict is `a-trancher.md` by keeping both
entries, and stops on a secret committed by a build — the person changes it
where it was issued, and the branch is not pushed until the commit leaves
history. `livrer` keeps secrets out of `! `, gives a paid chore its own yes,
commits an answer it collects, runs the online check once, and, when a row
fails, writes and commits `livraison.md` with what went out, so the next run
redoes only what is not still there. Chores left open go under **Reste à
faire** marked *à la main*, which `repartir` leaves to the person.

## Still to do

1. **Run the loop end to end** — 0.4.0 was run headless (`claude -p`) on a
   two-slice project: the sequential loop, nested axis sub-agents, a typed
   `/cadrer:reviser` followed by a resumed `executer`, and `parallele` with two
   worktrees merged back. Still unseen: that `background: false` makes a typed
   `/cadrer:reviser` wait in an interactive window, the AskUserQuestion hand-off
   of a returned question, and a *corriger d'abord* fix pass.
   Then in a throwaway project, `/cadrer:choisir` through
   `/cadrer:livrer` on a real free host, first with
   `claude --plugin-dir plugins/cadrer`, then
   through the real install line. Before the course pass, so the lessons copy
   what was seen.
2. **The course pass.** Lessons 4.2 to 4.8 and the platform exports still say
   `/workflow:ideate` and `claude plugin install workflow@workflow-skills`.
   Replace the commands (`/cadrer:choisir`…), the install line
   (`cadrer@cadrer`), `claude plugin details workflow`, and add the box above
   to 4.2. The "Did it work?" file checks change too: `idee.md`, `tranches.md`,
   and the headings and markers in the table above (`Fait quand`, not
   `Done when`). An English export, if one stays, points at the same plugin.
3. **The hub.** The course's rule says `~/Desktop/skill-hub/skills` is the
   source of truth and this repo holds copies. That is no longer how it works:
   `plugins/cadrer/skills/` here is the source, and the course copy in
   `~/Desktop/ai-coding-course/skills/` should be a copy of it (or a pointer).
   Update that rule in the course's `CLAUDE.md` with the course pass, and retire
   or re-point the hub.
