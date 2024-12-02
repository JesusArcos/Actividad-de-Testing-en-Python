# app/scripts/main.py
from app.scripts.charfun import esPalindromo

def main():
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")

if __name__ == "__main__":
    main()
