import os, json, time
from pynput.keyboard import Key, Controller
from pywinauto import application

keyboard = Controller()


def OpenWhatsappDesktop():
    """Open the Whastapp desktop application. Change the path before use."""
    try:
        os.startfile(r'C:\Users\luiz\AppData\Local\WhatsApp\WhatsApp.exe')
    except Exception as e:
        print(e)


def CloseWhatsappDesktop():
    """Close the Whatsapp Desktop application"""
    try:
        os.system('TASKKILL /F /IM WhatsApp.exe')
    except Exception as e:
        print(e)


def SearchGroup(nome):
    """Search for the group name"""
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


def OpenJson():
    """Open json file with the Group Name and its Message and retur as a dict"""
    # Path to Json
    CWD = os.getcwd()
    JSON_PATH = '%s/%s' % (CWD, 'lista_mensagens.json')
    # Dictionary holding the groups and messages values
    msgs = {}
    # Open json and store to Dictionary
    with open(JSON_PATH) as data_file:
        msgs = json.load(data_file)
    return(msgs)


lista = OpenJson()
for grupos in lista['lista_mensagens']:
    print(grupos['grupo'], ' - ', grupos['mensagem'])

OpenWhatsappDesktop()
time.sleep(30)

for grupos in lista['lista_mensagens']:
    SearchGroup(grupos['grupo'])
    
    #paste the image copied to memory before the program was started
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(3)
    #type de mesage and send it
    m = grupos['mensagem']
    horaatual = time.strftime('%d-%b-%Y %X')
    keyboard.type(f'{m}. Hora de Envio: {horaatual}.')
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)


time.sleep(1)
CloseWhatsappDesktop()
