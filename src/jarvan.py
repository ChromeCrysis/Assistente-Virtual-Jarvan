#Speech Recognition
import speech_recognition as sr
#Synthesis
import pyttsx3
#Choices
from random import choice
#Configurações do Jarvan
from config import *

def Jarvan():
    print("Ouvindo...")

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    usuario = "Sr.Bechelli"
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt").lower()
                    print("{}: {}".format(usuario,entrada))

                    #Abre comandos especificos
                    if "abrir sequência de comandos" in entrada:
                        resposta = comandos(entrada)

                    #Abre programas
                    elif "abrir" in entrada:
                        resposta = abrir(entrada)

                    #Pesquisa na web
                    elif "pesquisar" in entrada:
                        reposta = pesquisar(entrada)

                    #Entrada de cálculos matemáticos
                    elif "calcular" in entrada:
                        if "quanto é" in entrada:
                            entrada = entrada.replace("quanto é", "")
                            resposta = calcula(entrada)
                            print("Jarvan: {}".format(resposta))
                            voz_jarvan(resposta)
                        else:
                            resposta = "Operação Inválida."
                            voz_jarvan(resposta)
                    else:
                        resposta = conversas[entrada]
                        print("Jarvan: {}".format(resposta))
                        voz_jarvan("{}".format(resposta))

                    """comando = comandos[entrada]
                    print("Jarvan {}".format(comando))
                    voz_jarvan("{}".format(comando))"""

                except sr.UnknownValueError:
                    print(resposta_erro_aleatoria)
                    voz_jarvan(resposta_erro_aleatoria)
                except:
                    pass

#Executa o sistema do Jarvan e os métodos do config.py
if __name__ == "__main__":
    voz_jarvan("Inciando o sistema")
    introducao()
    apresentacao()
    Jarvan()