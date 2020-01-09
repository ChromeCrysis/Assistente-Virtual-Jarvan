#Synthesis
import pyttsx3

reproducao = pyttsx3.init()

version = "0.1.1"
def introducao():
    msg = "Jarvan - version {} | criada por: Anderson Bechelli".format(version)
    print("-"*len(msg) + "\n{}\n".format(msg) + "-"*len(msg))

def apresentacao():
    print("Meu nome é Jarvan, sou o assistente pessoal do Sr.Bechelli. Por favor diga alguma coisa para eu processar.")          
    voz_jarvan("Meu nome é Jarvan, sou o assistente pessoal do Sr.Bechelli. Por favor diga alguma coisa para eu processar.")         

def voz_jarvan(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def verifica_nome_usuario(usuario):
    if usuario.startswitch("Meu nome é"):
        usuario = usuario.replace("Meu nome é", "")
    
    return usuario

def verificar_nome_existe(nome):
    dados = open("dados/nomes.txt", "r")
    lista_nomes = dados.readlines()

    if not lista_nomes:
        vazio = open("dados/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append("\n{}".format(nome))
        vazio = open("dados/nomes.txt", "w")
        vazio.writelines(contetudo)
        vazio.close()

        return "Olá {}, prazer em te conhecer".format(nome)
    for linha in lista_nomes:
        if linha == nome:
            return "Olá {}, acho que já nos conhecemos".format(nome)

    vazio = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    vazio = open("dados/nomes.txt", "w")
    vazio.writelines(contetudo)
    vazio.close()

def abre_programas():
            try:
                lolzin = open("C:\Riot Games\League of Legends\LeagueClient.exe")
                chrome = open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                if entrada == "abrir league of legends":
                    voz_jarvan("Abrindo League of Legends")
                    return lolzin
                if entrada == "abrir google chrome":
                    voz_jarvan("Abrindo Google Chrome")
                    return chrome
            except FileNotFoundError:
                voz_jarvan("Não foi Possivel abrir o arquivo solicitado.")
                lolzin = open("C:\Riot Games\League of Legends\LeagueClient.exe")
                chrome = open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                lolzin.close()
                chrome.close()
    

lista_erros = [
    "Não entendi, por favor repita novamente.",
    "Desculpe, não consegui entender nada do que disse.",
    "Repita novamente, meus sensores de áudio devem estar com defeito",
    "Não entendi, por favor verifique o microfone e fale novamente."
]

conversas = {
    "Olá": "Oi, tudo bem?",
    "sim e você": "Estou bem, obrigado por perguntar",
    "Qual é o seu nome" : "Meu nome é Jarvan, prazer em conhecê-lo"
}

comandos = {
    "desligar": "desligando",
    "reiniciar": "reiniciando",
    "Abrir sequência de comandos" : "entendido Sr.Bechelli, abrindo sequência de comandos",
}