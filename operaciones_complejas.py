# operaciones_complejas.py
# Gregorio Martínez Andrea Itzel

# Programar un menú de operaciones complejas
def suma_complejos(z1: complex , z2: complex):
  """
  Suma de dos números complejos
  """
  return complex(z1.real + z2.real, z1.imag + z2.imag)

def resta_complejos(z1: complex, z2: complex):
  """
  Resta de dos números complejos
  """
  return complex(z1.real - z2.real, z1.imag - z2.imag)

def multiplicacion_complejos(z1: complex, z2: complex):
  """
  Multiplicación de dos números complejos
  """
  return complex(z1.real * z2.real - z1.imag * z2.imag, z1.real * z2.imag + z1.imag * z2.real)

def division_complejos(z1: complex, z2: complex):
  """
  División de dos números complejos
  """
  return complex((z1.real * z2.real + z1.imag * z2.imag) / (z2.real**2 + z2.imag**2), (z2.real * z1.imag - z1.real * z2.imag) / (z2.real**2 + z2.imag**2))

def menu():
  """
  Menú de operaciones de números complejos para 2 valores
  """
  mensaje = "Elija una opción:\n"
  mensaje += "1. Suma de complejos\n"
  mensaje += "2. Resta de complejos\n"
  mensaje += "3. Multiplicación de complejos\n"
  mensaje += "4. División de complejos\n"

  operacion = input(mensaje)
  # Descarta opción inválida
  if operacion not in ["1", "2", "3", "4"]:
    return "Opción no válida"

  z1 = input("Ingrese z1 = (a+bj): ")
  z2 = input("Ingrese z2 = (c+dj): ")


  # Llama a la operación
  if operacion == "1":
    print(suma_complejos(complex(z1), complex(z2)))
  elif operacion == "2":
    print(resta_complejos(complex(z1), complex(z2)))
  elif operacion == "3":
    print(multiplicacion_complejos(complex(z1), complex(z2)))
  elif operacion == "4":
    print(division_complejos(complex(z1), complex(z2)))


if __name__ == "__main__":
  menu()
