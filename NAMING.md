# Naming — CADRER

Names decided 2026-09-10. Built in this repo on 2026-09-12 as plugin `cadrer`
0.3.0: two plugins rendered from one source, `cadrer` with French commands and
files and `cadrer-en` with English ones, picked at install. This file records
what the names are, what was tried and
dropped on the way, and what still has to happen, in what order.

## The two names

| Level | Name | What it is |
| --- | --- | --- |
| Offer | **Première Livraison** | The free course this loop is taught in — 6 sections, 47 lessons, idea to a link you can send |
| Method | **CADRER** | This loop. The French verb *cadrer* — to keep something in frame — and the six steps spell it |

`CADRER` is an acronym, written in caps when it names the method. The plain verb
`cadrer` stays lowercase and free. It names the marketplace, the French plugin
(`cadrer-en` for the English one) and, once renamed, the GitHub repo. It is the
one name for both languages: methods keep their birth name when they cross a border
(Kanban, Kaizen, Scrum), and the English lesson gets one sentence saying where
the word comes from.

| Letter | Step | French command | English command | Writes (FR) | Writes (EN) |
| --- | --- | --- | --- | --- | --- |
| **C** | Choisir | `/cadrer:choisir` | `/cadrer-en:ideate` | `idee.md` | `idea.md` |
| **A** | Affiner | `/cadrer:affiner` | `/cadrer-en:refine` | `decisions.md` | `decisions.md` |
| **D** | Détailler | `/cadrer:detailler` | `/cadrer-en:spec` | `spec.md` | `spec.md` |
| **R** | Répartir | `/cadrer:repartir` | `/cadrer-en:slice` | `tranches.md` | `slices.md` |
| **E** | Exécuter | `/cadrer:executer` | `/cadrer-en:implement` | the code, plus ticks under the slice | same |
| **R** | Réviser | `/cadrer:reviser` | `/cadrer-en:audit` | `audits/<NN>.md` | `audits/<NN>.md` |

Typing the six French commands spells the method. Step 1 is **choisir**, not
*cadrer* — otherwise the word names both the loop and its first step. The
English plugin keeps the English step names, and its menu descriptions open
with the French one (*Choisir — ideate*) so the acronym still reads.

## Why deploying and monitoring never join the acronym

They are not steps of this loop. CADRER is re-run per idea and per slice; going
live happens once, when a loop closes, and monitoring never stops. A continuous
activity inside a numbered sequence misdescribes the mechanism.

The split already exists in the course: section 05 puts the app online and is a
lesson, not a skill, and architecture, secrets, tests and monitoring are already
Part 2 material. Part 2 gets its own name — **TENIR**, proposed, not locked —
covering real deployment, architecture, secrets, tests, monitoring.

**The rule:** an acronym is a counting contract. If a seventh skill ever truly
belongs to the build loop, it goes inside one of the six letters or out into the
outer ring. CADRER is never renamed to make room.

## Done 2026-09-12 — `cadrer` 0.3.0: one source, two plugins

What the learner picks, and where:

- **The language, at install.** `cadrer@cadrer` writes and shows French,
  `cadrer-en@cadrer` English. Same bodies, same version, one marketplace. Not
  a runtime setting: Claude Code has no install-time prompt, so the choice is
  the install line, and the two course exports each give their own.
- **Why the English plugin has its own name.** Claude Code keys plugins by
  name inside a marketplace and uses the plugin name as the command prefix.
  Two plugins named `cadrer` cannot share a marketplace, so the English one is
  `cadrer-en` and its commands are `/cadrer-en:ideate`. The alternative — one
  plugin holding all twelve skills — would show both languages in every menu
  and load both sets of descriptions on every run, for everyone.

What differs between the renders — the whole vocabulary, from `src/vocab/`:

