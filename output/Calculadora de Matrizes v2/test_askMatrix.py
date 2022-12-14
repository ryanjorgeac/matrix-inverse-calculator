import matrixAsker
from fractions import Fraction
from matrix import Matrix

def test_makeMatrix_1():
    x = matrixAsker.makeMatrix(1, 1)
    assert x == Matrix([[0]])


def test_makeMatrix_2():
    x = matrixAsker.makeMatrix(2, 2)
    assert x == Matrix([[0, 0],
                 [0, 0]])


def test_makeMatrix_3():
    x = matrixAsker.makeMatrix(3, 3)
    assert x == Matrix([[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])

def test_makeMatrix_not_square():
    x = matrixAsker.makeMatrix(3, 4)
    assert x == Matrix([[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]])

def test_makeMatrix_not_square2():
    x = matrixAsker.makeMatrix(4, 2)
    assert x == Matrix([[0, 0],
                        [0, 0],
                        [0, 0],
                        [0, 0]])

def test_makeMatrix_4x3():
    x = matrixAsker.makeMatrix(4, 3)
    assert x == Matrix([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])


def test_makeIdentityMatrix_1():
    x = matrixAsker.makeIdentityMatrix(2)
    assert x == Matrix([[Fraction(1, 1), Fraction(0, 1)],
                [Fraction(0, 1), Fraction(1, 1)]])


def test_makeIdentityMatrix_2():
    x = matrixAsker.makeIdentityMatrix(3)
    assert x == Matrix([[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]])


def test_makeIdentityMatrix_3():
    x = matrixAsker.makeIdentityMatrix(4)
    assert x == Matrix([[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]])
