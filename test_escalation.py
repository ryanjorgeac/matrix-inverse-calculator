import escalation
import matrixAsker
from fractions import Fraction

from TheresNoNotNullElementException import TheresNoNotNullElementException


class inputFake:
    def __init__(self, lista):
        self.inputList = lista
        self.outputList = []

    def input(self, prompt):
        return self.inputList.pop()

    def print(self, prompt, end=None):
        self.outputList.append(prompt)


def test_escalation_switchLines_size2():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)
    matrizSwitched = matriz.copy()
    identityMatrix = escalation.makeIdentityMatrix(2)
    escalation.switchLines(matrizSwitched, identityMatrix, 0, 1)
    assert matriz == [[Fraction(2, 1), Fraction(3, 1)],
                      [Fraction(4, 1), Fraction(5, 1)]] and matrizSwitched == [
        [Fraction(4, 1), Fraction(5, 1)], [Fraction(2, 1), Fraction(3, 1)]]


def test_escalation_switchLines_size3():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    matrizSwitched = matriz.copy()
    identityMatrix = escalation.makeIdentityMatrix(3)
    escalation.switchLines(matrizSwitched, identityMatrix, 1, 2)
    assert matriz == [[Fraction(13, 3), Fraction(0, 1), Fraction(1, 2)],
                      [Fraction(14, 1), Fraction(5, 1), Fraction(2, 1)],
                      [Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)]] \
           and matrizSwitched == [[Fraction(13, 3), Fraction(0, 1), Fraction(1, 2)],
                                  [Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)],
                                  [Fraction(14, 1), Fraction(5, 1), Fraction(2, 1)]]

def test_escalation_multiplyLine1():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)
    identityMatrix = escalation.makeIdentityMatrix(2)
    escalation.multiplyLineToAchievePivot(matriz, identityMatrix, 0)
    assert matriz[0] == [Fraction(1, 1), Fraction(3, 2)]

def test_escalation_multiplyLine2():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    identityMatrix = escalation.makeIdentityMatrix(3)
    escalation.multiplyLineToAchievePivot(matriz, identityMatrix, 1)
    assert matriz[1] == [Fraction(1, 1), Fraction(5, 14), Fraction(2, 14)]

def test_escalation_multiplyLine3():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "13/3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    identityMatrix = escalation.makeIdentityMatrix(3)
    escalation.multiplyLineToAchievePivot(matriz, identityMatrix, 0)
    assert matriz[0] == [Fraction(0, 1), Fraction(1, 1), Fraction(3, 26)]

def test_escalation_findNotNull1():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)
    x = escalation.findNotNull(matriz, 0)
    assert x == 0

def test_escalation_findNotNull2():
    numbers = ["5", "4", "3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)
    x = escalation.findNotNull(matriz, 0)
    assert x == 1

def test_escalation_findNotNull3():
    numbers = ["5", "4", "0", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)
    try:
        x = escalation.findNotNull(matriz, 0)
        assert False
    except TheresNoNotNullElementException as error:
        assert error.__str__() == "Non-invertible matrix"
    except (Exception,):
        assert False

def test_multiplyTwoLines_1():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)                    # [Fraction(2, 1), Fraction(3, 1)]
    identityMatrix = escalation.makeIdentityMatrix(2)
    escalation.multiplyTwoLines(matriz, identityMatrix, 1, 0)               # [Fraction(4, 1), Fraction(5, 1)]
    assert matriz[1] == [Fraction(-4, 1), Fraction(-7, 1)]

def test_multiplyTwoLines_with_first_null_element():
    numbers = ["5", "4", "3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, i)                    # [Fraction(0, 1), Fraction(3, 1)]
    identityMatrix = escalation.makeIdentityMatrix(2)
    escalation.multiplyTwoLines(matriz, identityMatrix, 1, 0)               # [Fraction(4, 1), Fraction(5, 1)]
    assert matriz[1] == [Fraction(4, 1), Fraction(-7, 1)]


def test_multiplyTwoLines_with_3_x_3_matrix():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)                    # [Fraction(13, 3), Fraction(0, 1), Fraction(1, 2)]
    identityMatrix = escalation.makeIdentityMatrix(3)
    escalation.multiplyTwoLines(matriz, identityMatrix, 1, 2)               # [Fraction(14, 1), Fraction(5, 1), Fraction(2, 1)]
    assert matriz[1] == [Fraction(-28, 1), Fraction(-51, 1), Fraction(-68, 1)]
                                                            # [Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)]

def test_lookForPivotInOtherLine_1():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    x = escalation.lookForPivotInOtherLines(matriz, 0)
    assert x == len(matriz)

def test_lookForPivotInOtherLine_2():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    x = escalation.lookForPivotInOtherLines(matriz, 0)
    assert x == 0

if __name__ == "__main__":
    test_escalation_findNotNull2()