| Where | French | English |
| --- | --- | --- |
| Plugin, commands | `cadrer`: `choisir`, `affiner`, `detailler`, `repartir`, `executer`, `reviser` | `cadrer-en`: `ideate`, `refine`, `spec`, `slice`, `implement`, `audit` |
| `/` menu: description | *Trouver l'idée. À utiliser quand…* | *Choisir — ideate. Use when…* |
| `/` menu: argument hint | `[numéro ou nom du dossier]`, `[dossier] [tranche]` | `[build number or name]`, `[build] [slice]` |
| Files | `idee.md`, `tranches.md` | `idea.md`, `slices.md` |
| `idee.md` headings | Le problème · En une phrase · Pourquoi celle-ci · Écartées · Pas encore · Encore ouvert · Jusqu'où on est allé | The problem · The one sentence · Why this one · Ruled out · Not yet · Still open · How far I took it |
| `decisions.md` headings | Décidé · Supposé · Abandonné | Settled · Assumed · Dropped |
| `spec.md` headings | Problème · Solution · Apparence · User stories · Décisions de réalisation · Décisions de test · Hors périmètre · Ouvert | Problem · Solution · Look · User stories · Implementation decisions · Testing decisions · Out of scope · Open |
| Story form | En tant que <qui>, je veux <quoi>, afin de <bénéfice> | As <who>, I want <thing>, so that <benefit> |
| Slice markers | À construire · Bloqué par · Fait quand · Non placé · Choisi · Pour lancer · Fichiers · Audit · Corrigé | What to build · Blocked by · Done when · Unplaced · Chosen · How to run · Files · Audit · Fixed |
| Audit headings | Deuxième passe · Rectifié · Plus tard | Second pass · Corrected · Later |
| Verdicts | fusionner · corriger d'abord · retour à la tranche | merge · fix first · back to slice |
| Worktree branch | `tranche-<NN>` | `slice-<NN>` |
| Language line | …in French | …in English |

`builds/`, `prototypes/`, `audits/`, `spec.md`, `decisions.md` and the words
*Spec*, *Code*, *Verdict* are the same in both. `User stories` stays English in
French because the course already says it that way. The French colon takes its
space (`**Fait quand :**`) through a `{{colon}}` placeholder.

The language line at the end of each opening paragraph now names the language
of the render — *Answer, and write the files' contents, in French; file names
and headings stay as written here* — instead of following the person. The
vocabulary fixes the headings, so the later skills and the lessons' file checks
can read them by string; the one line makes the prose match.

Bodies are English in both renders. Measured the same day with
`tools/token_estimate.py` (o200k): the French render costs 1.05× the English
one when a skill runs, 1.31× for the always-loaded descriptions; a fully
translated body cost 1.27–1.41×.

## Dropped 2026-09-12 — a second repo

For an hour both plugins were named `cadrer`, with English commands in both,
and the English one lived in a generated `cadrer-en` repo so that both could
type `/cadrer:ideate`. Dropped the same day: two repos to keep in step for one
prefix, and the French commands are the method — a French learner types
`choisir`, not `ideate`. One marketplace, two plugin names instead.

## Dropped 2026-09-12 — the French twin

A hand-translated French body for each skill. Dropped because the learner never
reads the skill, because French bodies cost about a quarter more on every run,
and because two hand-kept sets drift. What the twin was for — French questions,
French files — is now the French render: same English body, French vocabulary.

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
>    des titres en français. La compétence dit à Claude dans quelle langue te
>    répondre et écrire ; c'est la version que tu as installée qui le fixe.
> 3. **Une seule version à entretenir.** Les six compétences existent en
>    français et en anglais, mais à partir d'une seule source : ce qui change
>    d'une langue à l'autre, c'est le vocabulaire — les noms de fichiers, les
>    titres, les verdicts — pas la consigne.

## Still to do

1. **The course pass.** Lessons 4.2 to 4.8 and both platform exports still say
   `/workflow:ideate` and `claude plugin install workflow@workflow-skills`.
   Replace the commands (French export: `/cadrer:choisir`…; English export:
   `/cadrer-en:ideate`…), the install lines (`cadrer@cadrer`, `cadrer-en@cadrer`),
   `claude plugin details workflow`, and add the box above to 4.2. The "Did it work?" file checks change in the French
   export: `idee.md`, `tranches.md`, and the headings and markers in the table
   above (`Fait quand`, not `Done when`).
2. **Rename the GitHub repo** `workflow-skills` → `cadrer` (`gh repo rename
   cadrer`; GitHub redirects the old address). The README's install line already
   says `Karnonson/cadrer`.
3. **Push.** The rename is committed, not pushed. Pushing is what makes
   `cadrer@cadrer` installable and makes the old `workflow@workflow-skills` stop
   resolving for new installs; do it together with the course pass, or just
   before.
4. **The hub.** The course's rule says `~/Desktop/skill-hub/skills` is the
   source of truth and this repo holds copies. That is no longer how it works:
   `src/` here is the source, both renders are generated from it, and the
   course copy in `~/Desktop/ai-coding-course/skills/` should be one of the
   renders (or a pointer). Update that rule in the course's `CLAUDE.md` with
   the course pass, and retire or re-point the hub.
