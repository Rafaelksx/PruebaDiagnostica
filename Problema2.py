import re

def analizar_fen(fen):
    # Definición de nombres para las secciones de FEN
    campos = ["Tablero", "Turno", "Enroque", "Peón al paso", "Medio movimiento", "Movimiento total"]
    # split para separar los campos de la cadena FEN, se espera que haya exactamente 6 campos según el formato estándar.
    partes = fen.split()
    
    # 1. Validación inicial de estructura
    if len(partes) != 6:
        return f"ERROR: La cadena FEN debe tener 6 campos, se encontraron {len(partes)}."

    detalles = []
    es_valido = True

    # 2. Análisis detallado campo por campo
    tablero, turno, enroque, al_paso, medio, total = partes

    # Validación de Filas (Tablero)
    filas = tablero.split('/')
    if len(filas) == 8:
        detalles.append(f" Tablero: {len(filas)} filas detectadas correctamente.")
    else:
        detalles.append(f" Tablero: Se esperaban 8 filas, se encontraron {len(filas)}.")
        es_valido = False

    # Validación de Turno
    if turno in ['w', 'b']:
        color = "Blancas" if turno == 'w' else "Negras"
        detalles.append(f" Turno: Juegan las {color}.")
    else:
        detalles.append(f" Turno: Valor inválido '{turno}' (debe ser 'w' o 'b').")
        es_valido = False

    # Validación de Enroque
    if re.match(r'^(([KQkq]+)|-)$', enroque):
        desc = "Ninguno" if enroque == "-" else enroque
        detalles.append(f"✅ Enroque: Disponibilidad -> {desc}.")
    else:
        detalles.append(f"❌ Enroque: Formato inválido '{enroque}'.")
        es_valido = False

    # Validación de Peón al paso
    if re.match(r'^([a-h][36]|-)$', al_paso):
        detalles.append(f" Peón al paso: {al_paso}.")
    else:
        detalles.append(f" Peón al paso: Coordenada inválida '{al_paso}'.")
        es_valido = False

    # Validación de Contadores (Numéricos)
    if medio.isdigit() and total.isdigit():
        detalles.append(f" Reloj: {medio} medios movimientos / Turno nro {total}.")
    else:
        detalles.append(" Contadores: Los últimos dos campos deben ser números enteros.")
        es_valido = False

    # Resultado Final
    print("\n--- ANÁLISIS DE NOTACIÓN FEN ---")
    for d in detalles:
        print(d)
    
    return "\nESTADO FINAL: FEN VÁLIDO" if es_valido else "\nESTADO FINAL: FEN INVÁLIDO"

# Ejemplo de prueba (Posición inicial)
test_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# Para probar paso a paso, primero tenemos que en la cadena Fen primero va el tablero, luego el turno,
# después el enroque, el peón al paso, el medio movimiento y finalmente el movimiento total.
# En este caso, el tablero es el estándar de inicio, el turno es para las blancas, el enroque está disponible para ambos lados,
# no hay peón al paso, el medio movimiento es 0 y el movimiento total es 1.

print(analizar_fen(test_fen))