from matrixAsker import *
import inputIO


class inputFake:
    def __init__(self, lista):
        self.inputList = lista
        self.outputList = []

    def input(self, prompt):
        return self.inputList.pop()

    def print(self, prompt, end=None):
        self.outputList.append(prompt)


def test_viewMatrix_1():
    numbers = ["5"]
    i = inputFake(numbers)
    a = askMatrix(1, i)
    v = viewMatrix(1, a, i)
    assert i.outputList == [Fraction(0, 1), "", Fraction(5, 1), ""]

def test_viewMatrix_2():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    a = askMatrix(2, i)
    v = viewMatrix(2, a, i)
    assert i.outputList == [0, 0, "", 0, 0, "", 2, 0, "", 0, 0, "", 2, 3, "", 0, 0, "", 2, 3, "", 4, 0, "", 2, 3, "", 4, 5, ""]
