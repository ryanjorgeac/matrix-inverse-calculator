from matrix import Matrix
import matrixAsker

def test_getSizeLines():
    matrix1 = matrixAsker.makeMatrix(2, 4)
    assert matrix1.numberOfLines() == 2

def test_getSizeColumns():
    matrix1 = matrixAsker.makeMatrix(2, 4)
    assert matrix1.numberOfColumns() == 4

def test_getItem():
    matrix1 = matrixAsker.makeMatrix(2, 3)
    matrix1[0][0] = 4
    assert matrix1.__getitem__(0) == [4, 0, 0]

def test_getItem2():
    matrix1 = matrixAsker.makeMatrix(2, 4)
    matrix1[1][0] = 4
    matrix1[1][1] = 5
    assert matrix1.__getitem__(1) == [4, 5, 0, 0]

def test_setItem():
    matrix1 = matrixAsker.makeMatrix(2, 4)
    matrix1.__setitem__(1, [1, 2, 4, 6])
    assert matrix1[1] == [1, 2, 4, 6]

def test_setAndgetItem():
    matrix1 = matrixAsker.makeMatrix(2, 4)
    matrix1[0][0] = 40
    assert matrix1[0][0] == 40