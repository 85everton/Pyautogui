from time import time
from tkinter import W
import pyautogui
import time
import logging
logging.basicConfig(filename = "teste.log", level = logging.INFO, filemode=W)


#Inicializar testes com o PDV
pyautogui.alert("Abrir a versão do PDV a ser testada e deixar na tela de Caixa Livre e pressionar OK")
logging.info("Inicializando Testes")
time.sleep(1)
#Abrir o PDV
pyautogui.hotkey('alt', 'tab')
#Entrar no caixa
pyautogui.press('i')
time.sleep(1)
#Inserir produtos da promocao 1
pyautogui.press('Esc')
time.sleep(1)
logging.info("Iniciando teste com a promocao 1 Promocao com aplicar todos desmarcado somente 1 item deve receber o desconto")
logging.info("Subtotal Venda 14,98 total de desconto 1,00")
pyautogui.write('28277')
pyautogui.press('enter')
pyautogui.write('25230')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo1 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo1.png')
if promo1:
    logging.info("Valor da promocao 1 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 1 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 2
logging.info("Iniciando teste com a promocao 2 Promocao com Limite de itens")
logging.info("Subtotal Venda 40,33 total de desconto 12,00")
pyautogui.press('Esc')
time.sleep(1)
pyautogui.write('3')
pyautogui.press('home')
pyautogui.write('7368')
pyautogui.press('enter')
pyautogui.write('7')
pyautogui.press('home')
pyautogui.write('14422')
pyautogui.press('enter')
pyautogui.write('7')
pyautogui.press('home')
pyautogui.write('32987')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo2 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo2.png')
if promo2:
    logging.info("Valor da promocao 2 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 2 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 3
logging.info("Iniciando teste com a promocao 3 Promocao com a aba ganha")
logging.info("Subtotal Venda 19,84 total de desconto 2,21")
pyautogui.press('Esc')
time.sleep(1)
pyautogui.write('7')
pyautogui.press('home')
pyautogui.write('5598')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo3 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo3.png')
if promo3:
    logging.info("Valor da promocao 3 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 3 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 4
logging.info("Iniciando teste com a promocao 4 utilizando 3 itens para ativar aba Paga")
logging.info("Subtotal Venda 1,99 total de desconto 3,28")
pyautogui.press('Esc')
time.sleep(1)
pyautogui.write('35026')
pyautogui.press('enter')
pyautogui.write('35015')
pyautogui.press('enter')
pyautogui.write('1876')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo4 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo4.png')
if promo4:
    logging.info("Valor da promocao 4 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 4 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 5
logging.info("Iniciando teste com a promocao 5 utilizando campo Quantidade proporcional")
logging.info("Subtotal Venda 33,99 total de desconto 0,50")
pyautogui.press('Esc')
pyautogui.write('2904')
pyautogui.press('enter')
time.sleep(5)#Produto de balança necessario sequencia especifica de comandos
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('2')
pyautogui.press('enter')
pyautogui.write('0,5')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 0.5
pyautogui.write('2923')
pyautogui.press('enter')
time.sleep(5)#Produto de balança necessario sequencia especifica de comandos
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('2')
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo5 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo5.png')
if promo5:
    logging.info("Valor da promocao 5 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 5 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 6
pyautogui.press('Esc')
logging.info("Iniciando teste com a promocao 6 Utilizando quantidade proporcional fracionada")
logging.info("Subtotal Venda 1,70 total de desconto 0,50")
pyautogui.write('1008')
pyautogui.press('enter')
time.sleep(5)#Produto de balança necessario sequencia especifica de comandos
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('2')
pyautogui.press('enter')
pyautogui.write('0,5')
pyautogui.press('enter')
pyautogui.press('enter')
#Subtotal e finalizar a venda
time.sleep(1)
pyautogui.press('s')
time.sleep(1)
promo6 = pyautogui.locateOnScreen('C:\\git\\Testes\\imagens\\promo\\promo6.png')
if promo6:
    logging.info("Valor da promocao 6 esta correto, TESTE APROVADO")
    pyautogui.press('F4')
else:
   logging.info("Valor da promocao 6 esta incorreto, TESTE FALHOU") 
   pyautogui.press('F4')
time.sleep(3)
#Retornar o PDV para caixa Livre
pyautogui.press('Esc')
pyautogui.press('Esc')
#Finalizar Teste
logging.info("Testes Finalizados")
pyautogui.alert("Testes finalizados, verificar o log do pdv e a consistencia se necessario")