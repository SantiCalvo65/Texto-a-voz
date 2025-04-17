import pyttsx3 as py
import time

bucle = True
while bucle:
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
                    # Funcion para pedir el texto al usuario
                    def obtener_texto():
                        texto = input(str("Introduzca el texto a convertir en voz: "))
                        return texto

                    # Funcion para reproducir el audio
                    def reproducir_audio():
                        engine.say(obtener_texto())
                        engine.runAndWait()

                    # Se inicia el motor de voz
                    engine = py.init()

                    # Reproducimos el audio
                    reproducir_audio()

    if opcion == "3":
                    print("Cerrando el programa")
                    time.sleep(1)
                    print("Adios!")
                    bucle = False
                    
           