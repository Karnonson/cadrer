# Naming — CADRER

Decided 2026-09-10. Nothing in this repo has been renamed yet; this file records
what the names are and what has to happen, in what order.

## The two names

| Level | Name | What it is |
| --- | --- | --- |
| Offer | **Première Livraison** | The free course this loop is taught in — 6 sections, 47 lessons, idea to a link you can send |
| Method | **CADRER** | This loop. The French verb *cadrer* — to keep something in frame — and the six steps spell it |

`CADRER` is an acronym, written in caps when it names the method. The plain verb
`cadrer` stays lowercase and free.

| Letter | Step (FR) | Skill today | Writes |
| --- | --- | --- | --- |
| **C** | Choisir | `ideate` | `idea.md` |
| **A** | Affiner | `refine` | `decisions.md` |
| **D** | Détailler | `spec` | `spec.md` |
| **R** | Répartir | `slice` | `slices.md` |
| **E** | Exécuter | `implement` | the code, plus ticks under the slice |
| **R** | Réviser | `audit` | `audits/<NN>.md` |

Step 1 is **choisir**, not *cadrer* — otherwise the word names both the loop and
its first step.

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

## Pending — rename `workflow` → `cadrer`

Not done. Today a learner types `/workflow:slice` while the method says
*Répartir*. Renaming the plugin puts the brand name in the terminal in every
lesson of section 04.

Order of operations, decided: **plugin first, course second.** The course stays
exactly as it is — lessons 4.2 to 4.8, the `/workflow:` command names, the
install commands — until this repo ships the new name. Then the lessons and the
platform export follow in one pass.

## Planned — a French twin plugin

Two plugins in this one marketplace, same loop, different language:

| Plugin | Audience | Skill names | Bodies and descriptions |
| --- | --- | --- | --- |
| `workflow` (or `cadrer`, after the rename) | internal — Zana's own projects | `ideate`, `refine`, `spec`, `slice`, `implement`, `audit` | English |
| `cadrer-fr` | the course's French learners | `choisir`, `affiner`, `detailler`, `repartir`, `executer`, `reviser` | French, `tu` register |

The point of the French set is not the command names — it is that a skill body
in French makes the agent ask its questions and write its files in French. That
is what the learner gets. The command names are the bonus: typing them spells
the method.

Invariants for the twin, so the two sets stay interchangeable:

- **Identical output.** Same file names, same folder layout — `builds/<NN>-<slug>/idea.md`,
  `decisions.md`, `spec.md`, `slices.md`, `audits/<NN>.md`. Only the prose inside
  is translated. A build folder made with one set must be readable by the other,
  and the course's terminal commands (`cat builds/*/idea.md`) must work either way.
- **Same source-of-truth rule.** `~/Desktop/skill-hub/skills` stays the source
  for English. French lives beside it in the hub and is copied out the same way —
  never edited in this repo.
- **Versions in lockstep.** A change to a step ships in both plugins under the
  same version number, or neither.
- **Slugs carry no accents** (`detailler`, `repartir`, `executer`, `reviser`) —
  skill names are lowercase letters, digits and hyphens. The accented spelling
  lives in the description and the body.

Open questions, to settle when the twin is built:

1. Install both at once? Six skills cost roughly 460 tokens of always-loaded
   context; two sets double it for no gain. Assume one set per project.
2. Which set do the French lessons quote? The French course should quote the
   French skills — that is the second half of the rename pass.
3. How the French stays in sync when an English skill is revised. The course hub
   already has translation tooling; the same discipline applies here, by hand,
   checked, in `tu`.
