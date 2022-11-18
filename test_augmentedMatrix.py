from augmentedMatrix import AugmentedMatrix
import matrixAsker


def test_getItemFirstMatrix():
    matrix1 = matrixAsker.makeMatrix(2, 3)
    matrix2 = matrixAsker.makeMatrix(2, 3)
    matrix1[0][0] = 4
    matrix2[0][0] = 2
    x = AugmentedMatrix(matrix1, matrix2)
    assert x[0][0] == 4

def test_getItemSecondMatrix():
    matrix1 = matrixAsker.makeMatrix(2, 3)
    matrix2 = matrixAsker.makeMatrix(2, 3)
    matrix1[0][0] = 4
    matrix2[0][0] = 2
    x = AugmentedMatrix(matrix1, matrix2)
    assert x[0][3] == 2

def test_getItemSecondMatrixNull():
    matrix1 = matrixAsker.makeMatrix(2, 3)
    matrix2 = matrixAsker.makeMatrix(2, 3)
    matrix1[0][0] = 4
    matrix2[0][0] = 2
    x = AugmentedMatrix(matrix1, matrix2)
    assert x[0][4] == 0