import matrixAsker
from fractions import Fraction

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

def test_makeIdentityMatrix_1():
    x = matrixAsker.makeIdentityMatrix(2)
    assert x == [[Fraction(1, 1), Fraction(0, 1)],
                [Fraction(0, 1), Fraction(1, 1)]]

def test_makeIdentityMatrix_2():
    x = matrixAsker.makeIdentityMatrix(3)
    assert x == [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]]

def test_makeIdentityMatrix_3():
    x = matrixAsker.makeIdentityMatrix(4)
    assert x == [[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
                 [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]]
