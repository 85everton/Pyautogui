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
#Inserir produtos da promocao 2
pyautogui.press('Esc')
pyautogui.press('3')
pyautogui.press('home')
pyautogui.write('7368')
pyautogui.press('enter')
pyautogui.press('7')
pyautogui.press('home')
pyautogui.write('14422')
pyautogui.press('enter')
pyautogui.press('7')
pyautogui.press('home')
pyautogui.write('32987')
pyautogui.press('enter')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
pyautogui.alert("Total de descontos da promoção 2 deve ser R$ 12,00 e total da venda R$ 40,33, Caso os valores estiverem incorretos abortar a automação")
pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 3
pyautogui.press('Esc')
pyautogui.press('7')
pyautogui.press('home')
pyautogui.write('5598')
pyautogui.press('enter')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
pyautogui.alert("Total de descontos da promoção 3 deve ser R$ 2,21 e total da venda R$ 19,84, Caso os valores estiverem incorretos abortar a automação")
pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 4
pyautogui.press('Esc')
pyautogui.write('35026')
pyautogui.press('enter')
pyautogui.write('35015')
pyautogui.press('enter')
pyautogui.write('1876')
pyautogui.press('enter')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
pyautogui.alert("Total de descontos da promoção 4 deve ser R$ 3,28 e total da venda R$ 1,99, Caso os valores estiverem incorretos abortar a automação")
pyautogui.press('F4')
time.sleep(3)
#Inserir produtos da promocao 5
pyautogui.press('Esc')
pyautogui.write('30906')
pyautogui.press('enter')
pyautogui.write('25957')
pyautogui.press('enter')
pyautogui.write('30664')
pyautogui.press('enter')
pyautogui.press('4')
pyautogui.press('home')
pyautogui.write('32807')
#Subtotal e finalizar a venda
pyautogui.PAUSE = 0.5
pyautogui.press('s')
pyautogui.alert("Total de descontos deve ser R$ 13,95 e total da venda R$ 33,95, Caso os valores estiverem incorretos abortar a automação")
pyautogui.press('F4')
time.sleep(3)
#Retornar o PDV para caixa Livre
pyautogui.press('Esc')
pyautogui.press('Esc')
#Finalizar Teste
pyautogui.alert("Testes finalizados, verificar o log se necessario")