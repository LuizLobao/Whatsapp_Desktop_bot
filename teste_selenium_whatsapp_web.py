from selenium import webdriver
import time

class whatsappbot:
    def __init__(self):
        self.mensagem = "teste de bot"
        self.grupos = ["Eu Sozinho","Cripto Traders"]
        option = webdriver.ChromeOptions()
        option.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    
    def EnviarMensagens(self):
        
        #<span dir="auto" title="Eu Sozinho" class="_19RFN _1ovWX _F7Vk">Eu Sozinho</span>
        #<span dir="auto" title="Cripto Traders" class="_19RFN _1ovWX _F7Vk">
        #<div tabindex="-1" class="_3FeAD _1PRhq">
        #<div tabindex="-1" class="_13mgZ"><div tabindex="-1" class="_3FeAD _1PRhq"><div class="wjdTm" style="visibility: visible;">Digite uma mensagem</div><div class="_3u328 copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-icon="send" class="">
        print('Iniciando o WhatsApp Bot')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            print (f'Buscando o grupo: {grupo}')
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chatbox.click()
            print ('Digitando Mensagem')
            chatbox.send_keys(self.mensagem)
            botao_enviar=self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            print ('Clicando para Enviar')
            botao_enviar.click()
            time.sleep(3)

bot = whatsappbot()
bot.EnviarMensagens()
