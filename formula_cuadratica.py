# formula_cuadratica.py
# Gregorio Martínez Andrea Itzel

# Programar fórmula cuadrática
def formula_cuadratica(a: float, b:float, c:float):
  """
  Función que cálcula las soluciones de una ecuación cuadrática
  Args:
    a: coeficiente cuadrático
    b: coeficiente lineal
    c: término independiente
  Returns:
    Soluciones de la ecuación cuadrática o 
    mensaje que indique que no es ecuación cuadrática
  """
  # Descartar casos cuando no es ecuación cuadrática
  if a == 0 and b==0 and c==0:
    return "No es una ecuación cuadrática"
  elif a == 0 and b==0:
    return "No es una ecuación cuadrática"
  elif a == 0:
    return -c/b, "Observación. No es una ecuación cuadrática"
  else:
    determinante = b**2 - 4*a*c
  
  # Cálculo de raíces según su determinante
  if determinante == 0:
    # Raíces iguales
    x1 = -b / (2*a)
    x2 = x1
  elif determinante < 0:
    # Raíces complejas
    determinante = determinante * -1
    x1 = -b / (2 * a) + (determinante**(1/2) / 2 * a) * 1j
    x2 = -b / (2 * a) - (determinante**(1/2) / 2 * a) * 1j
  else:
    # Raíces reales
    x1 = (-b + determinante**(1/2)) / (2*a)
    x2 = (-b - determinante**(1/2)) / (2*a)

  return x1,x2


if __name__ == "__main__":
  a = float(input("a = "))
  b = float(input("b = "))
  c = float(input("c = "))

  print(formula_cuadratica(a,b,c))
    