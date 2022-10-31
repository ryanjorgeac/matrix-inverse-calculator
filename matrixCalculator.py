import inputIO
from matrixAsker import *

def main(userIO):
    size = int(userIO.input("Informe o tamanho da Matriz: "))
    matriz = askMatrix(size, userIO)
    viewMatrix(size, matriz, userIO)
    print("Acabou aqui.")

if __name__ == "__main__":
    main(inputIO.inputIO())
