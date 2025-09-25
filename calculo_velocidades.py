import math

# Constantes
rho = 1.29  # densidad del aire [kg/m^3]
A1 = 479.1e-6  # área 1 en m^2 (de mm^2 a m^2)
A2 = 126e-6    # área 2 en m^2 (de mm^2 a m^2)

# Pedir presiones
p1_kpa = float(input("Ingrese p1 en kPa: "))
p2_kpa = float(input("Ingrese p2 en kPa: "))

# Convertir a Pascales
p1 = p1_kpa * 1000
p2 = p2_kpa * 1000

# Fórmula de Bernoulli + continuidad
ratio = A1 / A2
delta_p = p1 - p2

v1 = math.sqrt((2 * delta_p) / (rho * (ratio**2 - 1)))
v2 = ratio * v1

# Resultados
print(f"v1 = {v1:.3f} m/s")
print(f"v2 = {v2:.3f} m/s")
