import matplotlib.pyplot as plt
import numpy as np

# ==========================
# Datos
# ==========================
x = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
y = [0.00286,0.00511,0.00695,0.00799,0.00946,0.01015,0.01093,0.01139]

plt.scatter(x, y, color='blue')

# ==========================
# Línea de tendencia 
# ==========================
grado = 1  # cámbialo según quieras probar
coef = np.polyfit(x, y, grado)
polinomio = np.poly1d(coef)

# Puntos para graficar suavizado
num = np.linspace(min(x), max(x), 200)
plt.plot(num, polinomio(num), color='red', label='Tendencia')

# ==========================
# Crear ecuación como texto
# ==========================
eq_str = "y = "
for i, c in enumerate(coef):
    pot = grado - i
    if pot > 1:
        eq_str += f"{c:.5f}x^{pot} "
    elif pot == 1:
        eq_str += f"{c:.5f}x "
    else:
        eq_str += f"{c:.5f} "
    if i < len(coef)-1:
        eq_str += "+ "

# ==========================
# Gráfico
# ==========================
plt.title("Gráfica Posición del generador vs Caudal")
plt.xlabel("Posicion del generador")
plt.ylabel("Caudal Q [m3/s]")
plt.grid(True)

# Poner ecuación dentro de la gráfica
plt.text(min(x), max(y), eq_str, fontsize=10, color="red", bbox=dict(facecolor='white', alpha=0.7))

plt.legend()
plt.show()
