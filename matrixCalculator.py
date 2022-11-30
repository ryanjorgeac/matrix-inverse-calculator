import inputIO
from escalation import *


def main(userIO):
    menu()
    opcao = input("         ")
    if opcao == "3":
        print('''
            Até logo :)''')
        return

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


def menu():
    print('''
    Bem-vindo(a) a Calculadora de Matrizes!
            O que deseja calcular?
            
        [1] - Inverter uma Matriz
        [2] - Escalonar uma Matriz
        [3] - Sair''')


if __name__ == "__main__":
    main(inputIO.inputIO())
