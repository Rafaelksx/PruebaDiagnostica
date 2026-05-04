# Problema 3: Conjetura de Collatz en un Intervalo
# Se debe verificar la conjetura en un rango [p, q], asegurando que q >= 100p.

def verificar_collatz(p, q):
    # Regla: q >= 100p 
    if q < 100 * p:
        return "Error: No se cumple la regla q >= 100p"
    
    #Verificación de la conjetura para cada número en el intervalo [p, q] 
    for n in range(p, q + 1):
        actual = n
        secuencia = [str(actual)]
        while actual != 1:
            if actual % 2 == 0:
                actual //= 2
            else:
                actual = 3 * actual + 1
            secuencia.append(str(actual))
        print(f"n={n}: {' -> '.join(secuencia)}")
    
    return "Demostrado para el intervalo."

# Ejemplo de uso [cite: 20]
verificar_collatz(1, 100)