import mi_modulo
import math # Módulo estándar de Python

# Uso del módulo propio
mensaje = mi_modulo.saludar("Angel")
print(mensaje)
print("Valor de PI en mi módulo:", mi_modulo.PI)

# Uso de módulos de la biblioteca estándar
raiz = math.sqrt(64)
print("Raíz cuadrada de 64 según módulo math:", raiz)