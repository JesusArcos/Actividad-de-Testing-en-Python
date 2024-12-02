# tests/test_2.py
import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromoSimple(unittest.TestCase):
    
    def test_palindromos_simples(self):
        # Pruebas con cadenas simples
        self.assertTrue(esPalindromo("madam"))
        self.assertTrue(esPalindromo("racecar"))
    
    def test_no_palindromos_simples(self):
        # Pruebas con cadenas no palíndromas simples
        self.assertFalse(esPalindromo("hello"))
        self.assertFalse(esPalindromo("world"))
        
if __name__ == "__main__":
    unittest.main()