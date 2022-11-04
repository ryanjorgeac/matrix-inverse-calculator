import inputIO
from escalation import *

def main(userIO):
    size = int(userIO.input("Informe o tamanho da Matriz: "))
    matriz = askMatrix(size, userIO)
    viewMatrix(size, matriz, userIO)
    print("\nComeçando o escalonamento...\n")
    result = escalation(matriz)
    print("Matriz: ")
    viewMatrix(len(result[0]), result[0], userIO)
    print("")
    print("Inversa: ")
    viewMatrix(len(result[1]), result[1], userIO)


if __name__ == "__main__":
    main(inputIO.inputIO())
