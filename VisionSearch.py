from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
import wikipedia
import google
import webbrowser
import pyperclip
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

speaker = pyttsx3.init('sapi5')
pyautogui.PAUSE = 1

lista_calculadora = ['Abrir calculadora', 'calculadora', 'abrir calculadora']

def Abrir():
        r = sr.Recognizer()
        with sr.Microphone()as source:
            r.adjust_for_ambient_noise(source)
            print('Qual programa você deseja abrir? ')
            speak('Qual programa você deseja abrir? ')
            audio = r.listen(source)
            programa = r.recognize_google(audio, language = 'pt')
            print('Você disse: ' + programa)
            
            if programa == "Abrir YouTube":
                    r = sr.Recognizer()
                    with sr.Microphone()as source:
                            r.adjust_for_ambient_noise(source)
                            print('Oque você deseja ouvir? ')
                            speak('Oque você deseja ouvir? ')
                            audio2 = r.listen(source)
                            x2 = r.recognize_google(audio2, language = 'pt')
                            pyautogui.press("win")
                            pyautogui.write("chrome")
                            pyautogui.press("enter")
                            pyautogui.write("youtube.com")
                            pyautogui.press("enter")
                            time.sleep(3)
                            pyautogui.click(779, 96, clicks=1)
                            pyautogui.write(x2)
                            pyautogui.press("enter")
                            time.sleep(2)
                            pyautogui.click(451, 493, clicks=1)
                
            if programa == "Abrir Google Chrome":
                    pyautogui.press("win")
                    pyautogui.write("chrome")
                    pyautogui.press("enter")
            
            if programa == "Abrir Word":
                    r = sr.Recognizer()
                    with sr.Microphone()as source:
                            r.adjust_for_ambient_noise(source)
                            print('Oque você deseja escrever? ')
                            speak('Oque você deseja escrever? ')
                            audio3 = r.listen(source)
                            x3 = r.recognize_google(audio3, language = 'pt')
                            pyautogui.press("win")
                            pyautogui.write("writer")
                            pyautogui.press("enter")
                            time.sleep(3)
                            pyautogui.write(x3)
                            time.sleep(5)
                            repeticao = "s"
                            while repeticao == "s":
                                    speak('Deseja escrever mais alguma coisa? ')
                                    audio3_resposta = r.listen(source)
                                    x3_resposta = r.recognize_google(audio3_resposta, language = 'pt')
                                    if x3_resposta == "sim":
                                            speak('Oque você deseja escrever? ')
                                            audio3_sim = r.listen(source)
                                            x4_sim = r.recognize_google(audio3_sim, language = 'pt')
                                            pyautogui.press("enter")
                                            pyautogui.write(x4_sim)
                                    else:
                                            speak('Trabalho finalizado com sucesso!')
                                            break                    
            if programa == "Abrir Excel":
                    pyautogui.press("win")
                    pyautogui.write("libreoffice calc")
                    pyautogui.press("enter")
                    
            for i in lista_calculadora:
                if programa in lista_calculadora:
                        pyautogui.press("win")
                        pyautogui.write("calculadora")
                        pyautogui.press("enter")
                        time.sleep(2)
                        break
                        exit
                
            if programa == "calculadora":
                    pyautogui.press("win")
                    pyautogui.write("calculadora")
                    pyautogui.press("enter")

            if programa == "Abrir Braille fácil":
                    pyautogui.press("win")
                    pyautogui.write("Braille Facil")
                    pyautogui.press("enter")
                    
            if programa == "abrir dosbox":
                    pyautogui.press("win")
                    pyautogui.write("Dosvox")
                    pyautogui.press("enter")

            if programa == "abrir nvda":
                    pyautogui.press("win")
                    pyautogui.write("nvda")
                    pyautogui.press("enter")        

            if programa == "Abrir Gmail":
                    pyautogui.press("win")
                    pyautogui.write("chrome")
                    pyautogui.press("enter")
                    pyautogui.write("gmail.com")
                    pyautogui.press("enter")
            
            if programa == "Abrir Outlook":
                    texto = "https://outlook.live.com/owa/"
                    pyautogui.press("win")
                    pyautogui.write("chrome")
                    pyautogui.press("enter")
                    pyperclip.copy(texto)
                    pyautogui.hotkey("ctrl", "v")
                    pyautogui.press("enter")
        
            if programa == "Abrir rádio":
                     pyautogui.press("win")
                     pyautogui.write("chrome")
                     pyautogui.press("enter")
                     pyautogui.write("radiosaovivo.net")
                     pyautogui.press("enter")
                     time.sleep(3)
                     pyautogui.click(435, 577, clicks = 1)

