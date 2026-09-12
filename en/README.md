# cadrer-en

The English render of **CADRER**, the six-step build loop taught in the free course **Première
Livraison**. Same plugin, same six commands as `Karnonson/cadrer`; the difference is the language of
what the skills write and show: `builds/<NN>-<slug>/idea.md`, `slices.md`, English headings, English
hints in the `/` menu.

```
claude plugin marketplace add Karnonson/cadrer-en
claude plugin install cadrer@cadrer-en --scope project
```

Then `/cadrer:ideate`, `/cadrer:refine`, `/cadrer:spec`, `/cadrer:slice`, `/cadrer:implement`,
`/cadrer:audit`. Install one language per project; the French render is `cadrer@cadrer`.

This repo is generated. The source is `src/` in https://github.com/Karnonson/cadrer, rendered by
`tools/render.py` and pushed here by `deploy-en.sh`. Do not edit here.
