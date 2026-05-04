import re


# Este problema requiere clasificar componentes de una cadena. 
# Utilizaremos Expresiones Regulares (Regex) para identificar cada token según las reglas: números reales/enteros sin signo, operandos que no inicien con números, y operadores básicos.

def analizar_expresion(cadena):
    # Definición de patrones según las reglas del enunciado 
    patrones = [
        ('NUMERO', r'\d+(\.\d+)?'),           # Enteros o reales con "." 
        ('OPERADOR', r'[\+\-\*/]'),           # + - * / 
        ('PAREN_IZQ', r'\('),
        ('PAREN_DER', r'\)'),
        ('OPERANDO', r'[a-zA-Z_][a-zA-Z0-9_]*'), # No inicia con número, sin espacios
        ('ESPACIO', r'\s+'),
    ]
    
    tokens_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patrones)
    resultado = []
    parentesis = 0
    error = False

    for match in re.finditer(tokens_regex, cadena):
        tipo = match.lastgroup
        valor = match.group(tipo)
        
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'PAREN_IZQ':
            parentesis += 1
        elif tipo == 'PAREN_DER':
            parentesis -= 1
        
        resultado.append(f"{tipo} {valor}")

    # Validación de balance de paréntesis [cite: 14]
    balance = "PARÉNTESIS BALANCEADOS" if parentesis == 0 else "PARÉNTESIS NO BALANCEADOS"
    return " ".join(resultado) + f" {balance}"

# Ejemplo de uso [cite: 12]
print(analizar_expresion("13-3*(4)"))