def setVoice(): #definição da voz padrão
        voices = speaker.getProperty('voices')
        for voice in voices:
            if voice.name == 'brazil':
                speaker.setProperty('voice', voice.id)
            
def speak(text):  #síntese da voz
    speaker.say(text)
    speaker.runAndWait()

setVoice() #setando a voz definida

r = sr.Recognizer() 
wikipedia.set_lang('pt')
keywords = ['quem é','o que é','quando foi', 'como foi','por que','quais sao','qual é','aonde fica'] #palavras chave para pesquisa
google_keywords = ['pesquisar por', 'pesquise por'] #palavras chave para pesquisa

def search_web(text): #definição do metodo de pesquisa na internet
    result = None
    if text is not None:
        for key in google_keywords:
            if text.startswith(key):
                result = text.replace(key, '')
        if result is not None:
            for url in searh(text, stop=2):
                webbrowser.open_new_tab(url) #metodo para abrir uma nova aba como resposta a requisição feita
                break
            return 'pesquisando por' + result.rstrip()
    return result

def answer(query):  #pegar a resposta
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return'Desculpe, não pude encontrar oque procura.' #mensagem de erro caso a requisição não seja encontrada

def evaluate(query):  #avaliar o comando
    for keyword in keywords:
        if query.startswith(keyword):
            return query.replace(keyword, '')
        else:
            return None

def Pesquisar():
        with sr.Microphone()as s:
            r.adjust_for_ambient_noise(s) #usar o microfone para receber a requisição
            print('Diga o que você procura: ')
            speak('Diga o que você procura: ')
            while True:
                audio = r.listen(s) 
                speech = r.recognize_google(audio) #usar sintetizador de voz do google para realizar a pesquisa
                result = evaluate(speech)
                print('Você disse: ' + r.recognize_google(audio, language = 'pt'))  
                
                if result == None:
                    ans = answer(speech) #devolver a resposta ao usuário
                    print(ans) #resposta em texto   
                    speak(ans) #resposta em voz)
                    response = search_web(speech) #resposta da requisição uma nova aba de pesquisa
                    repeticao2 = "s"
                    while repeticao2 == "s":
                            lista_pesquisar = ['pesquisar novamente', 'pesquisar denovo', 'pesquisar']
                            speak('Deseja repetir a resposta ou pesquisar novamente? ')
                            audio4_resposta = r.listen(s)
                            x4_resposta = r.recognize_google(audio4_resposta, language = 'pt')
                            for i in lista_pesquisar:
                                    if x4_resposta in lista_pesquisar:
                                            Pesquisar()
                                    elif x4_resposta == "repetir":
                                            print(ans)
                                            speak(ans)
                                    else:
                                        break
                                    
                else:
                    print("Desculpe, não conseguir entender!") #mensagem de erro caso a requisição não seja entendida adequadamente
                    speak("Desculpe, não conseguir entender!")

def inicio():                    
        lista_respostas = ['quero pesquisar', 'pesquisar', 'eu quero pesquisar']
        lista_respostas2 = ['abrir um programa', 'programa', 'quero abrir um programa', 'abrir o programa', 'eu quero abrir um programa']

        r = sr.Recognizer()
        with sr.Microphone()as source:
                r.adjust_for_ambient_noise(source) #usar o microfone para receber a requisição
                print('Oque você deseja?: ')
                speak('Oque você deseja?: ')
                audio = r.listen(source)
                resposta = r.recognize_google(audio, language = 'pt')
                print('Você disse: ' + resposta)

                for i in lista_respostas:
                        if resposta in lista_respostas:
                                Pesquisar()
                for i in lista_respostas2:
                        if resposta in lista_respostas2:
                                Abrir()

        
janela = Tk()
janela.title("Vision Search")
janela.geometry('670x470')
janela.resizable(width=False, height=False)
imagem = PhotoImage(file="imagem_sistema.png")
img_label = Label(janela, image = imagem)
img_label.place(x=0, y=0)
imagem_icone = PhotoImage(file="vision_search.png")
janela.iconphoto(False,imagem_icone)
imagem_botao = PhotoImage(file="gif_microfone2.png")
botao=Button(janela, image = imagem_botao, bd=0,relief=GROOVE,command = inicio(), width = 100, height = 100)
botao.place(x=135, y=90)

                       
janela.mainloop()
