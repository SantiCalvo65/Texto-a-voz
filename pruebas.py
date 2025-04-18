import pyttsx3 as py
import time
import urllib.request

# Funcion para pedir el texto 
def obtener_texto():
    texto = input(str("Introduzca el texto a convertir en voz: "))
    return texto

# Funcion para reproducir el audio
def reproducir_audio(texto):
    engine = py.init()
    engine.say(texto)
    engine.runAndWait()

# Funcion para pedir una URL
def pedir_url():
    url = input("Ingrese una URL: ")
    try: # Verificamos la url
        response = urllib.request.urlopen(url)
        contenido = response.read().decode('utf-8')
        return contenido
        
    except: # Si no es valida mostramos este mensaje
        print("No se pudo acceder a la URL. Verifíquela e intente de nuevo.")               

bucle = True
while bucle: # Inicializamos el programa y pedimos que elijan una opcion.
    print(
            "Bienvenido al programa Texto_a_voz \n" \
            "1. Convertir un texto a voz.\n" \
            "2. Convertir el texto de URL introducida a voz.\n" \
            "3. Salir del programa"
            )
    
    # Solicitamos la opción a utilizar
    opcion = input("Introduzca una opción (1, 2, 3): ")
    
    # Si la opcion es 1, convertimos un texto introducido a voz
    if opcion == "1":
                    reproducir_audio(obtener_texto())

    # Pedimos una URL y la transformamos a voz
    elif opcion == "2":
                   reproducir_audio(pedir_url())

    # Opcion para salir del programa
    elif opcion == "3":
                    print("Cerrando el programa")
                    time.sleep(1)
                    print("Adios!")
                    bucle = False


