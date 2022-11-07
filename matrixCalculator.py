import inputIO
from escalation import *


def main(userIO):
    size = int(userIO.input("Informe o tamanho da Matriz: "))
    matriz = askMatrix(size, userIO)
    print("\n\n")
    try:
        result = escalation(matriz)
        print("Matriz: ")
        viewMatrix(result[0], userIO)
        print("")
        print("Inversa: ")
        viewMatrix(result[1], userIO)
    except nnInvertibleException as error:
        print(error.args[0])


if __name__ == "__main__":
    main(inputIO.inputIO())
