#!/usr/bin/env bash
# Ping IndexNow. Usage: ./indexnow.sh URL [URL...]   (no args = every URL in the live sitemap)
# Reads SITE_URL and INDEXNOW_KEY from _build.py so a domain switch needs no edit here.
cd "$(dirname "$0")"
SITE=$(python3 -c 'import re;print(re.search(r"^SITE_URL = \"([^\"]+)",open("_build.py").read(),re.M).group(1))')
KEY=$(python3 -c 'import re;print(re.search(r"^INDEXNOW_KEY = \"([^\"]+)",open("_build.py").read(),re.M).group(1))')
HOST=$(python3 -c "from urllib.parse import urlparse;print(urlparse('$SITE').netloc)")
if [ $# -eq 0 ]; then set -- $(curl -s "${SITE}sitemap.xml" | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /tmp/indexnow.out -w "IndexNow HTTP %{http_code} ($# URLs)\n" -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"${SITE}${KEY}.txt\",\"urlList\":$LIST}"
cat /tmp/indexnow.out; echo
