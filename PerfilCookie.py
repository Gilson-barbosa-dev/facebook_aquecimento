from hashlib import new
from lib2to3.pgen2 import driver
from msilib.schema import File
from pickle import TRUE
from webbrowser import Chrome
from requests import options
from selenium import webdriver
import time
import random
import pyautogui
import PySimpleGUI as sg
#Bibliotecas utilizadas Selenium, time
# Baixar chromedrive conforme a versão do seu chrome 
#Precisar baixar o e deixar na pasta de destino o chromedriver link para download https://chromedriver.chromium.org/downloads

#Imagens
imagens = [
'https://www.des1gnon.com/wp-content/uploads/2020/03/Pexels-Banco-de-Imagens-gratis-Des1gnON.jpg',
'https://images.pexels.com/photos/2859616/pexels-photo-2859616.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260',
'https://s1.1zoom.me/big0/815/Sunrises_and_sunsets_Hands_Sun_571948_1280x918.jpg',
'https://imagens.mdig.com.br/thbs/45184mn.jpg',
'https://i.pinimg.com/originals/1b/24/d3/1b24d3bb3ff75aab49a62c27dd1dcf98.jpg',
'https://imagens.ebc.com.br/5imVYbYeZRa2QiaZrqw-E-bCNBY=/754x0/smart/https://radios.ebc.com.br/sites/default/files/thumbnails/image/tedio.jpeg'
'https://uploads.bemparana.com.br/upload/image/noticia/noticia_706260_img1_games.jpg'
'https://4.bp.blogspot.com/-gkE-FWMZVvQ/VkpUef9rKuI/AAAAAAAAAnU/IWnbeSjZQuA/s1600/0.jpg'
'https://www.decorfacil.com/wp-content/uploads/2021/04/20210416oque-fazer-no-tedio-faxina.jpg'
'https://www.decorfacil.com/wp-content/uploads/2021/04/20210416cozinhar.jpg'

]

#postagens
postagens = [
'Minha missão na vida não é apenas sobreviver, mas prosperar.',
'Olhe para o céu e escute as mensagens de Deus para hoje!',
'Jamais se esqueça: você é o motivo do sorriso de muitas pessoas. ',
'Não tenho medo de aceitar que você não é mais o mesmo.',
'Os sonhos servem para abrir o caminho e mostrar a direção.',
'Um dia tudo isto ainda vai parecer pequeno, porque tuas conquistas te farão enorme.',
'Aceite que seu corpo precisa de descanso para recuperar energias! Não se exija em excesso.',
'Confie no que a vida planejou para você!',
'Desconfie do destino e acredite em você.',
'A vida é uma aventura ousada ou nada...',
'Tenha orgulho da pessoa que você é.',
'Confie em você e no seu potencial. Você pode fazer muito mais do que imagina!',
'A força que você busca mora dentro de você.',
'Abra os braços e receba a vida com amor. Ela também quer que tudo dê certo para você.',
'A vida já é complicada, não torne tudo mais pesado! Permita-se agir com mais leveza.',
'Faça hoje o que vai te dar orgulho amanhã.',
'Meta do dia: agradecer por estar vivo!'
]

reacoes = [
'//*[@id="root"]/table/tbody/tr/td/ul/li[1]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[2]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[3]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[4]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[5]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[6]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[7]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
]

comentarios = [
'Muito legal',
'Gostei demais',
'Muito Top!',
'UP',
'Gosto de postagens assim',
'Que demais',
'Vamos ajudar a repostar pessoal',
'Ai eu dou valor'
]

navegador = webdriver.ChromeOptions()
navegador.add_extension('cookie.crx')
navegador = webdriver.Chrome(chrome_options=navegador)

#Acessando o facebook no modo lite
navegador.get("https://mbasic.facebook.com/")


#Tempo para usuário colocar o cookie
time.sleep(30)

pyautogui.press('F5')

postagensNum = 0
while postagensNum <= postagensNum:

    #=================== Reagindo a públicações ==============================

    try:

      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Reagindo a públicações ==============================
    
    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
     #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

     #=================== Reagindo a públicações ==============================

    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
     #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))
    
    #=================== Entrando em grupos ==============================
    try:

      navegador.find_element_by_xpath('//*[@id="header"]/nav/a[8]').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_link_text('Participar').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
     #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Reagindo a públicações ==============================
    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================
    
    time.sleep(random.choice(range(175,580)))

      #=================== Reagindo a públicações ==============================
    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Postando Mensagem de texto ==============================
    try:

      navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[2]/div/textarea').send_keys(random.choice(postagens))
      
      #Envia a mensagem de texto
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[3]/div/input').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

   #=================== Reagindo a públicações ==============================
    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Reagindo a públicações ==============================
    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))
    
    #=================== Postando Foto ==============================
    try:
    
      navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/div[2]/span/div[1]/table/tbody/tr/td[2]/input').click()

      #Clica para selecionar o arquivo da foto
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_class_name('ba').click()
      
      #Seleciona a foto 
      time.sleep(random.choice(range(5,20)))
      pyautogui.write(random.choice(imagens))

      #Clica no Enter do teclado para confirmar a seleção
      time.sleep(random.choice(range(5,20)))
      pyautogui.press('Enter')
      time.sleep(random.choice(range(5,20)))

      #Clica no botão previa
      time.sleep(random.choice(range(15,30)))
      navegador.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]').click()

      #Faz a postagem da foto
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="composer_form"]/input[19]').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Reagindo a públicações ==============================

    try:

      navegador.find_element_by_link_text('Reagir').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath(random.choice(reacoes)).click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

    except Exception as e:
      navegador.get("https://mbasic.facebook.com/")
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Comentário ==============================
    try:
      
      navegador.find_element_by_partial_link_text('coment').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_partial_link_text('Comentar').click()
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="root"]/section/form/div[1]/textarea').send_keys(random.choice(comentarios))
      time.sleep(random.choice(range(5,20)))
      navegador.find_element_by_xpath('//*[@id="root"]/section/form/div[4]/input').click()
      time.sleep(random.choice(range(5,20)))
    
    except Exception as e:
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))

    #=================== Sentindo-se ==============================
    try:
        #Sentir-se
        y = [1,2,6,9,10]
        reacao = (random.choice(y))

        #Sentir-se 2
        x = range(1,18)
        reacao2 = (random.choice(x))

        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/div[2]/span/div[2]/table/tbody/tr/td[2]/input').click()
        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_xpath(f'//*[@id="root"]/table/tbody/tr/td/ul/li[{reacao}]/div/table/tbody/tr/td[2]/a').click()
        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_xpath(f'//*[@id="root"]/table/tbody/tr/td/ul/li[{reacao2}]/table/tbody/tr/td/table/tbody/tr/td[2]/a').click()
        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_xpath('//*[@id="composer_form"]/input[18]').click()

    except Exception as e:
      navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
        #=================== Terminou ==============================
   
    time.sleep(random.choice(range(175,580)))

    #=================== Compartilhar publicações ==============================

    try:
        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_partial_link_text('Compartilhar').click()
        time.sleep(random.choice(range(5,20)))
        navegador.find_element_by_xpath('//*[@id="composer_form"]/input[18]').click()
        
    except Exception as e:
        navegador.get('https://mbasic.facebook.com/')
    #=================== Terminou ==============================

    time.sleep(random.choice(range(175,580)))