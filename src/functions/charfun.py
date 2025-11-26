"""
charfun.py

Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.

Ultima Modificación. 26/11/2025
Autor. Ignacio Lázaro Zambrano
Dependencias. Unicodedata

"""

import unicodedata


def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """

    # Validamos que la cadena no esté vacía
    if not cadena or not cadena.strip():
        raise ValueError("La cadena no puede estar vacía")
    
    # Convertimos la cadena a minúsculas
    cadena_lower = cadena.lower()
    
    # Normalizamos para quitar las tildes con NFD (Normalization Form Decomposition)
    cadena_normalizada = unicodedata.normalize('NFD', cadena_lower)
    
    # Filtamos solo los carácteres alfanuméricos (ignorando espacios y signos de puntuación)
    cadena_limpia = ''

    for caracter in cadena_normalizada:
        if caracter.isalnum():
            cadena_limpia += caracter
    
    # Comprobamos si es igual al revés
    cadena_reversa = cadena_limpia[::-1]
    
    if cadena_limpia == cadena_reversa:
        return True
    else:
        return False