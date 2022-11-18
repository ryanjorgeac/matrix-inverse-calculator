import inputIO
from escalation import *


def main(userIO):
    howManyLines = int(userIO.input("Informe a quantidade de linhas da Matriz: "))
    howManyColumns = int(userIO.input("Informe a quantidade de colunas da Matriz: "))
    matriz = askMatrix(howManyLines, howManyColumns, userIO)
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
