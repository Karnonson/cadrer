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
| **A** | Affiner | `/cadrer:affiner` | `decisions.md` |
| **D** | Détailler | `/cadrer:detailler` | `spec.md` |
| **R** | Répartir | `/cadrer:repartir` | `tranches.md` |
| **E** | Exécuter | `/cadrer:executer` | the code, plus ticks under the slice |
| **R** | Réviser | `/cadrer:reviser` | `audits/<NN>.md` |

Typing the six commands spells the method. Step 1 is **choisir**, not
*cadrer* — otherwise the word names both the loop and its first step.

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
| Files | `idee.md`, `decisions.md`, `spec.md`, `tranches.md`, `audits/<NN>.md` |
| `idee.md` headings | Le problème · En une phrase · Pourquoi celle-ci · Écartées · Pas encore · Encore ouvert · Jusqu'où on est allé |
| `decisions.md` headings | Décidé · Supposé · Abandonné |
| `spec.md` headings | Problème · Solution · Apparence · User stories · Décisions de réalisation · Décisions de test · Hors périmètre · Ouvert |
| Story form | En tant que <qui>, je veux <quoi>, afin de <bénéfice> |
| Slice markers | À construire · Bloqué par · Fait quand · Non placé · Choisi · Pour lancer · Fichiers · Audit · Corrigé |
| Audit headings | Deuxième passe · Rectifié · Plus tard |
| Verdicts | fusionner · corriger d'abord · retour à la tranche |
| Worktree branch | `tranche-<NN>` |

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

## Still to do

1. **Run the loop end to end** in a throwaway project, `/cadrer:choisir` through
   `/cadrer:reviser`, first with `claude --plugin-dir plugins/cadrer`, then
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
