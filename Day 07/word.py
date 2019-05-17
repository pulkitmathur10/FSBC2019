# -*- coding: utf-8 -*-

import requests
import json
word_id = "example"
url = "https://oed-api.oxforddictionaries.com/oed/api/v2/thesaurus/EN-GB/ace"
r = requests.get(url, headers={
  "Accept": "application/json",
  "app_id": "0540d14a",
  "app_key": "74f9ac0988caef1b994fd001aab1635a"
})

print(r.content)