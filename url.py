import pyttsx3 as py
import time
import urllib.request

def obtener_texto():
    texto = input(str("Introduzca el texto a convertir en voz: "))
    return texto

# Función para reproducir el audio
def reproducir_audio_texto():
    engine = py.init()
    engine.say(obtener_texto())
    engine.runAndWait()

# Función para pedir una URL
def pedir_url():
    url = input("Ingrese una URL: ")
    try:
        response = urllib.request.urlopen(url)
        contenido = response.read().decode('utf-8')

        engine = py.init()
        engine.say("Leyendo los primeros caracteres del contenido de la URL")
        engine.say(contenido[:300])  # Podés ajustar la cantidad de texto
        engine.runAndWait()
    except:
        print("⚠️ No se pudo acceder a la URL. Verifíquela e intente de nuevo.")

# Bucle principal
bucle = True
while bucle:
    print(
        "\nBienvenido al programa Texto_a_voz\n" \
        "1. Convertir un texto a voz.\n" \
        "2. Convertir el texto de URL introducida a voz.\n" \
        "3. Salir del programa"
    )

    opcion = input("Introduzca una opción (1, 2, 3): ")

    if opcion == "1":
        reproducir_audio_texto()
    elif opcion == "2":
        pedir_url()
    elif opcion == "3":
        print("Cerrando el programa...")
        time.sleep(1)
        print("¡Adiós!")
        bucle = False
    else:
        print("⚠️ Opción no válida. Intente con 1, 2 o 3.")

