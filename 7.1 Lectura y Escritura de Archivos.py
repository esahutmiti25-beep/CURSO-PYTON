# 1. Escritura en un archivo text
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea 1: Registro de prácticas Python.\n")
    archivo.write("Línea 2: Aprendiendo entrada y salida de archivos.\n")

# 2. Lectura del archivo creado
try:
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("--- Contenido del archivo ---")
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")