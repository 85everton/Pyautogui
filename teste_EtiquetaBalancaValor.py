from time import time
import pyautogui
import time


#Inicializar testes com o PDV
pyautogui.alert("Abrir a versão do PDV a ser testada e deixar na tela de Caixa Livre e pressionar OK")
pyautogui.PAUSE = 0.5
#Abrir o PDV
pyautogui.hotkey('alt', 'tab')
#Entrar no caixa
pyautogui.press('i')
pyautogui.PAUSE = 0.5
pyautogui.press('Esc')
#Inserir produto KG
pyautogui.write('2001034003607')
pyautogui.press('enter')
pyautogui.alert("Verifique se a etiqueta passou com peso de 100 gramas")
#Inserir produto com peso menor que 5 gramas
pyautogui.write('2001034000147')
pyautogui.press('enter')
pyautogui.alert("Verifique se o produto com menos de 5 gramas vai ser vendido")
#Inserir etiqueta de produto UN
pyautogui.write('2000460007597')
pyautogui.press('enter')
pyautogui.alert("Verifique se a etiqueta de produto UN vai entrar")
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
pyautogui.PAUSE = 0.5
pyautogui.press('F4')
#Retornar o PDV para caixa Livre
time.sleep(1)
pyautogui.press('Esc')
pyautogui.press('Esc')
#Finalizar Teste
pyautogui.alert("Testes finalizados, verificar o log se necessario")