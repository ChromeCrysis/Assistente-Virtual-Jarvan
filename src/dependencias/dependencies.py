import os
import sys

print("Antes de começar instale a versão do Python 3.6.")
print("Olá, sou o instalador de dependencias do Jarvan. Para funcionar, Jarvan precisa de algumas dependências.")
print("Essas dependências são: \nPyAudio.\nSpeechRecognition.\nPyttsx3.")
print("Deseja instalar as dependências?")
confirmacao = str(input('Digite S para Sim e N para Não:'))
if confirmacao == N:
    print("Entendido, não será instalado nada.") 
    #exit()
else:
    os.system("pip install PyAudio")
    os.system("pip install SpeechRecognition")
    os.system("pip install pyttsx3")