import os
import time
from pynput.keyboard import Key, Controller
from pywinauto import application

keyboard = Controller()

def OpenWhatsappDesktop():
    try:
        os.startfile(r'C:\Users\luiz\AppData\Local\WhatsApp\WhatsApp.exe')
    except Exception as e:
        print(e)


def CloseWhatsappDesktop():
    try:
        os.system('TASKKILL /F /IM WhatsApp.exe')
    except Exception as e:
        print(e)


def SearchGroup(nome):
    try:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(3)

        keyboard.type(nome)
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
    except Exception as e:
        print(e)


OpenWhatsappDesktop()
time.sleep(10)

groups = ['Eu Sozinho', 'Teste Python']
for group in groups:
    SearchGroup(group)
    horaatual = time.strftime('%d-%b-%Y %X')
    #paste the image copied to memory before the program was started
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(1)
    keyboard.type(f'Teste de bot em Python via Whatsapp DeskTop, {horaatual}.')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


time.sleep(1)
CloseWhatsappDesktop()