from matrixAsker import *
from TheresNoNotNullElementException import TheresNoNotNullElementException
from nnInvertibleException import nnInvertibleException
from CannotMultiplyLineToAchievePivotException import CannotMultiplyLineToAchievePivotException
from CannotMakeAPivotOnColumnException import *
from copy import *


def escalation(matrix):
    copyOfMatrix = deepcopy(matrix)
    identityMatrixToCalculate = makeIdentityMatrix(len(matrix))
    for i in range(len(matrix)):
        try:
            makePivotOnColumn(matrix, identityMatrixToCalculate, i)
            putZerosInColumn(matrix, identityMatrixToCalculate, i)
        except CannotMakeAPivotOnColumnException:
            raise nnInvertibleException("Matriz não invertível.")

    return copyOfMatrix, identityMatrixToCalculate


def makePivotOnColumn(matrix, identityMatrix, position):
    if matrix[position][position] != 1:
        try:
            multiplyLineToAchievePivot(matrix, identityMatrix, position)

        except CannotMultiplyLineToAchievePivotException:
            raise CannotMakeAPivotOnColumnException("Matriz não invertível.")


def putZerosInColumn(matrix, identityMatrix, position):
    for i in range(len(matrix)):
        if i == position:
            continue

        else:
            valueToMultiply = matrix[i][position]
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] - (valueToMultiply*matrix[position][j])
                identityMatrix[i][j] = identityMatrix[i][j] - (valueToMultiply * identityMatrix[position][j])


def multiplyLineToAchievePivot(matrix, identityMatrix, indexLine):
    if -len(matrix) > indexLine or indexLine >= len(matrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    try:
        indexNotNull = findNotNull(matrix, indexLine)

    except TheresNoNotNullElementException:
        raise CannotMultiplyLineToAchievePivotException("Não foi possível multiplicar a linha para encontrar o pivô.")

    notNullNumber = matrix[indexLine][indexNotNull]
    reverseOfNotNullNumber = 1/notNullNumber

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
