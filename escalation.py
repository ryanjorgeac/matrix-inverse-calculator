import augmentedMatrix
import elementaryOperation
from matrixAsker import *
from TheresNoNotNullElementException import TheresNoNotNullElementException
from nnInvertibleException import nnInvertibleException
from CannotMultiplyLineToAchievePivotException import CannotMultiplyLineToAchievePivotException
from CannotMakeAPivotOnColumnException import *
from copy import *
from augmentedMatrix import AugmentedMatrix
from elementaryOperation import *
from maybe import *


def escalation(matrix):
    # copyOfMatrix = deepcopy(matrix)
    identityMatrixToCalculate = makeIdentityMatrix(matrix.numberOfLines())
    augmentedMatrixToCalculate = augmentedMatrix.AugmentedMatrix(matrix, identityMatrixToCalculate)
    return escalationOfAugmentedMatrix(augmentedMatrixToCalculate)


def makePivotOnColumn(augMatrix, line, column):
    if augMatrix[line][column] != 0:
        try:
            multiplyLineToAchievePivot(augMatrix, line)

        except CannotMultiplyLineToAchievePivotException:
            raise CannotMakeAPivotOnColumnException("Matriz não invertível.")


def putZerosInColumn(augMatrix, line, column):
    for i in range(len(augMatrix)):
        if i == line:
            continue

        else:
            valueToMultiply = -augMatrix[i][column]
            operation = addToOneRowAScalarMultipleOfAnother(valueToMultiply, i, line)
            augMatrix.applyElementaryOperations(operation)


def multiplyLineToAchievePivot(augMatrix, indexLine):
    if -len(augMatrix) > indexLine or indexLine >= len(augMatrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    maybeIndex = findNotNullOnLine(augMatrix.firstMatrix(), indexLine)
    indexNotNull = maybeIndex.orElseThrow(CannotMultiplyLineToAchievePivotException(
        "Não foi possível multiplicar a linha para encontrar o pivô.")
    )

    notNullNumber = augMatrix[indexLine][indexNotNull]
    reverseOfNotNullNumber = 1/notNullNumber

    operation = multiplyRowByANonZeroScalar(reverseOfNotNullNumber, indexLine)
    augMatrix.applyElementaryOperations(operation)


def findNotNullOnLine(matrix, indexLine):
    for i in range(matrix.numberOfLines()):
        if matrix[indexLine][i] != 0:
            return just(i)

    return nothing()

def findNotNullOnColumn(matrix, line, indexColumn):
    for i in range(line, matrix.numberOfLines()):
        if matrix[i][indexColumn] != 0:
            return just(i)

    return nothing()


def escalationOfAugmentedMatrix(augMatrix):
    column = 0
    i = 0
    while i < len(augMatrix) and column < augMatrix.firstMatrix().numberOfColumns():

        try:
            indexNotNull = findNotNullOnColumn(augMatrix.firstMatrix(), i, column).orElseThrow(
                TheresNoNotNullElementException("Não há elementos não nulos"))
            operation = elementaryOperation.swapTwoRows(i, indexNotNull)
            augMatrix.applyElementaryOperations(operation)
        except TheresNoNotNullElementException:
            column += 1
            continue

        makePivotOnColumn(augMatrix, i, column)
        putZerosInColumn(augMatrix, i, column)

        column, i = column + 1, i + 1

    return augMatrix