import escalation
import matrixAsker
from fractions import Fraction


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
    escalation.switchLines(matrizSwitched, 0, 1)
    assert matriz == [[Fraction(2, 1), Fraction(3, 1)], [Fraction(4, 1), Fraction(5, 1)]] and matrizSwitched == [
        [Fraction(4, 1), Fraction(5, 1)], [Fraction(2, 1), Fraction(3, 1)]]


def test_escalation_switchLines_size3():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    matrizSwitched = matriz.copy()
    escalation.switchLines(matrizSwitched, 1, 2)
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
    escalation.multiplyLineToAchievePivot(matriz, 0)
    assert matriz[0] == [Fraction(1, 1), Fraction(3, 2)]

def test_escalation_multiplyLine2():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    escalation.multiplyLineToAchievePivot(matriz, 1)
    assert matriz[1] == [Fraction(1, 1), Fraction(5, 14), Fraction(2, 14)]

def test_escalation_multiplyLine3():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "13/3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, i)
    escalation.multiplyLineToAchievePivot(matriz, 0)
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
    x = escalation.findNotNull(matriz, 0)
    assert x == 2

if __name__ == "__main__":
    test_escalation_findNotNull2()