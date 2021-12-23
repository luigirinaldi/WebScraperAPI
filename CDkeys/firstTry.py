import requests
from requests.api import head
import json
import pprint

from requests.models import Response

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.4664.110 Safari/537.36',
    "sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "accept":"application/json",
    'content-type':'application/x-www-form-urlencoded',
    "Origin":"https://www.cdkeys.com",
    "Sec-Fetch-Site":"cross-site",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://www.cdkeys.com/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en,en-US;q=0.9,it;q=0.8",
}


url = "https://muvyib7tey-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20instantsearch.js%20(4.7.2)%3B%20Magento2%20integration%20(3.0.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-application-id=MUVYIB7TEY&x-algolia-api-key=ODNjY2VjZjExZGE2NTg3ZDkyMGQ4MjljYzYwM2U0NmRjYWI4MDgwNTQ0NjgzNmE2ZGQyY2ZmMDlkMzAyYTI4NXRhZ0ZpbHRlcnM9"

payload = json.dumps({"requests":[
    {
        "indexName":"magento2_default_products","params":"highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page=0&ruleContexts=%5B%22magento_filters%22%5D&hitsPerPage=24&clickAnalytics=true&query=restaru&maxValuesPerFacet=10&facets=%5B%22restricted_countries%22%2C%22platforms%22%2C%22region%22%2C%22language%22%2C%22genres%22%2C%22price.EUR.default%22%5D&tagFilters=&facetFilters=%5B%22restricted_countries%3A-IT%22%5D&numericFilters=%5B%22visibility_search%3D1%22%5D"}
        ]
})

r = requests.post(url=url,data=payload,headers=headers)

with open('response.json','w') as f:
    json.dump(r.json(),f)