#Speech Recognition
import speech_recognition as sr
#Synthesis
import pyttsx3
#OS
import os
import sys
#Web Browser para abrir páginas web
import webbrowser as web
from jarvan import Jarvan

reproducao = pyttsx3.init()

version = "0.1.1"
path_navegador = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
path_lol = 'C:\Riot Games\League of Legends\LeagueClient.exe'

#Introdução do Sistema 
def introducao():
    msg = "Jarvan - version {} | criada por: Anderson Bechelli".format(version)
    print("-"*len(msg) + "\n{}\n".format(msg) + "-"*len(msg))

#Apresentação do Jarvan
def apresentacao():
    print("Meu nome é Jarvan, sou o assistente pessoal do Sr.Bechelli. Por favor diga alguma coisa para eu processar.")
    voz_jarvan(
        "Meu nome é Jarvan, sou o assistente pessoal do Sr.Bechelli. Por favor diga alguma coisa para eu processar.")

#Método de configuração da Synthesis de voz
def voz_jarvan(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

#Método de operações matemáticas simples utilizando sistema de decisão
def calcula(entrada):
    if "mais"in entrada or "+" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = int(entradas_recebidas[2]) + int(entradas_recebidas[4])

    elif "menos" in entrada or "-" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = int(entradas_recebidas[2]) - int(entradas_recebidas[4])
    
    elif "vezes" in entrada or "x" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = round(float(entradas_recebidas[2]) * float(entradas_recebidas[4]), 2)

    elif "divido" in entrada or "/" in entrada:
        entradas_recebidas = entrada.split(" ")
        resultado = round(float(entradas_recebidas[2]) / float(entradas_recebidas[4]), 2)
    else:
        resultado = "Operação matemática não encontrada"
        voz_jarvan(resultado)

    return resultado

#Método de abertura de programas
def abrir(fala):
    try:
        if "league of legends" in fala:
            os.startfile(path_lol)
            resultado = "abrindo League of Legends"
            voz_jarvan(resultado)
        elif "google chrome" in fala:
            os.startfile(path_navegador)
            resultado = "abrindo google"
            voz_jarvan(resultado)
        else:
            return "Não foi possível abrir o arquivo, por favor tente novamente."
    except:
        return "Houve um erro no comando de abertura de arquivo."

#Método de pesquisa na Web
def pesquisar(fala):
    try:
        if "facebook" in fala:
            web.open("facebook.com.br/")
            resultado = "abrindo facebook"
            voz_jarvan(resultado)
        elif "repositórios" in fala:
            web.open("github.com")
            resultado = "abrindo Github"
            voz_jarvan(resultado)
        else:
            return "Página não encontrada, por favor tente novamente."
    except:
        return "Houve um erro no comando de pesquisa."

#Método em desenvolvimento
def fechar_programas(fala):
    try:
        if "fechar" in fala:
            resultado = "Fechando"
            voz_jarvan(resultado)
    except:
        return "Houve um erro para executar o comando de fechamento."
#Método em desenvolvimento
def comandos(fala):
    try:
        voz_jarvan("Abrindo sequência de comandos.")
        if "desligar" in fala:
            resultado = "Desligando"
            voz_jarvan(resultado)
        else:
            return "Este comando não está disponível, por favor tente novamente."
    except:
        return "Houve um erro para executar a sequência de comandos."

#Lista de erros caso Jarvan não entenda o que disse
lista_erros = [
    "Não entendi, por favor repita novamente.",
    "Desculpe, não consegui entender nada do que disse.",
    "Repita novamente, meus sensores de áudio devem estar com defeito",
    "Não entendi, por favor verifique o microfone e fale novamente."
]

#Dicionário de conversas tradicionais com Jarvan
conversas = {
    "olá": "Oi, tudo bem?",
    "sim e você": "Estou bem, obrigado por perguntar",
    "qual é o seu nome": "Meu nome é Jarvan, prazer em conhecê-lo",
    "obrigado Jarvan": "É sempre um prazer Sr.Bechelli",
    "você é um gênio jarvan": "Obrigado Sr.Bechelli, é sempre bom ouvir elogios"
}

#Dicionário de comandos
comandos_dict = {
    "desligar": "desligando",
    "reiniciar": "reiniciando",
    "abrir sequência de comandos": "entendido Sr.Bechelli, abrindo sequência de comandos",
    "desejar feliz aniversário para o Alex": "Olá Alex, feliz aniversário, tenha um ótimo dia e que você seja sempre próspero e amigo do Sr.Bechelli.",
    "desejar um bom dia a todos do grupo": "Olá pessoal, desejo a todos um bom dia em meu nome e do Sr.Bechelli."
}
