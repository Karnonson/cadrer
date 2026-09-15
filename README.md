# cadrer

**Français** · [English](README.en.md)

**CADRER** est la boucle de construction en six étapes enseignée dans le cours gratuit **Première
Livraison**. Ce dépôt est sa marketplace Claude Code, avec la boucle en un seul plugin, `cadrer` : six
commandes en français, des noms de fichiers et des titres en français, et Claude qui répond et écrit
dans la langue dans laquelle vous lui écrivez.

| Étape | Commande | Écrit |
| --- | --- | --- |
| **C**hoisir | `/cadrer:choisir` | `idee.md` |
| **A**ffiner | `/cadrer:affiner` | `decisions.md`, `architecture.md` |
| **D**étailler | `/cadrer:detailler` | `spec.md` |
| **R**épartir | `/cadrer:repartir` | `tranches.md` |
| **E**xécuter | `/cadrer:executer` | le code, les cases cochées sous chaque tranche, un audit par tranche via réviser, `a-trancher.md` |
| **R**éviser | `/cadrer:reviser` | `audits/<NN>.md` |
| — Livrer | `/cadrer:livrer` | le projet en ligne, `livraison.md` |

Les six écrivent dans un dossier par idée, `builds/<NN>-<slug>/`, et chacune lit ce que la précédente a
laissé. `affiner` tranche ce qu'on construit, puis où ça tourne, ce que ça coûte et ce que la personne
prépare à la main, dans `architecture.md`. `/cadrer:executer` vérifie que ces tâches sont faites, puis
enchaîne seul le reste, sur l'ordinateur, jamais en ligne : chaque tranche ouverte est construite par un
sous-agent, auditée par un autre qui suit `reviser`, corrigée puis auditée à nouveau si l'audit trouve un
défaut, puis la suivante. Un choix que seule la personne peut faire ne l'arrête pas : la construction
prend son option et écrit la question dans `a-trancher.md`, posée à la fin. Une seule revue du code
couvre tout le passage, dans `audits/code.md`. `/cadrer:executer <dossier> <NN>` fait une seule
tranche ; `parallele` construit les tranches ouvertes en même temps, un worktree git chacune, fusionné
une fois audité. Un passage complet consomme des tokens sur chaque tranche, deux à quatre sous-agents
chacune. `/cadrer:reviser` tourne encore seul, dans son propre sous-agent avec ses deux relecteurs, sur
une tranche construite à la main.

La mise en ligne, c'est `/cadrer:livrer`, une commande en dehors des six lettres, lancée avec la
personne au clavier une fois chaque tranche auditée *fusionner*. Elle demande les tâches *avant la
livraison* — les secrets sont tapés par la personne et jamais affichés —, puis montre un tableau de ce
qu'elle va créer, payer ou envoyer et comment annuler chaque action, et attend un oui. Elle met ensuite
le projet là où `architecture.md` le dit, refait le **Trajet** de l'architecture sur la vraie adresse, et
écrit `livraison.md` : l'adresse, comment recommencer, ce qui a été vu en ligne, comment revenir en
arrière, et ce qui reste pour `repartir`.

Les noms de commandes n'ont pas d'accents — un nom de compétence ne contient que des minuscules, des
chiffres et des tirets — donc on tape `detailler`, `repartir`, `executer`, `reviser`.

## Installer

Dans un terminal, placé dans le projet où vous voulez la boucle :

```
claude plugin marketplace add Karnonson/cadrer
claude plugin install cadrer@cadrer --scope project
```

`--scope project` active le plugin pour ce dossier seulement (il écrit `.claude/settings.json` dans ce
dossier) ; sans cette option, il s'active pour tous les projets de votre machine. Ensuite
`/cadrer:choisir` et les autres répondent par leur nom dans toute fenêtre Claude Code ouverte dans ce
dossier. `claude plugin details cadrer` montre ce qu'il vous coûte par session ; `claude plugin
uninstall cadrer --scope project` le retire.

Avant la 0.3.0, le plugin s'appelait `workflow` (`/workflow:ideate`, depuis la marketplace
`workflow-skills`). Désinstallez-le et installez `cadrer`. Les dossiers de construction commencés avec
`workflow` utilisent les noms de fichiers anglais (`idea.md`, `slices.md`) : commencez les nouveaux avec
`cadrer`.

## Langues

Trois couches, trois lecteurs :

- **Ce que voit l'apprenant est en français.** Les commandes, les descriptions et les indications
  d'arguments du menu `/`, les noms de fichiers, les titres dans chaque fichier, les repères que les
  étapes suivantes cherchent (`Fait quand`, `Bloqué par`…) et les verdicts (`fusionner`, `corriger
  d'abord`, `retour à la tranche`). Ils sont fixes : la compétence suivante et les vérifications de
  fichiers du cours les lisent mot pour mot.
- **Ce qu'écrit Claude suit la personne.** Chaque compétence dit : répondre, et écrire le contenu des
  fichiers, dans la langue de la personne ; les noms de fichiers et les titres restent tels qu'écrits.
  Un apprenant qui écrit en français obtient du français. Pour le fixer dans toutes les fenêtres,
  mettez `"language": "French"` dans `~/.claude/settings.json`, ou choisissez-le dans `/config`.
- **Ce que seul Claude lit est en anglais.** Le corps des compétences. Une compétence est lue par
  l'agent, jamais par l'apprenant, et le français coûte plus de tokens pour la même instruction.

Mesuré avec `tools/token_estimate.py` le 2026-09-12, tokenizer o200k, contre une version des mêmes
corps avec le vocabulaire en anglais (commit `f9eb4f1`) :

| | Vocabulaire anglais | `cadrer` |
| --- | --- | --- |
| Six compétences, chargées quand l'une tourne | 4 448 | 4 657 (1,05×) |
| Six descriptions, toujours chargées | 318 | 416 (1,31×) |

Un corps entièrement traduit en français donnait 1,27–1,41× à la place.

Les compétences sous `plugins/cadrer/skills/` sont la source. Modifiez-les à la main ; `claude plugin
validate plugins/cadrer` vérifie le manifeste.

## Outils

`tools/token_estimate.py` compte ce qu'un ensemble de compétences coûte en tokens, et peut comparer
deux ensembles (appariés par les slugs CADRER, ou `--map EN=FR`). Le tokenizer de Claude n'est pas
public, donc il compte avec des tokenizers publics — celui d'OpenAI, Llama 3, Qwen 3, DeepSeek V3,
Mistral Nemo, Gemma 3 — et donne le ratio FR/EN sur l'ensemble ; avec `ANTHROPIC_API_KEY` défini, il
ajoute le compte exact de Claude via `count_tokens`.

```
uv run tools/token_estimate.py plugins/cadrer/skills              # un ensemble
uv run tools/token_estimate.py path/to/en/skills plugins/cadrer/skills   # EN contre FR
```

`--detail o200k` détaille par compétence, `--json` affiche les chiffres. La page publique pour les
lecteurs non techniques, *Le prix du français*, vit dans son propre dépôt, `~/Desktop/prix-du-francais`.

## Crédits

`affiner` est adapté de `grilling` de Matt Pocock (MIT) — github.com/mattpocock/skills.
