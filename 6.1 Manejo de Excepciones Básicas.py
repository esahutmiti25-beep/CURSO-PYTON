try:
    num1 = 10
    num2 = 0
    resultado = num1 / num2
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except TypeError as e:
    print(f"Error de tipo: {e}")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("Fin del bloque try-except.\n")