class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad proporcionada no es válida."""
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser un número negativo.")
    return f"Edad registrada: {edad}"

try:
    print(verificar_edad(-5))
except EdadInvalidaError as error:
    print(f"Excepción capturada: {error}")