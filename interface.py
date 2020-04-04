def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n


def linha(tam=75):
    return '-' * tam


def header(titulo):
    print (linha())
    print ((f'\033[33m{titulo}\033[m').center(75))
    print (linha())


def menu(lista):
    header('Controle de Mensagens por Whatsapp')
    c = 1
    for item in lista:
        print (f'{c} - {item}')
        c += 1
    print (linha())
    opc = leiaint('Opção : ')
    return opc
