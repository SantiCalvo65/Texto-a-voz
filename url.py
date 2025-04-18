import pyttsx3 as py
import time
import urllib.request



url = input("Ingrese una URL: ")
response = urllib.request.urlopen(url)
contenido = response.read().decode('utf-8')

print(contenido)


