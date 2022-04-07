from time import time
import pyautogui
import time
from tkinter import W
import logging
logging.basicConfig(filename = "teste.log", level = logging.INFO, filemode=W)

# Inicializar testes com o PDV
pyautogui.alert("Abrir a versão do PDV a ser testada e pressionar OK")
pyautogui.PAUSE = 0.5
# Abrir o PDV
pyautogui.hotkey('alt', 'tab')
i = 1
while i < 10:
# Entrar no caixa
    pyautogui.press('i')
    pyautogui.PAUSE = 0.5
    pyautogui.press('Esc')
# Inserir um produto
    pyautogui.write('7896045523412')
    pyautogui.press('enter')
# Subtotal e finalizar a venda
    pyautogui.PAUSE = 0.5
    pyautogui.press('s')
    #time.sleep(1)
    conf_Pagto = pyautogui.locateOnScreen('C:\git\Testes\imagens\padrao\eceber.png')
    if conf_Pagto:
        logging.info("Looping " + str(i) + " Passou")
        pyautogui.press('F4')
    else:
        logging.info("Teste nao completou o passo " + str(i) + " TESTE FALHOU") 
        pyautogui.alert("Testes finalizados, verificar o log se necessario")
        exit()
    time.sleep(3)
# Retornar o PDV para caixa Livre
    pyautogui.PAUSE = 1.0
    pyautogui.press('Esc')
    pyautogui.press('Esc')
    #logging.info(i)
    i = i + 1
# Finalizar Teste
pyautogui.alert("Testes finalizados, verificar o log se necessario")
