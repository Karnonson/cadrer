#!/usr/bin/env sh
# en/ is the English render of the plugin (python3 tools/render.py): a whole marketplace, named
# cadrer-en, so that both languages install the same plugin name and the same commands. This
# force-pushes en/ as the main branch of the cadrer-en repo. Run it after committing here.
set -eu
cd "$(dirname "$0")"
python3 tools/render.py --check >/dev/null
remote=${EN_REMOTE:-git@github.com:Karnonson/cadrer-en.git}
source=$(git rev-parse --short HEAD)
tmp=$(mktemp -d)
cp -R en/. "$tmp"
cd "$tmp"
git init -q -b main
git add -A
git commit -q -m "Render of Karnonson/cadrer $source"
git push -q -f "$remote" main
cd - >/dev/null
rm -rf "$tmp"
echo "pushed cadrer-en main from $source"
