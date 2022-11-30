from copy import deepcopy
import augmentedMatrix
import escalation
from matrixAsker import makeIdentityMatrix
from maybe import just, nothing


def inverter(matrix):
    copyOfMatrix = deepcopy(matrix)
    identityMatrixToCalculate = makeIdentityMatrix(matrix.numberOfLines())
    augMatrix = augmentedMatrix.AugmentedMatrix(copyOfMatrix, identityMatrixToCalculate)
    escalatedMatrix = escalation.escalationOfAugmentedMatrix(augMatrix)
    if escalatedMatrix.firstMatrix() == makeIdentityMatrix(matrix.numberOfLines()):
        return just(escalatedMatrix.secondMatrix())

    else:
        return nothing()
