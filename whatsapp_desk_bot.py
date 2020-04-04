import os, json, time
from time import sleep
from interface import *
from pynput.keyboard import Key, Controller
#from pywinauto import application

JSON_FILE_NAME = 'lista_mensagens.json'
keyboard = Controller()


def OpenWhatsappDesktop():
    """Open the Whastapp desktop application. Change the path before use."""
    try:
        os.startfile(r'C:\Users\luiz\AppData\Local\WhatsApp\WhatsApp.exe')
    except Exception as e:
        print(e)

def SendWhatsappMessage():
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
    JSON_PATH = '%s/%s' % (CWD, JSON_FILE_NAME)
    # Dictionary holding the groups and messages values
    msgs = {}
    # Open json and store to Dictionary
    with open(JSON_PATH) as data_file:
        msgs = json.load(data_file)
    return(msgs)

def AddtoJson(texto):
    """Open json file to add a new Group and Message to it"""
    # Path to Json
    CWD = os.getcwd()
    JSON_PATH = '%s/%s' % (CWD, JSON_FILE_NAME)
    # Dictionary holding the groups and messages values
    msgs = {}
    # Open json and store to Dictionary
    with open(JSON_PATH, 'w') as data_file:
        json.dump(texto, data_file, indent=4)

def Menu():
    while True:
        resposta = menu(['Exibir Lista de Grupos x Mensagem', 'Alterar Lista', 'Incluir Dados na Lista','Excluir Dados da Lista','Executar Robô','Sair'])
        if resposta == 1:
            header('Lista de Grupos e Mensagens')
            lista = OpenJson()
            n = 1
            for grupos in lista['lista_mensagens']:
                print(n, '-',grupos['grupo'], ' - ', grupos['mensagem'])
                n +=1
            sleep(5)
        
        elif resposta ==2:
            header ('Alterar Lista')
            print ("EM DESENVOLVIMENTO")
            sleep(2)
        
        elif resposta ==3:
            header ('Incluir Dados na Lista')
            msg = {}
            g = input('Nome do Grupo:')
            m = input('Mensagem:')
            msg = {"grupo":g,"mensagem":m}
            print(msg)
            print(type(msg))
            lista = OpenJson()
            
            with open (JSON_FILE_NAME) as json_file:
                data = json.load(json_file)
                temp = data['lista_mensagens']
                y = msg
                temp.append(y)
            AddtoJson(data)
            sleep(2)

        elif resposta ==4:
            header ('Excluir Dados da Lista')
            print ("EM DESENVOLVIMENTO")
            sleep(2)

        elif resposta ==5:
            header ('Executar Robô')
            sleep(2)
            OpenWhatsappDesktop()
            time.sleep(30)
            SendWhatsappMessage()
            time.sleep(1)
            CloseWhatsappDesktop()

        elif resposta == 6:
            header ('Saindo...')
            sleep(2)
            break

        else:
            print ('\033[31mERRO: Selecione uma opção válida!\033[m')
            sleep(2)

#adds the list of groups and messages to a global variable
lista = OpenJson()


Menu()

