import PySimpleGUI as vt
import pywhatkit
import keyboard
import time
from datetime import datetime

vt.theme("Topanga")
layout = [
     [vt.Text("Bem vindo ao RenegadeBot!")],
     [vt.Button("Run", button_color="green")],
     [vt.Button("Exit", button_color="red")],
     ]

janela = vt.Window("RenegadeBot", element_justification='center', layout=layout, size=(250,140 ))

while True:
    evento, valores = janela.read()
    if evento == vt.WIN_CLOSED or evento == "Exit" :
      break
    if evento == "Run":

      contatos = ['+5521979144103', '+5521980182223']
      for i in range(6):
            print(i)
            for n in contatos:
                 pywhatkit.sendwhatmsg(n, "Olá, sou o RenegadeBot", datetime.now().hour, datetime.now().minute + 1)
            else:
                 print("Todos os nomes foram listados com sucesso")
      keyboard.press_and_release("ctrl + w")

        
print("Rodando")
janela.close()