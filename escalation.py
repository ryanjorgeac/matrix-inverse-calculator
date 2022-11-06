from matrixAsker import *
from TheresNoNotNullElementException import TheresNoNotNullElementException
from nnInvertibleException import nnInvertibleException
from CannotMultiplyLineToAchievePivotException import CannotMultiplyLineToAchievePivotException


def escalation(matrix):
    identityMatrixToCalculate = makeIdentityMatrix(len(matrix))
    # while matrix != identityMatrix:

    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            lineOfPivot = lookForPivotInOtherLines(matrix, i)
            if lineOfPivot < len(matrix):
                switchLines(matrix, identityMatrixToCalculate, i, lineOfPivot)
                putZerosInColumn(matrix, identityMatrixToCalculate, i)
            else:
                try:
                    multiplyLineToAchievePivot(matrix, identityMatrixToCalculate, i)

                except CannotMultiplyLineToAchievePivotException:
                    raise nnInvertibleException("Matriz não invertível.")

                putZerosInColumn(matrix, identityMatrixToCalculate, i)

        else:
            putZerosInColumn(matrix, identityMatrixToCalculate, i)

    return matrix, identityMatrixToCalculate


def putZerosInColumn(matrix, identityMatrix, position):
    for i in range(len(matrix)):
        if i == position:
            continue

        else:
            valueToMultiply = matrix[i][position]
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] - (valueToMultiply*matrix[position][j])
                identityMatrix[i][j] = identityMatrix[i][j] - (valueToMultiply * identityMatrix[position][j])


def lookForPivotInOtherLines(matrix, position):
    for i in range(len(matrix)):
        if matrix[i][position] == 1:
            return i
    else:
        return len(matrix)


def switchLines(matrix, identityMatrix,  indexLine1, indexLine2):
    if -len(matrix) > indexLine1 or indexLine1 >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    elif -len(matrix) > indexLine2 or indexLine2 >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    else:
        matrix[indexLine1], matrix[indexLine2] = matrix[indexLine2], matrix[indexLine1]
        identityMatrix[indexLine1], identityMatrix[indexLine2] = identityMatrix[indexLine2], identityMatrix[indexLine1]


def multiplyLineToAchievePivot(matrix, identityMatrix, indexLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    try:
        indexNotNull = findNotNull(matrix, indexLine)

    except TheresNoNotNullElementException:
        raise CannotMultiplyLineToAchievePivotException("Não foi possível multiplicar a linha para encontrar o pivô.")

    notNullNumber = matrix[indexLine][indexNotNull]
    reverseOfNotNullNumber = 1/notNullNumber

    # use 1/x where x is the Fraction to be reverted

    for i in range(len(matrix[indexLine])):
        matrix[indexLine][i] = matrix[indexLine][i] * reverseOfNotNullNumber
        identityMatrix[indexLine][i] = identityMatrix[indexLine][i] * reverseOfNotNullNumber


def findNotNull(matrix, indexLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    for i in range(len(matrix)):
        if matrix[indexLine][i] != 0:
            return i

    else:
        raise TheresNoNotNullElementException("Há somente elementos nulos")


# def multiplyTwoLines(matrix, identityMatrix, indexLine, pivotLine):
#     if -len(matrix) > indexLine or indexLine >= len(matrix):
#         raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")
#
#     elif -len(matrix) > pivotLine or pivotLine >= len(matrix):
#         raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")
#
#     indexNotNull = findNotNull(matrix, indexLine)
#     notNullNumber = matrix[indexLine][indexNotNull]
#
#     for i in range(len(matrix[indexLine])):
#         matrix[indexLine][i] = matrix[indexLine][i] - (notNullNumber * matrix[pivotLine][i])
#         identityMatrix[indexLine][i] = identityMatrix[indexLine][i] - (notNullNumber * identityMatrix[pivotLine][i])
