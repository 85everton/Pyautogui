from time import time
import pyautogui
import time


#Inicializar testes com o PDV
pyautogui.alert("Abrir a versão do PDV a ser testada e deixar na tela de Caixa Livre e pressionar OK")
pyautogui.PAUSE = 0.5
#Abrir o PDV
pyautogui.hotkey('alt', 'tab')
pyautogui.PAUSE = 0.5

#Entrar no caixa
pyautogui.press('i')
pyautogui.PAUSE = 0.5
pyautogui.press('Esc')
#Inserir produtos para o primeiro Cartão
pyautogui.write('5')
pyautogui.press('home')
pyautogui.write('7891000100103')
pyautogui.press('enter')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
#Passando Cartão Crédito Master
pyautogui.press('F6')
time.sleep(3)
pyautogui.write('3')
pyautogui.press('enter')
pyautogui.write('2')
pyautogui.press('enter')
pyautogui.write('5124549074480795')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('1123')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('132')
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
# Retornar o PDV para caixa Livre
time.sleep(9)
pyautogui.press('Esc')
pyautogui.press('Esc')
#Entrar no caixa
pyautogui.press('i')
pyautogui.PAUSE = 0.5
pyautogui.press('Esc')
#Inserir produtos para o segundo cartão
pyautogui.write('5')
pyautogui.press('home')
pyautogui.write('7891000100103')
pyautogui.press('enter')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
#Passando Cartão Crédito visa
pyautogui.press('F6')
time.sleep(3)
pyautogui.write('3')
pyautogui.press('enter')
pyautogui.write('2')
pyautogui.press('enter')
pyautogui.write('4485609661290324')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('0623')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('255')
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
# Retornar o PDV para caixa Livre
time.sleep(9)
pyautogui.press('Esc')
pyautogui.press('Esc')
pyautogui.alert("Testes finalizados verificar o VRMaster consistencia e transação TEF")