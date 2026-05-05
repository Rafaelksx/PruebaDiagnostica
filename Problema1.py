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

    # Procesamiento de la cadena utilizando el regex combinado, la función finditer nos permite iterar sobre
    # cada coincidencia y clasificarla según el tipo de token identificado.
    for match in re.finditer(tokens_regex, cadena):

        # Cada coincidencia se clasifica según el grupo que haya sido identificado por el regex,
        # y se maneja el conteo de paréntesis para validar su balance.
        tipo = match.lastgroup

        # El valor del token se extrae utilizando 
        # el grupo correspondiente al tipo identificado.
        valor = match.group(tipo)
        
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'PAREN_IZQ':
            parentesis += 1
        elif tipo == 'PAREN_DER':
            parentesis -= 1
        
        resultado.append(f"{tipo} {valor}")

    # Validación de balance de paréntesis 
    balance = "PARÉNTESIS BALANCEADOS" if parentesis == 0 else "PARÉNTESIS NO BALANCEADOS"
    return " ".join(resultado) + f" {balance}"

# Ejemplo de uso 
# La corrida en frío, para representar como funciona paso a paso es la siguiente:
# 1. Se define la cadena "13-3*(4)".
# 2. finditer encuentra al tipo NUMERO con valor "13", luego el OPERADOR "-", seguido por otro NUMERO "3", el OPERADOR "*",
# el PAREN_IZQ "(", otro NUMERO "4" y finalmente el PAREN_DER ")".
# 3. Se verifica el balance de paréntesis, que en este caso es correcto
# 4. El resultado final es una cadena que clasifica cada token y confirma que los paréntesis están balanceados.
print(analizar_expresion("13-3*(4)"))