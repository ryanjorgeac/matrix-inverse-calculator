from fractions import Fraction
import matrixAsker

class Matrix:
    def __init__(self, sizeOfMatrix, inputToBeUsed):
        if sizeOfMatrix <= 0:
            raise ValueError("O tamanho da matriz precisa ser um valor positivo maior que 0")
        self.size = sizeOfMatrix
        self.matrix = []
        self.inputIO = inputToBeUsed

    def createMatrix(self, listOfNumbers):
        pass

