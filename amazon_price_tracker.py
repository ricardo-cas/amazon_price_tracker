import requests
from bs4 import BeautifulSoup
import time
import smtplib


# defing the web url form the product that i want to track
url = 'https://www.amazon.com.br/Teclado-Mecanico-K7-Rainbow-Fortrek-2019-windows/dp/B07NRTQXR6/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ASRDF755788U&dchild=1&keywords=teclado+mecanico+redragon&qid=1594258247&sprefix=teclado+meca%2Caps%2C282&sr=8-2'
# defing the headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
WANTED_PRICE = 160

# Método que vai fazer o rastreio do preço e saber se  ele está abaixo ou acima do preço alvo
def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f'Ainda está caro, ainda falta R$ {diff} para atingir o preço alvo')
    else:
        print(f'Ebá!!!! Chegou a hora de comprar! O produto atingiu um preço abaixo do seu preço alvo: {WANTED_PRICE}')

# método que pega o preço do site 
def getPrice():
    # seding a request to the page and bringing it down
    page = requests.get(url, headers=headers)
    # adding the page into the BeatifulSoup Libary
    soup = BeautifulSoup(page.content, 'html.parser')

    # Creating the variable title that will contain the title of the product that you
    title = soup.find(id ='productTitle').get_text().strip()
    price = soup.find(id = 'priceblock_ourprice').get_text().strip()[2:5]


    print(title)
    print(price)

    return price

if __name__ == "__main__":
    while True:
        getPrice()
        trackPrice()
        time.sleep(2)


'''
Testes

'''

# print(f'Sua URL é: {url}')
# print(f'Seu User Agent é: {headers}')
# url = 'https://www.amazon.com.br/Alimenta%C3%A7%C3%A3o-Material-Poli%C3%A9ster-Indicado-Multikids/dp/B07MP161W1/ref=sr_1_9?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1IBX72G2AESKO&dchild=1&keywords=lilo+stitch+pelucia&qid=1594260569&sprefix=lilo+sti%2Caps%2C272&sr=8-9'