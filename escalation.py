import augmentedMatrix
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
    copyOfMatrix = deepcopy(matrix)
    identityMatrixToCalculate = makeIdentityMatrix(matrix.numberOfLines())
    augmentedMatrixToCalculate = augmentedMatrix.AugmentedMatrix(copyOfMatrix, identityMatrixToCalculate)
    return escalationOfAugmentedMatrix(augmentedMatrixToCalculate)


def makePivotOnColumn(augMatrix, position):
    if augMatrix[position][position] != 0:
        try:
            multiplyLineToAchievePivot(augMatrix, position)

        except CannotMultiplyLineToAchievePivotException:
            raise CannotMakeAPivotOnColumnException("Matriz não invertível.")


def putZerosInColumn(augMatrix, position):
    for i in range(len(augMatrix)):
        if i == position:
            continue

        else:
            valueToMultiply = -augMatrix[i][position]
            operation = addToOneRowAScalarMultipleOfAnother(valueToMultiply, i, position)
            augMatrix.applyElementaryOperations(operation)


def multiplyLineToAchievePivot(augMatrix, indexLine):
    if -len(augMatrix) > indexLine or indexLine >= len(augMatrix):
        raise ValueError("O índex da linha a ser alterada é inexistente na matriz.")

    maybeIndex = findNotNull(augMatrix.firstMatrix(), indexLine)
    indexNotNull = maybeIndex.orElseThrow(CannotMultiplyLineToAchievePivotException(
        "Não foi possível multiplicar a linha para encontrar o pivô.")
    )

    notNullNumber = augMatrix[indexLine][indexNotNull]
    reverseOfNotNullNumber = 1/notNullNumber

    operation = multiplyRowByANonZeroScalar(reverseOfNotNullNumber, indexLine)
    augMatrix.applyElementaryOperations(operation)


def findNotNull(matrix, indexLine):
    for i in range(matrix.numberOfLines()):
        if matrix[indexLine][i] != 0:
            return just(i)

    return nothing()


def escalationOfAugmentedMatrix(augMatrix):
    column = 0
    for i in range(len(augMatrix)):
        makePivotOnColumn(augMatrix, i)
        putZerosInColumn(augMatrix, i)

    return augMatrix