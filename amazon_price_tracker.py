import requests
from bs4 import BeautifulSoup
import time
import smtplib
import os

# defing the web url form the product that i want to track
url = 'https://www.amazon.com.br/Teclado-Mecanico-K7-Rainbow-Fortrek-2019-windows/dp/B07NRTQXR6/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ASRDF755788U&dchild=1&keywords=teclado+mecanico+redragon&qid=1594258247&sprefix=teclado+meca%2Caps%2C282&sr=8-2'
# defing the headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# definindo o preço alvo de compra
WANTED_PRICE = 260
email = os.environ.get('GMAIL_USER')
senha = os.environ.get('GMAIL_PASSWORD')

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
    # title = soup.find(id ='productTitle').get_text().strip()
    price = soup.find(id = 'priceblock_ourprice').get_text().strip()[2:5]

    # print(title)
    # print(price)

    return price

# função que envia e-mail automático caso tenha o preço for abaixo do preço alvo 
# def enviaEmail():

    
    # definindo qual servidor SMTP iremos enviar e qual porta utilizar
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    
    # comando utilizado para enviar ao server uma requisição entre dois serveres de e-mail
    # server.ehlo()
    
    # encriptando a conexão
    # server.starttls()
    
    # # comando utilizado para enviar ao server uma requisição entre dois serveres de e-mail
    # server.ehlo()
    
    # efetuando login no server
    # server.login(email,senha)

    # definindo o assunto do e-mail
    # assunto = f'Preço do produto caiu!'
    
    # definindo a mensagem no corpo do e-mail
    # corpo = f'O preço do produto caiu, entra lá pra comprar! https://www.amazon.com.br/Teclado-Mecanico-K7-Rainbow-Fortrek-2019-windows/dp/B07NRTQXR6/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ASRDF755788U&dchild=1&keywords=teclado+mecanico+redragon&qid=1594258247&sprefix=teclado+meca%2Caps%2C282&sr=8-2'

    # msg = f"Subject:{assunto}\n\n{corpo}"
    # mensagem = msg.encode('ascii')

    # remetente = 'seue-mail@gmail.com'.encode('utf8')
    # para = 'seue-mail@gmail.com'.encode('utf8')

    # server.sendmail( email , email, msg)

    # print('E-mail enviado! :D')

    # server.quit()
def enviarEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login(email,senha)

    assunto = 'Teste de envio de e-mail via Python 3 - com URL '
    corpo = 'https://www.amazon.com.br/Teclado-Mecanico-K7-Rainbow-Fortrek-2019-windows/dp/B07NRTQXR6/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3ASRDF755788U&dchild=1&keywords=teclado+mecanico+redragon&qid=1594258247&sprefix=teclado+meca%2Caps%2C282&sr=8-2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin facilisis vestibulum laoreet. Quisque venenatis faucibus augue, quis gravida ligula tincidunt at. Phasellus non gravida justo. Nunc sit amet purus nisi. Vestibulum ullamcorper mi arcu, id cursus quam facilisis eget. Phasellus pulvinar pellentesque volutpat. In pellentesque lacus vel molestie tempus. In ut faucibus magna. Proin at varius felis. Phasellus suscipit in nisi sed fringilla. Fusce a lectus ante. Proin eu turpis at nulla ultricies condimentum. Suspendisse eget scelerisque metus, venenatis rhoncus augue.Pellentesque ligula ligula, cursus at metus vitae, vestibulum dapibus eros. Vestibulum venenatis tortor at ipsum imperdiet, non luctus turpis fringilla. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas porttitor lacus ipsum, eu feugiat metus tempor vitae. Duis quis orci tellus. In rutrum felis id porta dignissim. Phasellus fermentum ipsum eu elit efficitur placerat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam lectus diam, commodo vel risus eu, vulputate imperdiet purus. Curabitur et luctus nulla. Vestibulum aliquam faucibus nisl, eu viverra tellus commodo et. Sed in arcu eleifend, interdum magna ut, placerat quam. Morbi luctus diam vel rhoncus mollis. Pellentesque nisl nibh, hendrerit vel rutrum vitae, egestas sed leo. Vivamus sed leo a metus porttitor scelerisque. Integer aliquet ex lorem, non laoreet felis auctor quis.Etiam et tempor mauris, sed accumsan metus. Aenean ut tortor orci. Duis vulputate lacus ligula, ac faucibus dolor cursus sed. Integer ut gravida nisi, in lacinia est. Phasellus iaculis felis id massa bibendum gravida. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce vel tempor ligula, ac imperdiet dolor. Sed tincidunt, ipsum sit amet vehicula consequat, nisl tortor pulvinar nisi, eu mollis sem libero eget purus. Maecenas dui purus, luctus eget neque a, ullamcorper accumsan sem. Aliquam erat volutpat. Donec laoreet, nunc ac vulputate pulvinar, mi est sodales leo, eu varius elit diam eu ex. Nunc nisi tellus, tincidunt ut vestibulum ut, pellentesque nec nisi. Phasellus et nisi augue. Ut non sem eget mi ultricies tincidunt eget et metus. Proin posuere arcu ipsum, id pellentesque massa pretium ut. Mauris tincidunt sodales felis nec faucibus.Praesent dapibus aliquam massa, at porttitor dolor eleifend at. Morbi lectus turpis, pulvinar eleifend mi ac, convallis congue lorem. Curabitur rutrum tincidunt tempor. Cras sed magna nisi. Sed vehicula, diam vel venenatis pretium, sem ipsum tincidunt nibh, vel blandit urna elit id augue. Suspendisse potenti. Cras in nulla non arcu venenatis lobortis eget ut tortor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus accumsan odio vel sem interdum, at finibus nulla efficitur. Duis eu bibendum purus. Quisque tempus rutrum euismod. Vivamus mattis pellentesque justo, bibendum tristique leo tempus eget. In sed magna facilisis, placerat eros eget, tristique turpis.Vivamus pretium urna a ante dictum cursus. Sed tristique quam in semper gravida. Mauris gravida vestibulum massa, at consectetur odio rutrum a. Proin sollicitudin facilisis molestie. Aenean vel fringilla odio. Maecenas aliquet pellentesque quam, luctus convallis nunc tincidunt a. Sed rhoncus elit eget ipsum vehicula tempor. Mauris massa mi, placerat nec nunc vel, blandit rutrum dui. Phasellus nec eros scelerisque, ultrices quam vitae, facilisis ante. Vestibulum quis ex ullamcorper, volutpat orci ac, viverra sem. Praesent posuere imperdiet aliquet.'
    msg = f'Subject: {assunto}\n\n{corpo}'


    server.sendmail(email, email, msg)
    print('E-mail enviado! :)')
    quit()


# Validação para garantir que estou chamando a classe principal Main
if __name__ == "__main__":
    while True:
        getPrice()
        trackPrice()
        enviarEmail()
        
        # time.sleep(2)


'''
Testes

'''

# print(f'Sua URL é: {url}')
# print(f'Seu User Agent é: {headers}')
# url = 'https://www.amazon.com.br/Alimenta%C3%A7%C3%A3o-Material-Poli%C3%A9ster-Indicado-Multikids/dp/B07MP161W1/ref=sr_1_9?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1IBX72G2AESKO&dchild=1&keywords=lilo+stitch+pelucia&qid=1594260569&sprefix=lilo+sti%2Caps%2C272&sr=8-9'