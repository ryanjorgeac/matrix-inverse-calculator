from fractions import Fraction

from TheresNoNotNullElementException import TheresNoNotNullElementException


def escalation(matrix, sizeOfMatrix):
    pass

def switchLines(matrix, indexLine1, indexLine2):
    if -len(matrix) > indexLine1 or indexLine1 >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    elif -len(matrix) > indexLine2 or indexLine2 >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    else:
        matrix[indexLine1], matrix[indexLine2] = matrix[indexLine2], matrix[indexLine1]

def multiplyLineToAchievePivot(matrix, indexLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    indexNotNull = findNotNull(matrix, indexLine)
    notNullNumber = matrix[indexLine][indexNotNull]
    reverseOfNotNullNumber = 1/notNullNumber

    # use 1/x where x is the Fraction to be reverted

    for i in range(len(matrix[indexLine])):
        matrix[indexLine][i] = matrix[indexLine][i] * reverseOfNotNullNumber


def findNotNull(matrix, indexLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    for i in range(len(matrix)):
        if matrix[indexLine][i] != 0:
            return i

    else:
        raise TheresNoNotNullElementException("Non-invertible matrix")


def multiplyTwoLines(matrix, indexLine, pivotLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    elif -len(matrix) > pivotLine or pivotLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    indexNotNull = findNotNull(matrix, indexLine)
    notNullNumber = matrix[indexLine][indexNotNull]

    for i in range(len(matrix[indexLine])):
        matrix[indexLine][i] = matrix[indexLine][i] - (notNullNumber * matrix[pivotLine][i])
