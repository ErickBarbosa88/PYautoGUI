from time import time
import pyautogui
import pyperclip
import time
import pandas

tabela = pandas.read_excel("C:/Users/Shinom/Downloads/Vendas.xlsx")
print(tabela)

quantidade = tabela["Quantidade"].sum()
print(quantidade)

# entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(1064, 374)
time.sleep(1)
pyautogui.click
pyautogui.hotkey("ctrl", "t")
pyperclip.copy(
    "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
print(pyautogui.position())
pyautogui.click(359, 268, clicks=2)
# print(pyautogui.position())
time.sleep(2)
pyautogui.click(372, 414)
pyautogui.click(1393, 160)
time.sleep(0.7)
pyautogui.click(1231, 581)
