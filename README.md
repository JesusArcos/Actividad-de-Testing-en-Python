# Actividad-de-Testing-en-Python

Puesta en Producción Segura
CPIFP Alan Turing. Curso 24/25
Actividad de Evaluación sobre Testing en Python 3

En tu empresa se ha creado un programa en un fichero denominado charfun.py que solicita
repetidas veces a un usuario que introduzca una cadena de texto. Si el usuario escribe salir, el
programa termina. Si no, se analizará la cadena de texto para saber si es palíndroma informando
del resultado por pantalla y volviendo nuevamente a preguntar por otra cadena. Dicho fichero
contiene una función llamada esPalindromo(cadena). Esta función determina si la cadena
pasada como parámetro contiene o no una frase palíndroma.
Una cadena de texto se dice que es palíndroma si se lee igual de adelante hacia atrás y de atrás
hacia delante, una vez que se eliminan los espacios, puntuación, tíldes, diéresis, etc y se ignoran
las diferencias entre mayúsculas y minúsculas.
En la actualidad charfun.py tiene la siguiente estructura:
r"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 21/11/2024
Autor. Gregorio Coronado Morón
Dependencias. Unicodedata
"""
import unicodedata
def esPalindromo(cadena):
"""
Función que verifica si una cadena es palíndroma.
Ignora espacios, mayúsculas y tildes.
"""
# Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos

cadena_limpia = ''.join(char.lower() for char in cadena if
char.isalnum())

# Comparar la cadena limpia con su reverso

return cadena_limpia == cadena_limpia[::-1]
frase = input("Introduce una frase (o escribe 'salir' para
terminar): ")
if frase.lower() == "salir":
print("Programa finalizado.")
else:

# Comprobar si es palíndromo

if esPalindromo(frase):
print("La frase es palíndroma.")
else:
print("La frase no es palíndroma.")

Dado el programa anterior se te encomienda dotar de la estructura necesaria al programa
y realizar una clase de testing. Para ello, en un nuevo fichero:
• Importa la librería de texto de software en este caso unittest.
• Crea una clase (del tipo unittest.TextCase)
• Dentro de esta clase definiremos una o varias funciones (podemos llamarlas como
consideremos pero es recomendable un nombre ilustrativo)
• Dentro de la función reflejaremos el tipo de testeo que vamos a realizar.
• No olvides incluir todas aquellas comprobaciones que creas necesarias para testear
que la función esPalindromo funciona correctamente. No des por sentado que el
programador puede hacer un "buen uso" de ella. Prepárala para "lo peor".
Una vez hecho el programa de testing, si encuentras algún fallo debes modificarlo para que
pase los tests de manera correcta.
