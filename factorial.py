# factorial.py
# Gregorio Martínez Andrea Itzel

# Programar factorial
def calcular_factorial(n: int):
  """"
  Cálculo de factorial recursivo
  """
  if n == 0:
    return 1
  elif n < 0:
    return "No ingresar numeros negativos"
  else:
    return n * calcular_factorial(n-1)

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
  

if __name__ == "__main__":
    print(calcular_factorial(3))
    print(calcular_factorial_iterativo(3))
