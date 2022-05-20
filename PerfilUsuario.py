from hashlib import new
from lib2to3.pgen2 import driver
from msilib.schema import File
from pickle import TRUE
from time import time
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


#=======================================Interface Gráfica ============================================
layout =[
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login',layout)

eventos, valores = janela.read()


#Usuário e senha do perfil
login = valores['usuario']
senha = valores['senha']

#=======================================Interface Gráfica ============================================


#=======================================Imagens Fanpage ============================================

imagens = [

'https://clinichair.com.br/wp-content/uploads/2018/02/hidratacao-cabelosoleosos-11496638-633.jpg',
'https://mulhercompleta.com/wp-content/uploads/2020/05/Leave-in-para-cabelos.jpg',
'https://static.vixbrasiltv.com/pt/sites/default/files/m/mulher-passando-creme-0816-1400x800.jpg',
'https://ath2.unileverservices.com/wp-content/uploads/sites/2/2016/09/condicionador-antes-do-shampoo-abre-782x439.jpg',
'https://tudoela.com/wp-content/uploads/2016/06/mulher-lavando-o-cabelo-1-810x540.jpg',
'https://portal6.com.br/wp-content/uploads/2021/09/mulher-lavando-cabelo-0816-1400x800-1.jpg',
'https://meajudenatransicao.com.br/wp-content/uploads/2018/12/lavar-o-cabelo-todo-dia-faz-mal-1024x683.jpg',
'https://istoe.com.br/wp-content/uploads/sites/14/2021/08/lavando-cabelo-scaled.jpg',
'https://opetroleo.com.br/wp-content/uploads/2021/03/463_shampun_pivo.jpg',
'https://s2.glbimg.com/YWJQ3jx0xcSEOcIlEV4WCGxiRaI=/512x320/smart/e.glbimg.com/og/ed/f/original/2017/04/24/lavar-cabelo.jpg'
]

#=======================================Imagens Fanpage ============================================

#=======================================Postagens perfil ============================================

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

#=======================================Postagens perfil ============================================

#=======================================Reações ============================================

reacoes = [
'//*[@id="root"]/table/tbody/tr/td/ul/li[1]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[2]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[3]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[4]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[5]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[6]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
'//*[@id="root"]/table/tbody/tr/td/ul/li[7]/table/tbody/tr/td/a/div/table/tbody/tr/td[2]',
]

#=======================================Reações ============================================

#=======================================Sentir-se ============================================
sentir1 = [

'//*[@id="root"]/table/tbody/tr/td/ul/li[1]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[2]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[3]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[4]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[5]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[6]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[7]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[8]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[9]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[10]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[11]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[12]/div/table/tbody/tr/td[2]/a',
'//*[@id="root"]/table/tbody/tr/td/ul/li[13/div/table/tbody/tr/td[2]/a'
]

sentir2 = [
'//*[@id="root"]/table/tbody/tr/td/ul/li[1]/table/tbody/tr/td/table/tbody/tr/td[2]/a'
]

#=======================================Sentir-se ============================================

#=======================================Iniciando programa ============================================

#Chame o Drive do chrome

navegador = webdriver.Chrome("chromedriver.exe")

#Acessando o facebook no modo lite
navegador.get("https://mbasic.facebook.com/")


#Tempo para carregamento da página
time.sleep(5)

#Fazendo login facebook 
navegador.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(login)
navegador.find_element_by_xpath('//*[@id="password_input_with_placeholder"]/input').send_keys(senha)
navegador.find_element_by_xpath('//*[@id="login_form"]/ul/li[3]/input').click()

#Tempo para carregamento da página
time.sleep(5)


#Não quero logar com 1click
navegador.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div/div[3]/a').click()
time.sleep(10)

#=======================================Iniciando programa ============================================

postagensNum = 0
while postagensNum <= postagensNum:
   
    time.sleep(15)

    #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(19)
    
    #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
     #=================== Terminou ==============================

    time.sleep(26)

     #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
     #=================== Terminou ==============================

    time.sleep(375)
    
    #=================== Entrando em grupos ==============================

    #Entrando em grupos
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="header"]/nav/a[8]').click()
    time.sleep(2)
    navegador.find_element_by_link_text('Participar').click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

     #=================== Terminou ==============================

    time.sleep(265)

    #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================
    
    time.sleep(457)

      #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(127)

    #=================== Postando Mensagem de texto ==============================
    
    #Digita a mensagem de texto
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[2]/div/textarea').send_keys(random.choice(postagens))
    

    #Envia a mensagem de texto
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[3]/div/input').click()
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(27)

   #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(37)

    #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(942)
    
    #=================== Postando Foto ==============================
    
    # Clica no botão Postar foto
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="mbasic-composer-form"]/div[2]/span/div[1]/table/tbody/tr/td[2]/input').click()
    time.sleep(15)

    #Clica para selecionar o arquivo da foto
    time.sleep(5)
    navegador.find_element_by_class_name('ba').click()
    time.sleep(10)

    #Seleciona a foto 
    time.sleep(5)
    pyautogui.write(random.choice(imagens))
    time.sleep(5)

    #Clica no Enter do teclado para confirmar a seleção
    time.sleep(5)
    pyautogui.press('Enter')
    time.sleep(10)

    #Clica no botão previa
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]').click()
    time.sleep(10)

    #Faz a postagem da foto
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="composer_form"]/input[19]').click()
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================

    time.sleep(160)

    #=================== Reagindo a públicações ==============================

    #Reagindo a públicações
    time.sleep(5)
    navegador.find_element_by_link_text('Reagir').click()
    time.sleep(2)
    navegador.find_element_by_xpath(random.choice(reacoes)).click()
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()
    
    #=================== Terminou ==============================
 
    time.sleep(600)
  
   


