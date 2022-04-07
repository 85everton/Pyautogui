import pyautogui
import locale

local1 = pyautogui.locateOnScreen('arquivo.png')
print(local1)
print(local1.left)
print(local1[0])
print(local1.top)
print(local1[1])
local_todos = list(pyautogui.locateAllOnScreen('arquivo.png'))
print(local_todos)