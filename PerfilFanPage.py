from secrets import choice
import time
import pyautogui
from selenium import webdriver
import random
from urllib.parse import urlparse

#imagens postagem dica de cabelo fanpage

imagensfan = [

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
#Postagem de dicas de cabelo

postagemfan = [

'Atenção à temperatura da água: procure lavar os fios com a temperatura mais baixa que conseguir. Não precisa ser muito fria, mas também não pode ser quente. Dessa forma, o cabelo não ficará ressecado e terá muito mais brilho, ou seja, se o cabelo for oleoso, irá reduzir o nível de gordura, e se for seco, irá desidratar menos.',
'O primeiro passo na lavagem é aplicar o shampoo. Sua função é limpar o couro cabeludo. A quantidade correta que deve ser utilizada não é proporcional ao tamanho do cabelo, ao contrário, basta despejar um pouco do produto na palma da mão e diluir com água para distribuí-lo melhor e fazer mais espuma sem sobrecarregar os fios.',
'Caso o cabelo não se encontre muito sujo, não há necessidade de aplicar o shampoo duas vezes. Esse hábito torna-se desnecessário quando se lava os fios com frequência. Além de não trazer nenhum benefício, nos leva a consumir mais produto, gastar mais água e mais energia.',
'Lavar o cabelo com as unhas é um perigo, pois contribui para a disseminação de fungos e bactérias no couro cabeludo. Use a ponta dos dedos.',
'Evite esfregar o cabelo durante a lavagem! Deixe que a espuma envolva os fios e massageie suavemente, deslizando os dedos. Shampoo é uma palavra de origem indiana e significa "massagear"! Importante sempre se lembrar disso na hora de lavar o cabelo.',
'Enxágue o cabelo até retirar os produtos por completo evitando, assim, o acúmulo de resíduos que podem deixar o cabelo pesado.',
'O segundo passo é aplicar a máscara de tratamento apenas de uma a duas vezes por semana. Sua função é nutrir e hidratar os fios dos cabelos prejudicados e enfraquecidos por fatores externos. A máscara não substitui o condicionador. Ambos são complementares.',
'O condicionador finaliza o processo de lavagem dos fios. Sua função é proteger os fios selando a cutícula. Além disso, é o condicionador que oferece maleabilidade ao cabelo. Nesse caso, a quantidade correta que deve ser utilizada é proporcional ao comprimento do cabelo. Não esquecer que o condicionador deve ser passado somente nos fios e nunca na raiz.',
'Antes de aplicar o condicionador e a máscara, lembre-se de retirar o excesso de água do cabelo. O produto ficará menos diluído e a ação será mais efetiva.',
'Consulte um profissional para diagnosticar quais produtos são ideais ao seu tipo de cabelo. Assim, você evita produtos que agridem os fios.'

]


#usuário precisa falar o nome da página

fanpage = input('qual o nome da fan page? ')

navegador = webdriver.ChromeOptions()
navegador.add_extension('cookie.crx')
navegador = webdriver.Chrome(chrome_options=navegador)

#Acessando o facebook no modo lite
navegador.get("https://mbasic.facebook.com/")


#Tempo para usuário colocar o cookie
time.sleep(30)

pyautogui.press('F5')

time.sleep(5)

#=================== Postando na Fanpage ==============================



navegador.get(f'https://mbasic.facebook.com/{fanpage}')


#Clica em públicar postagem
time.sleep(10)
navegador.find_element_by_xpath('//*[@id="mFinchContainer"]/div/div[3]/div/div[2]/table/tbody/tr/td[1]/a').click()

#texto da postagem 
time.sleep(10)
navegador.find_element_by_name('xc_message').send_keys(random.choice(postagemfan))

#Clica para anexar a imagem  
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="composer_form"]/div[2]/div[2]/table/tbody/tr/td[2]/input').click()

#Escolhe a imagem navegador 
time.sleep(5)
navegador.find_element_by_class_name('ba').click()
time.sleep(5)
pyautogui.write(random.choice(imagensfan))

#Clica no Enter do teclado para confirmar a seleção
time.sleep(5)
pyautogui.press('Enter')

#Clica no botão previa
time.sleep(15)
navegador.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]').click()

#Faz a postagem da publicação
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="composer_form"]/input[20]').click()
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="header"]/form/table/tbody/tr/td[1]/a/img').click()

#=================== Terminou ==============================