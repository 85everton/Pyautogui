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
pyautogui.press('Esc')
#Inserir produtos da promocao 6
logging.info("Iniciando teste com a promocao 6")
pyautogui.write('1008')
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
promo6 = pyautogui.locateOnScreen('C:\git\Testes\imagens\promo\promo6.png')
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
pyautogui.alert("Testes finalizados, verificar o log se necessario")