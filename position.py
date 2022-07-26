# time.sleep(4)
# print(pyautogui.position())
from time import time
import pyautogui
import pyperclip
import time
import pandas

tabela = pandas.read_excel("C:/Users/Shinom/Downloads/Vendas.xlsx")
print(tabela)

quantidade = tabela["Quantidade"].sum()
print(quantidade)