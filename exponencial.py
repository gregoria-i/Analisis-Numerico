# exponencial.py
# Gregorio Martínez Andrea Itzel

# Programar grafica de la función exponencial
import numpy as np
import matplotlib.pyplot as plt

def calcular_factorial_iterativo(n: int):
  """
  Cálculo de factorial de forma iterativa (cómo vimos en ayudantía)
  """
  if n == 0:
    return 1
  elif n < 0:
    return "No ingresar numeros negativos"
  else:
    factorial = 1  # 
    for i in range(1, n+1):
        factorial *= i
    return factorial
  
def exponencial(x: float, num_terminos: int):
    """
    Función que para una x nos da un valor aproximado con serie de Taylor de la función exponencial
    """
    exp_x = 0
    for i in range(num_terminos):
        factorial = calcular_factorial_iterativo(i)
        exp_x += (x ** i) / factorial

    return exp_x

def generar_puntos(num_puntos: int, num_terminos_exponencial: int):
    """
    Función que genera dos listas de valores numéricos.
    lista_1 tiene valores consecutivos y lista_2 resulta de aplicar la función que recibe
    a los datos de lista_1
    """
    # Genera lista de números consecutivos
    lista_1 = np.linspace(0, num_puntos, num_puntos)

    # Lista vacía para alamacenar las evaluaciones
    lista_2 = []

    # Aplica la función a cada uno de los elementos de la lista_1
    for i in range(len(lista_1)):
        fx = exponencial(lista_1[i], num_terminos_exponencial)
        lista_2.append(fx)

    return lista_1, lista_2

def graficar_puntos(x: list[float], y: list[float]):
    """
    Función que recibe dos listas de números y los grafica utilizando matplotlib
    """
    plt.plot(x, y, linestyle="-", linewidth=2, marker=".", markersize=6, color="#FEAAAA", mec="#FF0000")
    plt.title("Gráfica de la función exponencial")
    plt.xlabel("x")
    plt.ylabel("exp(x)")
    plt.show()


if __name__=="__main__":
    try:
        numero_puntos = int(input("Número de puntos: "))
        numero_terminos = int(input("Número de términos en serie de Taylor: "))

        if numero_puntos <= 0 or numero_terminos <= 0:
            print("Error: Ingresa valores positivos mayores a 0.")
        else:
            valores_x, valores_fx = generar_puntos(numero_puntos, numero_terminos)
            graficar_puntos(valores_x, valores_fx)

    except ValueError:
        print("Error: Ingresa enteros positivos.")
        