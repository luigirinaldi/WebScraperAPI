import requests
import json
import pprint
from bs4 import BeautifulSoup

def getResponseURL(url):
    headers = {
        "authority":"www.amazon.it",
        "scheme":"https",
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
    try:
        return requests.get(url=url,headers=headers)
    except:
        return -1

def getItemResponse(itemId):
    url = f"https://amazon.it/dp/{itemId}"
    return getResponseURL(url)

def findPriceIT(inputStr):
    #price sample: 
    #   class="a-price" data-a-size="m" data-a-color="price"><span class="a-offscreen">8,20 €</s
    #assuming price is between class="a-price a-text-price and €
    #then assume it is between € and >
    pricePos = inputStr.find('class="a-price a-text-price')
    pricePos1 = inputStr.find('€',pricePos)
    pricePos2 = inputStr.rfind('>',pricePos,pricePos1) + 1  #search leftwards from € 
    
    final = inputStr[pricePos2:pricePos1].replace('.','') #remove all dots 
    final = final.replace(',','.') #replace decimal separator to make it work

    return float(final)

def findProdTitle(inputStr):
    #sample: 
    #   <span id="productTitle" class="a-size-large product-title-word-break">        Gigabyte GeForce, Scheda grafica RTX 3080 GAMING OC 10GB V2 LHR       </span> 
    #find span id="productTitle" and next <, then find previous > and done
    pos0 = inputStr.find('span id="productTitle"')
    pos1 = inputStr.find('<',pos0)
    pos2 = inputStr.find('>',pos0,pos1) + 1

    return inputStr[pos2:pos1].strip()

def searchAmazon(query):
    url = f"https://www.amazon.it/s?k={query}"
    resp = getResponseURL(url)

    # data-component-type="s-search-result" -> recognize div containing search result
    # data-asin="B07TRVXS17" -> ASIN of the amazon item
    soup = BeautifulSoup(resp.text,'html.parser')
    asins = soup.findAll(attrs={"data-component-type":"s-search-result"})

    # price stored in <span class="a-price-whole">22,99</span> 
    # name: <span class="a-size-base-plus a-color-base a-text-normal">NWOUIIAY Rasoio Elettrico Uomo Wet &amp; Dry Ricaricabile Rasoio Barba con Testine Rotanti 3D ...</span>
    for asin in asins:
        id = asin['data-asin']
        try:
            priceStr = asin.find(attrs={'class':'a-price-whole'}).string
            priceStr = priceStr.replace('.','') #remove all dots 
            priceStr = priceStr.replace(',','.') #replace decimal separator to make it work
            price = float(priceStr)

            name = asin.find(attrs={'class':'a-size-base-plus a-color-base a-text-normal'}).string
            print(f"{id} {name[:50]}: EUR {price}")
        except:
            print(f"{id} not found")



    # SLOW AND STUPID 

    # for asin in asins:
    #     id = asin['data-asin']
    #     r = getItemResponse(id).text
    #     try:
    #         print(f"{id} {findProdTitle(r)}: EUR {findPriceIT(r)}")
    #     except:
    #         print(f"{id} failed")


if __name__ == "__main__":

    # url = "https://www.amazon.it/Gigabyte-GeForce-Scheda-grafica-V2/dp/B096Y36BM3/ref=sr_1_1?keywords=rtx+3080&qid=1640285620&sr=8-1"

    # r = getResponseURL(url)

    # print(f"{findProdTitle(r.text)}: {findPriceIT(r.text)}€")

    qString = input("find the price of the following item:\n")

    qStringFormat = qString.replace(' ','+')

    searchAmazon(qStringFormat)

