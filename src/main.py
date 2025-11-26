"""
main.py

Programa principal que utilliza la función esPalindromo del módulo "functions"
para determinar si una cadena introducida por el usuario es palíndroma.
El programa seguirá solicitando cadenas hasta que el usuario escriba
"salir".

Ultima Modificación. 26/11/2025
Autor. Ignacio Lázaro Zambrano
Dependencias. Unicodedata

"""

from functions.charfun import *

def main():
    """
    Función principal que gestiona la interacción con el usuario.
    """
    while True:
        try:
            input_str = input("Introduce una frase (o 'salir' para terminar): ")
            
            # Verificamos si el usuario ha escrito "salir"
            if input_str.lower().strip() == "salir":
                print("Gracias por usar el programa. ¡Hasta pronto!")
                break
            
            # Comprobamos si es palíndromo
            if esPalindromo(input_str):
                print(f"La frase '{input_str}' ES palíndroma.\n")
            else:
                print(f"La frase '{input_str}' NO es palíndroma.\n")

        except Exception as e:
            print(f"Error inesperado: {e}\n")

if __name__ == "__main__":
    main()