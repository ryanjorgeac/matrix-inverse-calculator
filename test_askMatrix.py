import matrixAsker

def test_askMatrix_1():
    x = matrixAsker.makeMatrix(1)
    assert x == [[0]]


def test_askMatrix_2():
    x = matrixAsker.makeMatrix(2)
    assert x == [[0, 0],
                 [0, 0]]

def test_askMatrix_3():
    x = matrixAsker.makeMatrix(3)
    assert x == [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
