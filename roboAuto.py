from time import time
import pyautogui
import time
import logging
logging.basicConfig(filename = "teste.log", level = logging.INFO)


#Inicializar testes com o PDV
pyautogui.alert("Abrir a versão do PDV a ser testada e pressionar OK")
#Abrir o PDV
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
#localizar informação do caixa Livre para seguir
#Entrar no caixa
cxlivre = pyautogui.locateOnScreen('C:\git\Testes\imagens\padrao\caixaLivre.png')
if cxlivre:
    pyautogui.alert("passou no livre")
    logging.info("passou no livre")
    pyautogui.press('i')
else:
   pyautogui.alert("Caixa inicial não foi encontrado") 
   exit()
#Entrar no caixa e responder sobre o CNPJ/CPF
time.sleep(1)
#Entrar cliente
cnpjCpf = pyautogui.locateOnScreen('C:\git\Testes\imagens\padrao\CnpjCpf.png')
if cnpjCpf:
    pyautogui.alert("passou no cpf")
    logging.info("passou no cpf")
    pyautogui.press('Esc')
else:
   pyautogui.alert("Não foi localizado identificação do consumidor") 
   exit()
#Inserir um produto
codProd = pyautogui.locateOnScreen('C:\git\Testes\imagens\padrao\codProduto.png')
if codProd:
    pyautogui.write('4043')
    pyautogui.press('enter')
    pyautogui.alert("passou no produto")
    logging.info("passou no produto")
else:
   pyautogui.alert("Caixa não retornou para inserção do produto") 
   exit()
#Subtotal e finalizar a venda
pyautogui.press('s')
time.sleep(1)
subTotal = pyautogui.locateOnScreen('C:\git\Testes\imagens\padrao\eceber.png')
if subTotal:
    pyautogui.alert("passou na venda")
    logging.info("passou no venda")
    pyautogui.press('F4')
else:
    pyautogui.alert("Valor da Venda não bate com o esperado") 
    exit()
time.sleep(1)
#Fechar o PDV
pyautogui.press('Esc')
#pyautogui.press('F1')
#pyautogui.write('113')
#pyautogui.press('enter')
time.sleep(1)
#pyautogui.press('1')
#pyautogui.press('enter')
#Finalizar Teste
pyautogui.alert("Testes finalizados, verificar o log se necessario")
logging.info("Testes finalizados")