import random

# Juego de adivinar el número
def adivina_numero():
    # Generar un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1,10)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Adivina el número secreto entre 1 y 10. Escribe 'exit' para salir.")

    while True:
        # Pedir la entrada del usuario
        entrada = input("Introduce un número o 'exit' para salir: ")

        # Verificar si el usuario desea salir
        if entrada.lower() == "exit":
            print("Has salido del juego. ¡Hasta la próxima!")
            break

        # Intentar convertir la entrada a un número
        try:
            adivinanza = int(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Contar el intento
        intentos += 1

        # Comparar la adivinanza con el número secreto
        if intentos < 3:
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print("Ya no tienes mas intentos")
                break
          
        if adivinanza == numero_secreto:
            print("Has adivinado el numero secreto.")   
            break     


# Piedra-papel-tijeras

def piedra_papel_tijeras():
    
    # Inicializamos variables de puntos
    puntos_jugador=0
    puntos_maquina=0
    
    while puntos_jugador < 3 or puntos_maquina < 3:
        
        opciones = ["Piedra", "Papel", "Tijera"]
        # El jugador elige una de las 3 opciones que tiene
        jugador = input("Escoge piedra papel o tijera: ")
        
        while jugador.lower() not in opciones:
            print("No existe esa opción en este juego, intentelo de nuevo")
            jugador = input("Escoge piedra papel o tijera: ")
        
        # Para la maquina damos opciones y la escoge de forma random
        maquina = random.choice(opciones)
        
        # Barajamos todas las opciones para ganar y empatar
        if jugador.lower() == "papel" and maquina.lower() == "tijera":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado la máquina")
            puntos_maquina +=1           
            print(f"Las puntuaciones van asi: {puntos_jugador}:{puntos_maquina}")
            
        elif jugador.lower() == "tijera" and maquina.lower() == "papel":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado el jugador")
            puntos_jugador +=1            
            print(f"Las puntuaciones van asi: {puntos_jugador}:{puntos_maquina}")
            
        elif jugador.lower() == "tijera" and maquina.lower() == "piedra":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado la máquina")
            puntos_maquina +=1            
            print(f"Las puntuaciones van asi: {puntos_jugador}:{puntos_maquina}")
            
        elif jugador.lower() == "piedra" and maquina.lower() == "tijera":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado el jugador")
            puntos_jugador +=1            
            print(f"Las puntuaciones van asi: {puntos_jugador}:{puntos_maquina}")  
            
        elif jugador.lower() == "papel" and maquina.lower() == "piedra":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado el jugador")
            puntos_jugador +=1           
            print(f"Las puntuaciones van asi {puntos_jugador}:{puntos_maquina}") 
                
        elif jugador.lower() == "piedra" and maquina.lower() == "papel":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Ha ganado la máquina")
            puntos_maquina +=1            
            print(f"Las puntuaciones van asi {puntos_jugador}:{puntos_maquina}")
            
        elif jugador.lower() == "piedra" and maquina.lower() == "piedra":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Es un empate")            
            print(f"Las puntuaciones van asi {puntos_jugador}:{puntos_maquina}")
            
        elif jugador.lower() == "papel" and maquina.lower() == "papel":
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Es un empate")        
            print(f"Las puntuaciones van asi {puntos_jugador}:{puntos_maquina}")
            
        else:
            print(f"El jugador a sacado {jugador} y la maquina ha sacado {maquina}")
            print("Es un empate")
            print(f"Las puntuaciones van asi {puntos_jugador}:{puntos_maquina}")
        
        
        # Comprobamos las puntuaciones
        if puntos_jugador == 3:
            print(f"El jugador a ganado, {puntos_jugador} a {puntos_maquina}")  
            break
        elif puntos_maquina == 3:
            print(f"La máquina a ganado, {puntos_maquina} a {puntos_jugador}")
            break



# AHORCADO     
# Función para obtener la palabra el txt
def obtener_palabra_txt(nombre_archivo):
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        contenido = archivo.read().replace(',', ' ').replace('\n', ' ')  # Reemplaza comas y saltos de línea por espacios en blanco
        palabras = contenido.split()
    return random.choice(palabras)

# Función para mostrar el estado actual del juego
def mostrar_juego(palabra, letras_correctas):
    for letra in palabra:
        if letra in letras_correctas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

# Función para obtener la letra ingresada por el usuario
def obtener_letra():
    while True:
        letra = input("Introduce una letra: ")
        if len(letra) == 1 and letra.isalpha():
            return letra.lower()
        else:
            print("Entrada inválida. Por favor, introduce una letra válida.")

# Función para ejecutar un turno del juego
def turno(palabra, letras_correctas, letras_incorrectas, intentos):
    mostrar_juego(palabra, letras_correctas)
    letra = obtener_letra()
    
    if letra in letras_correctas or letra in letras_incorrectas:
        print("Ya has introducido esa letra. Inténtalo de nuevo.")
        return intentos
    
    if letra in palabra:
        letras_correctas.add(letra)
        print("Letra correcta.")
    else:
        letras_incorrectas.add(letra)
        intentos -= 1
        print("Letra incorrecta. Tienes", intentos, "intentos.")
    
    return intentos

# Función para verificar si el jugador ha ganado el juego
def verificar_victoria(palabra, letras_correctas):
    for letra in palabra:
        if letra.lower() not in letras_correctas:
            return False
    return True

def ahorcado():
    print("¡Bienvenido/a al juego del ahorcado!")
    palabra = obtener_palabra_txt('ahorcado.txt')
    letras_correctas = set()
    letras_incorrectas = set()
    intentos_restants = len(palabra)*2
    while intentos_restants > 0:
        intentos_restants = turno(palabra, letras_correctas, letras_incorrectas, intentos_restants)
        if verificar_victoria(palabra, letras_correctas):
            print("¡Has ganado! La palabra era: ", palabra)
            return
        else:
            print("Letras usadas:", " ".join(letras_incorrectas), " ".join(letras_correctas))
            print("Letras restantes: ")
    print("Has perdido. La palabra era", palabra)
           
            
            
            
# Menu principal del juego
def menu_principal():
    # Ponemos el menu con las opciones para el jugador
    print("Bienvenido a tu Gameroom, estos son los juegos disponibles")
    print("1. Adivina el número")
    print("2. Piedra-Papel-Tijeras")
    print("3. Ahorcado")
    print("4. Salir")
    
    # Variable para guardan la opción del jugador
    opcion = input("Pon el número del juego que quieres jugar: ")
    
    while opcion != "4":
        if opcion == "1":
            adivina_numero()
            print("1. Adivina el número")
            print("2. Piedra-Papel-Tijeras")
            print("3. Penjat")
            print("4. Salir")
            opcion = input("Pon el número del juego que quieres jugar o salir: ")
        elif opcion == "2":
            piedra_papel_tijeras()
            print("1. Adivina el número")
            print("2. Piedra-Papel-Tijeras")
            print("3. Penjat")
            print("4. Salir")
            opcion = input("Pon el número del juego que quieres jugar o salir: ")
        elif opcion == "3":
            ahorcado()
            print("1. Adivina el número")
            print("2. Piedra-Papel-Tijeras")
            print("3. Penjat")
            print("4. Salir")
            opcion = input("Pon el número del juego que quieres jugar o salir: ")


menu_principal()
        