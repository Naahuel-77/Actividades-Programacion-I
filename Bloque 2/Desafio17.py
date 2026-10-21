import random
import time

def simulacion_carrera():
    print("=== ¡COMIENZA LA CARRERA DE AUTOS (10 SEGUNDOS) ===\n")
    
    # 1. Creamos los autos y arrancan todos en la distancia 0
    # Usamos un diccionario: 'Nombre del auto': distancia_recorrida
    autos = {
        "Auto Rojo": 0,
        "Auto Azul": 0,
        "Auto Verde": 0,
        "Auto Amarillo": 0
    }
    
    # 2. El bucle principal: simula los 10 segundos de la carrera
    for segundo in range(1, 11):
        print(f"--- Segundo {segundo} ---")
        
        # En cada segundo, cada auto calcula su velocidad aleatoria y avanza
        for auto in autos:
            # Generamos una velocidad aleatoria entre 10 y 30 metros por segundo
            velocidad = random.randint(10, 30)
            
            # Sumamos esa velocidad a la distancia acumulada del auto
            autos[auto] += velocidad
            
            # Mostramos cuánto avanzó en este segundo
            print(f"{auto} viajó a {velocidad} m/s | Distancia total: {autos[auto]} metros")
        
        print("-" * 50)
        time.sleep(0.5)  # Una pequeña pausa de medio segundo para darle emoción en la consola
    
    # 3. Terminó la carrera. Buscamos cuál es la distancia máxima alcanzada
    # max(autos.values()) nos da el número más alto de los metros recorridos
    distancia_maxima = max(autos.values())
    
    # 4. Buscamos quién o quiénes alcanzaron esa distancia máxima (por si hay empate)
    ganadores = []
    for auto, distancia in autos.items():
        if distancia == distancia_maxima:
            ganadores.append(auto)
            
    # 5. Mostramos los resultados finales
    print("\n" + "="*40)
    print("¡FIN DE LA CARRERA! RESULTADOS:")
    print("="*40)
    
    # Si hay más de un auto en la lista de ganadores, es un empate
    if len(ganadores) > 1:
        print(f"¡Tenemos un EMPATE en el primer puesto con {distancia_maxima} metros!")
        print("Los ganadores son:")
        for g in ganadores:
            print(f"🏆 {g}")
    else:
        # Si hay uno solo, hay un único ganador contundente
        print(f"🏆 ¡El GANADOR es el {ganadores[0]} con {distancia_maxima} metros! 🏆")
        
    print("="*40)

# Ejecutamos la simulación
simulacion_carrera()