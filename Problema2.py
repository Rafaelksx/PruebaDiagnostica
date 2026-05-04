# Problema 2: Validador de Notación FEN (Ajedrez)
# La notación FEN describe una posición de ajedrez. Una cadena FEN válida debe tener 6 campos separados por espacios: disposición de piezas, turno, enroque, peón al paso, medio movimiento y número de movimiento.

import re
    
def es_fen_valido(fen):
    partes = fen.split()
    if len(partes) != 6:
        return False
    
    tablero, turno, enroque, al_paso, medio, total = partes
    
    # 1. Validar filas del tablero (deben ser 8)
    filas = tablero.split('/')
    if len(filas) != 8:
        return False
        
    # 2. Validar turno
    if turno not in ['w', 'b']:
        return False
        
    # 3. Validar enroque
    if not re.match(r'^(([KQkq]+)|-)$', enroque):
        return False
        
    return True

# Ejemplo: Posición inicial
print(es_fen_valido("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))