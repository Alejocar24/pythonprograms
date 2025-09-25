from sympy import symbols, SOPform

# ===========================
# Programa para simplificar funciones booleanas con símbolos matemáticos
# ===========================

# Función auxiliar para imprimir con símbolos
def bool_to_math(expr):
    expr_str = str(expr)

    # Reemplazo de negación: ~X -> X̅
    for var in expr.free_symbols:
        expr_str = expr_str.replace(f"~{var}", f"{var}̅")

    # Reemplazo de AND y OR
    expr_str = expr_str.replace("&", "·")  # AND -> multiplicación
    expr_str = expr_str.replace("|", "+")  # OR -> suma lógica

    return expr_str


# Pedir número de entradas
n = int(input("Ingrese el número de entradas del sistema: "))

# Crear las variables (A, B, C, ... según n)
variables = symbols(" ".join([chr(65+i) for i in range(n)]))

# Pedir minterminos
minterms = list(map(int, input("Ingrese los minterminos separados por comas: ").split(",")))

# Generar la función simplificada
f_simplificada = SOPform(variables, minterms)

# Mostrar resultados
print("\n=========================================")
print("Número de variables:", n)
print("Minterminos:", minterms)
print("Función simplificada (símbolos Python):")
print(f_simplificada)
print("\nFunción simplificada (símbolos matemáticos):")
print(bool_to_math(f_simplificada))
print("=========================================")
