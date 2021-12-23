import requests
from requests.api import head
import json
import pprint

from requests.models import Response

def findPrice(inputStr):
    #price sample: 
    #   class="a-price" data-a-size="m" data-a-color="price"><span class="a-offscreen">8,20 €</s
    #assuming price is between class="a-price a-text-price and €
    #then assume it is between € and >
    pricePos = r.text.find('class="a-price a-text-price')
    pricePos1 = r.text.find('€',pricePos)
    pricePos2 = r.text.rfind('>',pricePos,pricePos1) + 1  #search leftwards from € 
    
    final = r.text[pricePos2:pricePos1].replace(',','.')
    return float(final)


# class="a-price a-text-price a-size-medium apexPriceToPay"

headers = {
    "authority":"www.amazon.it",
    "scheme":"https",
    "path":"/Silverline-546524-Set-cacciaviti-colore/dp/B003TO2JD0/ref=sr_1_9?keywords=cacciavite&qid=1640281294&sr=8-9",
    "cache-control":"max-age=0",
    "rtt":"50",
    "downlink":"10",
    "ect":"4g",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"'Windows'",
    "upgrade-insecure-requests":"1",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"en,en-US;q=0.9,it;q=0.8",
}


url = "https://www.amazon.it/dp/B01J84AMZ6/ref=s9_acsd_ri_bw_c2_ALTICOL_8_i?pf_rd_m=A2VX19DFO3KCLO&pf_rd_s=merchandised-search-7&pf_rd_r=QN7P20MJE1YEVP2BYHY5&pf_rd_t=101&pf_rd_p=c1058088-23f6-4c4f-a75a-20fb47f45f87&pf_rd_i=26215470031&th=1"

r = requests.get(url=url,headers=headers)

print(f"{findPrice(r.text)}€")

with open('response.txt','w',encoding="utf-8") as f:
    f.write(r.text)