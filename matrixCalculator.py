import inputIO
from escalation import escalation
from matrixAsker import viewMatrix, askMatrix
from nnInvertibleException import nnInvertibleException
from matrixInverter import inverter


def main(userIO):
    menu()
    opcao = input("         ")
    if opcao == "3":
        print('''
            Até logo :)''')
        return

    elif opcao == "2":
        howManyLines = int(userIO.input("Informe a quantidade de linhas da Matriz: "))
        howManyColumns = int(userIO.input("Informe a quantidade de colunas da Matriz: "))
        matriz = askMatrix(howManyLines, howManyColumns, userIO)

        print("\n\n")
        print("Matriz: ")
        viewMatrix(matriz, userIO)
        print("")

        result = escalation(matriz)
        print("Matriz Escalonada: ")
        viewMatrix(result.firstMatrix(), userIO)

    elif opcao == "1":
        matrixOrder = int(userIO.input("Informe a ordem da Matriz: "))
        matriz = askMatrix(matrixOrder, matrixOrder, userIO)

        print("\n\n")
        print("Matriz: ")
        viewMatrix(matriz, userIO)
        print("")

        try:
            result = inverter(matriz).orElseThrow(nnInvertibleException("Matriz não invertível."))
            print("Matriz Inversa: ")
            viewMatrix(result, userIO)
        except nnInvertibleException:
            print("Matriz não invertível.")
            return


def menu():
    print('''
    Bem-vindo(a) a Calculadora de Matrizes!
            O que deseja calcular?
            
        [1] - Inverter uma Matriz
        [2] - Escalonar uma Matriz
        [3] - Sair''')


if __name__ == "__main__":
    main(inputIO.inputIO())
