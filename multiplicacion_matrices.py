# multiplicacion_matrices.py
# Gregorio Martínez Andrea Itzel 

# Programar multiplicación de matrices
import numpy as np


def multiplicacion_matrices_aleatorias(matriz_1 : np.array, matriz_2 : np.array):
  """
  Función que genera matrices aleatorias y las multiplica
  """
  # Generar matriz de ceros de dimensiones adecuadas
  matriz_resultado = np.zeros([matriz_1.shape[0], matriz_2.shape[1]])

  if matriz_1.shape[1] != matriz_2.shape[0]:
    return "No se pueden multiplicar las matrices"

  # Por cada fila de la matriz 1
  for i in range(matriz_1.shape[0]):
    
    # Por cada columna de la matriz 2
    for j in range(matriz_2.shape[1]):
      
      # Por cada elemento de la fila y columna correspondiente
      for k in range(matriz_1.shape[1]):
        # Rellenar matriz
        matriz_resultado[i][j] += matriz_1[i][k] * matriz_2[k][j]

  return matriz_resultado


if __name__ == "__main__":
    # Generar matrices aleatorias
    matriz_A = np.random.random([2,1])
    matriz_B = np.random.random([1,3])

    # Multiplicar matrices
    print(multiplicacion_matrices_aleatorias(matriz_A, matriz_B))
