# Naming — CADRER

Names decided 2026-09-10; the rename shipped in this repo on 2026-09-12 as plugin
`cadrer` 0.3.0, and the French twin was dropped the same day (see the end of this
file). This file records what the names are and what still has to happen, in
what order.

## The two names

| Level | Name | What it is |
| --- | --- | --- |
| Offer | **Première Livraison** | The free course this loop is taught in — 6 sections, 47 lessons, idea to a link you can send |
| Method | **CADRER** | This loop. The French verb *cadrer* — to keep something in frame — and the six steps spell it |

`CADRER` is an acronym, written in caps when it names the method. The plain verb
`cadrer` stays lowercase and free.

| Letter | Step (FR) | Skill since 0.3.0 | Skill before | Writes |
| --- | --- | --- | --- | --- |
| **C** | Choisir | `choisir` | `ideate` | `idea.md` |
| **A** | Affiner | `affiner` | `refine` | `decisions.md` |
| **D** | Détailler | `detailler` | `spec` | `spec.md` |
| **R** | Répartir | `repartir` | `slice` | `slices.md` |
| **E** | Exécuter | `executer` | `implement` | the code, plus ticks under the slice |
| **R** | Réviser | `reviser` | `audit` | `audits/<NN>.md` |

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

## Done 2026-09-12 — rename `workflow` → `cadrer` (plugin 0.3.0)

What changed in this repo:

- `plugins/workflow/` → `plugins/cadrer/`; the six skill folders take the step
  names without accents (table above). `plugin.json` and `marketplace.json`
  follow; version 0.3.0, since every command name changes.
- Each skill's front matter: `name:` is the new slug; the description opens with
  the accented step name and the old English name — `Choisir — ideate.` — so the
  agent and Zana both know which is which.
- The three places a skill named another skill by its English name now use the
  new slug: `detailler` ("if the affiner step left it"), `executer` ("run the
  reviser skill in a new window"), `reviser` (description, and "fixes go to the
  executer skill"). The rule from the course hub stands: name the skill, never
  the command.
- One line added at the end of each skill's opening paragraph: *Answer, and
  write the files' contents, in the language the person writes in; file names
  stay as written here.* This is what makes an English skill serve a French
  learner (next section). The prose and headings follow the learner; the paths
  (`idea.md`, `slices.md`…) never do, because the next skill and the lessons'
  file checks read them by name. Not a setting: the language the person writes
  in *is* the setting, and a project that wants otherwise says so once in its
  `CLAUDE.md`, which the agent reads alongside the skill.

Order of operations was **plugin first, course second**, and the second half is
still open — see *Still to do*.

## Dropped 2026-09-12 — the French twin

There is no `cadrer-fr`. One plugin, French names, English bodies, and the
language line above. Why:

- **The learner never reads the skill.** A skill body is a standing instruction
  to the agent, loaded on every run. Translating it changes nothing the learner
  sees, except the bill.
- **French costs about a quarter more.** Measured 2026-09-12 with
  `tools/token_estimate.py` on the six skills against a working French draft:
  FR/EN between 1.27 and 1.41 across eight public tokenizers, ~1.27 on the
  large-vocabulary ones current models use. Always-loaded descriptions cost a
  little more still. Paid on every run, by every learner.
- **What the twin was for is one line.** The point was that the agent asks its
  questions and writes its files in French. The language line does that from an
  English body, and it follows the learner rather than the plugin: someone
  writing in English gets English files from the same install.
- **One set to maintain.** Two sets meant lockstep versions and a hand-checked
  translation on every revision, for a plugin one person keeps.

What the learner does get in French: the plugin name, the six commands (typing
them spells the method), the questions the agent asks, and every file in
`builds/`. Both audiences install the same thing.

One thing to watch: the build files are written in the learner's language, so
the markers the later skills look for — **Done when**, **Audit:**, *merge*,
*fix first*, *back to slice* — will be in French in a French learner's project.
The agent reads them by meaning, not by string, and a project stays in one
language, so this is expected to hold; the course walk will confirm it.

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
> 2. **Claude te répond en français quand même.** Chaque compétence lui demande
>    de parler, et d'écrire tes fichiers, dans la langue où tu lui écris. Tu
>    tapes `/cadrer:choisir`, tu expliques ton problème en français, et
>    `idea.md` sort en français.
> 3. **Une seule version à entretenir.** Deux versions, c'est deux fois plus
>    d'occasions qu'elles se contredisent. Ce qui est en français, c'est ce que
>    tu tapes : les six commandes épellent la méthode.

## Still to do

1. **Copy the edits back to the hub.** `~/Desktop/skill-hub/skills` is the
   source of truth and was not reachable from the machine that did the rename;
   the six bodies here now differ from it by the front-matter `name:`, the
   description prefix, the three cross-references and the language line. Apply
   the same edits there (and decide whether the hub folders take the new names),
   then the release check `diff -r -x example.md ~/Desktop/skill-hub/skills
   plugins/cadrer/skills` is clean again. The course copy in
   `~/Desktop/ai-coding-course/skills/` follows with the course pass.
2. **The course pass.** Lessons 4.2 to 4.8 and both platform exports still say
   `/workflow:ideate` and `claude plugin install workflow@workflow-skills`.
   Replace command names, install lines, `claude plugin details workflow`, and
   add the box above to 4.2. The "Did it work?" file checks still hold: same
   paths, same headings — in the learner's language.
3. **Push.** The rename is committed, not pushed. Pushing is what makes
   `cadrer@workflow-skills` installable and makes the old `workflow@workflow-skills`
   stop resolving for new installs; do it together with the course pass, or
   just before.
4. **Open: the marketplace name.** `cadrer@workflow-skills` still carries the
   old word. Renaming the GitHub repo (GitHub redirects the old name) and the
   `name` in `marketplace.json` to `cadrer` would give `cadrer@cadrer`. Not done:
   it changes the install line learners were given, so it belongs in the same
   course pass if it happens at all.
