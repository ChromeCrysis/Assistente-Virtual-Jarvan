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
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt")
                    print("Você disse: {}".format(entrada))

                    """abrir_programas = abre_programas()
                    voz_jarvan("{}".format(abrir_programas))"""

                    """resposta = conversas[entrada]
                    print("Jarvan {}".format(resposta))
                    voz_jarvan("{}".format(resposta))"""

                    comando = comandos[entrada]
                    print("Jarvan {}".format(comando))
                    voz_jarvan("{}".format(comando))
                    comando = exit()

                except sr.UnknownValueError:
                    print(resposta_erro_aleatoria)
                    voz_jarvan(resposta_erro_aleatoria)

if __name__ == "__main__":
    voz_jarvan("Inciando o sistema")
    introducao()
    apresentacao()
    Jarvan()