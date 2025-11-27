# Proyecto: Detector de Palíndromos

## 📋 Descripción

Proyecto que implementa funciones para la detección de palíndromos en español, con soporte completo para tildes, mayúsculas, espacios y signos de puntuación. Incluye una suite completa de tests unitarios y parametrizados.

## 👤 Autor

**Ignacio Lázaro Zambrano**

Última Modificación: 27/11/2025

## 🚀 Características

- ✅ Detección de palíndromos con soporte para:
  - Mayúsculas y minúsculas
  - Tildes y acentos
  - Espacios
  - Signos de puntuación
  - Números
  - Caracteres especiales

- ✅ Suite completa de tests:
  - Tests unitarios tradicionales
  - Tests parametrizados
  - Más de 20 casos de prueba diferentes

## 🔧 Requisitos

- Python 3.6 o superior
- unittest (incluido en la biblioteca estándar de Python)

## 💻 Uso

### Programa Principal (main.py)

El programa principal `main.py` proporciona una interfaz interactiva para el usuario:

```bash
python main.py
```

**Funcionalidades:**
- Solicita frases al usuario de forma continua
- Verifica si cada frase es un palíndromo
- Permite salir escribiendo "salir"
- Maneja errores de entrada (cadenas vacías)
- Interfaz amigable con mensajes claros

**Ejemplo de ejecución:**
```
Introduce una frase (o 'salir' para terminar): > ojo
La frase 'ojo' ES palíndromo.

Introduce una frase (o 'salir' para terminar): > hola
La frase 'hola' NO es palíndromo.

Introduce una frase (o 'salir' para terminar): > salir
Gracias por usar el programa. ¡Hasta pronto!
```

## 🧪 Tests Incluidos

### TestEsPalindromo (Tests Unitarios)
- Palíndromos simples en minúsculas
- Palíndromos con mayúsculas
- Palíndromos con espacios
- Palíndromos con tildes y acentos
- Palíndromos con signos de puntuación
- Casos que NO son palíndromos
- Casos especiales (cadena vacía, un carácter, números, etc.)

### TestEsPalindromoParametrizado (Tests Parametrizados)
Define un test parametrizado de palíndromos válidos que utiliza una lista de palabras palíndromas. Mediante un bucle, se recorre la lista completa verificando que cada elemento sea efectivamente un palíndromo.

- **test_palindromos_validos**: Verifica múltiples palíndromos válidos
- **test_no_palindromos**: Verifica múltiples casos que NO son palíndromos


