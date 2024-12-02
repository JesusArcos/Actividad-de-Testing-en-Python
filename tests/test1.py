# tests/test1.py
import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    
    def test_palindromos(self):
        # Pruebas con frases palíndromas
        self.assertTrue(esPalindromo("Anita lava la tina"))
        self.assertTrue(esPalindromo("A man, a plan, a canal, Panama"))
        self.assertTrue(esPalindromo("Was it a car or a cat I saw"))
        
    def test_no_palindromos(self):
        # Pruebas con frases no palíndromas
        self.assertFalse(esPalindromo("Hola mundo"))
        self.assertFalse(esPalindromo("Python es divertido"))
    
    def test_ignorar_espacios(self):
        # Pruebas con espacios intercalados
        self.assertTrue(esPalindromo("   A man a   plan a canal Panama   "))
    
    def test_ignorar_mayusculas(self):
        # Pruebas que ignoran mayúsculas
        self.assertTrue(esPalindromo("Madam In Eden, I'm Adam"))
    
    def test_ignorar_puntajes(self):
        # Pruebas con puntuación
        self.assertTrue(esPalindromo("Eva, can I see bees in a cave?"))
    
    def test_cadenas_vacias(self):
        # Probar con una cadena vacía
        self.assertTrue(esPalindromo(""))
    
    def test_espacios_al_inicio_y_final(self):
        # Probar cadenas con espacios adicionales al principio y al final
        self.assertTrue(esPalindromo("   A man a plan a canal Panama   "))

    
    def test_no_palindromo_con_acentos(self):
        # Probar con una cadena que no es palíndroma, incluso con tildes
        self.assertFalse(esPalindromo("Arbol"))
        
if __name__ == "__main__":
    unittest.main()
