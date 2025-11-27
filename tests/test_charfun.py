"""
test_charfun.py

Tests unitarios para la función esPalindromo del módulo functions.
Incluye numerosos casos de prueba para garantizar el correcto funcionamiento
de la detección de palíndromos.

Última Modificación: 26/11/2025
Autor: Ignacio Lázaro Zambrano
Dependencias: unittest, sys, os

"""

import unittest
import sys
import os


# Añadimos el directorio src al path para poder importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.functions.charfun import esPalindromo



class TestEsPalindromo(unittest.TestCase):
    """
    Clase de tests para la función esPalindromo.
    
    Tests incluidos:

    - Palíndromos simples
    - Palíndromos con mayúsculas y minúsculas
    - Palíndromos con espacios
    - Palíndromos con tildes
    - Palíndromos con signos de puntuación
    - Frases no palíndromas
    - Casos especiales 
   
    """

    # Tests palindromos simples, mayúsculas, minúsculas, espacios, tildes y puntuación
    
    def test_palindromo_simple_minusculas(self):
        """Test: Palíndromo simple en minúsculas"""
        self.assertTrue(esPalindromo("ojo"))
        self.assertTrue(esPalindromo("ese"))
        self.assertTrue(esPalindromo("sometemos"))
    
    def test_palindromo_simple_mayusculas(self):
        """Test: Palíndromo con mayúsculas"""
        self.assertTrue(esPalindromo("OJO"))
        self.assertTrue(esPalindromo("ESE"))
        self.assertTrue(esPalindromo("SOMETEMOS"))
    
    def test_palindromo_con_espacios(self):
        """Test: Palíndromo con espacios"""
        self.assertTrue(esPalindromo("amor a roma"))
        self.assertTrue(esPalindromo("yo soy"))
        self.assertTrue(esPalindromo("luz azul"))
    
    def test_palindromo_con_tildes(self):
        """Test: Palíndromo con tildes y acentos"""
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"))
        self.assertTrue(esPalindromo("Sé verlas al revés"))
    
    def test_palindromo_con_puntuacion(self):
        """Test: Palíndromo con signos de puntuación"""
        self.assertTrue(esPalindromo("A mamá, Roma le aviva el amor a mamá"))
        self.assertTrue(esPalindromo("¿Acaso hubo búhos acá?"))
        self.assertTrue(esPalindromo("A ti no, bonita"))
    

    # Tests no palíndromos
    
    def test_no_palindromo_simple_minusculas(self):
        """Test: Frases que NO son palíndromas"""
        self.assertFalse(esPalindromo("ignacio"))
        self.assertFalse(esPalindromo("puesta"))
        self.assertFalse(esPalindromo("segura"))

    def test_no_palindromo_simple_mayusculas(self):
        """Test: Frases que NO son palíndromas"""
        self.assertFalse(esPalindromo("Ignacio"))
        self.assertFalse(esPalindromo("Puesta"))
        self.assertFalse(esPalindromo("Segura"))
    
    def test_no_palindromo_con_espacios(self):
        """Test: Frases con espacios que NO son palíndromas"""
        self.assertFalse(esPalindromo("esto no es palindromo"))
        self.assertFalse(esPalindromo("una frase cualquiera"))


    # Tests de casos especiales

    def test_cadena_vacia(self):
        """Test: Cadena vacía"""
        with self.assertRaises(ValueError):
            esPalindromo("")
    
    def test_un_solo_caracter(self):
        """Test: Un solo carácter (siempre es palíndromo)"""
        self.assertTrue(esPalindromo("a"))
        self.assertTrue(esPalindromo("Z"))
        self.assertTrue(esPalindromo("5"))
    
    def test_palindromo_numeros(self):
        """Test: Palíndromos con números"""
        self.assertTrue(esPalindromo("12321"))
        self.assertTrue(esPalindromo("1 2 3 2 1"))
    
    def test_palindromo_mayusculas_minusculas_mezcladas(self):
        """Test: Palíndromo con mayúsculas y minúsculas mezcladas"""
        self.assertTrue(esPalindromo("AnItA LaVa La TiNa"))
        self.assertTrue(esPalindromo("ReCOnoceR"))
    
    def test_palindromo_mixto(self):
        """Test: Palíndromos con letras y números"""
        self.assertTrue(esPalindromo("I181I"))
        self.assertTrue(esPalindromo("22 ama 22"))
    
    def test_caracteres_especiales_multiples(self):
        """Test: Palíndromo con múltiples caracteres especiales"""
        self.assertTrue(esPalindromo("@O#S#O@"))
        self.assertTrue(esPalindromo("[[O]]j[[O]]"))

    def test_palindromos_muy_largos(self):
        """Test: Palíndromo con muchos caracteres"""
        self.assertTrue(esPalindromo("a" * 1000 + "b" + "a" * 1000))
        self.assertTrue(esPalindromo("1" * 500 + "2" + "1" * 500))


class TestEsPalindromoParametrizado(unittest.TestCase):
    """
    Clase de tests parametrizados para esPalindromo.
    """
    
    def test_palindromos_validos(self):
        """Test: Múltiples casos de palíndromos válidos"""
        casos_validos = [
            "ojo",
            "ESE",
            "amor a roma",
            "Dábale arroz a la zorra el abad",
            "¿Acaso hubo búhos acá?",
            "[[O]]j[[O]]",
            "I181I",
            "ReCOnoceR",
        ]
        
        for caso in casos_validos:
            with self.subTest(caso=caso):
                self.assertTrue(esPalindromo(caso))
    
    def test_no_palindromos(self):
        """Test: Múltiples casos que NO son palíndromos"""
        casos_invalidos = [
            "ignacio",
            "PUESTA",
            "aprendo python",
            "Atún con tomate",
            "¿Eres tú, Pedro?",
            "I1891I",
            "AlBorNoz",
        ]
        
        for caso in casos_invalidos:
            with self.subTest(caso=caso):
                self.assertFalse(esPalindromo(caso))

if __name__ == "__main__":
    unittest.main(verbosity=2)