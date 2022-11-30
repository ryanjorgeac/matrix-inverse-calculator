import augmentedMatrix
import escalation
import matrixAsker
from fractions import Fraction

import maybe
from nnInvertibleException import nnInvertibleException
from TheresNoNotNullElementException import TheresNoNotNullElementException
from matrix import Matrix

class inputFake:
    def __init__(self, lista):
        self.inputList = lista
        self.outputList = []

    def input(self, prompt):
        return self.inputList.pop()

    def print(self, prompt, end=None):
        self.outputList.append(prompt)


def test_escalation_multiplyLine1():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    identityMatrix = escalation.makeIdentityMatrix(2)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.multiplyLineToAchievePivot(augMatrix, 0)
    assert matriz[0] == [Fraction(1, 1), Fraction(3, 2)]


def test_escalation_multiplyLine2():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "13/3"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)
    identityMatrix = escalation.makeIdentityMatrix(3)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.multiplyLineToAchievePivot(augMatrix, 1)
    assert matriz[1] == [Fraction(1, 1), Fraction(5, 14), Fraction(2, 14)]


def test_escalation_multiplyLine3():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "13/3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)
    identityMatrix = escalation.makeIdentityMatrix(3)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.multiplyLineToAchievePivot(augMatrix, 0)
    assert matriz[0] == [Fraction(0, 1), Fraction(1, 1), Fraction(3, 26)]


def test_escalation_findNotNull1():
    numbers = ["5", "4", "3", "2"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    x = escalation.findNotNullOnLine(matriz, 0)
    assert x.orElseThrow(AssertionError) == 0


def test_escalation_findNotNullOnLine2():
    numbers = ["5", "4", "3", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    x = escalation.findNotNullOnLine(matriz, 0)
    assert x.orElseThrow(AssertionError) == 1


def test_escalation_findNotNullOnLine3():
    numbers = ["5", "4", "0", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    x = escalation.findNotNullOnLine(matriz, 0)
    assert maybe.isNothing(x)

def test_escalation_findNotNullOnColumn1():
    numbers = ["5", "4", "0", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    try:
        index = escalation.findNotNullOnColumn(matriz, 0, 0).orElseThrow(TheresNoNotNullElementException("Elemento não existe: TESTE"))
        assert index == 1
    except TheresNoNotNullElementException as error:
        assert error.__str__() == "Elemento não existe: TESTE"

def test_escalation_findNotNullOnColumn2():
    numbers = ["5", "0", "5", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    try:
        index = escalation.findNotNullOnColumn(matriz, 0, 0).orElseThrow(TheresNoNotNullElementException("Elemento não existe: TESTE"))
        assert index is None
    except TheresNoNotNullElementException as error:
        assert error.__str__() == "Elemento não existe: TESTE"


def test_putZerosInColumn_1():
    numbers = ["5", "4", "3", "2", "5", "14", "1/2", "0", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)                        # [Fraction(1, 1), Fraction(0, 1), Fraction(1, 2)]
    identityMatrix = escalation.makeIdentityMatrix(3)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.putZerosInColumn(augMatrix, 0, 0)      # [Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)]
    assert matriz[1][0] == Fraction(0, 1) and matriz[2][0] == Fraction(0, 1) and matriz[0][0] == Fraction(1, 1)


def test_putZerosInColumn_2():
    numbers = ["1", "4", "3", "2", "1", "14", "1/2", "0", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)                        # [Fraction(1, 1), Fraction(0, 1), Fraction(1, 2)]
    identityMatrix = escalation.makeIdentityMatrix(3)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)# [Fraction(14, 1), Fraction(1, 1), Fraction(2, 1)]
    escalation.putZerosInColumn(augMatrix, 1, 1)      # [Fraction(3, 1), Fraction(4, 1), Fraction(1, 1)]
    assert matriz[0][1] == Fraction(0, 1) and matriz[2][1] == Fraction(0, 1) and matriz[1][1] == Fraction(1, 1)


def test_putZerosInColumn_3():
    numbers = ["1", "4", "3", "2", "1", "14", "1/2", "0", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)                    # [Fraction(1, 1), Fraction(0, 1), Fraction(1, 2)]
    identityMatrix = escalation.makeIdentityMatrix(3)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)# [Fraction(14, 1), Fraction(5, 1), Fraction(2, 1)]
    escalation.putZerosInColumn(augMatrix, 2, 2)  # [Fraction(3, 1), Fraction(4, 1), Fraction(1, 1)]
    assert matriz[0][2] == Fraction(0, 1) and matriz[1][2] == Fraction(0, 1) and matriz[2][2] == Fraction(1, 1)


def test_putZerosInColumn_5():
    numbers = ["1", "4", "3", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)                    # [Fraction(4, 1), Fraction(3, 1)]
    identityMatrix = escalation.makeIdentityMatrix(2)        # [Fraction(1, 1), Fraction(1, 1)]
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.putZerosInColumn(augMatrix, 0, 0)
    assert matriz[1][0] == Fraction(0, 1) and matriz[1][1] == Fraction(-11, 1) and matriz[0][0] == Fraction(1, 1)


def test_escalation_3x3():
    numbers = ["10", "8", "7", "6", "5", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(3, 3, i)
    result = escalation.escalation(matriz)
    assert result.secondMatrix() == Matrix([[Fraction(-2, 3), Fraction(-4, 3), Fraction(1, 1)],
                                            [Fraction(-2, 3), Fraction(11, 3), Fraction(-2, 1)],
                                            [Fraction(1, 1), Fraction(-2, 1), Fraction(1, 1)]])


def test_escalation_2x2():
    numbers = ["5", "4", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    result = escalation.escalation(matriz)
    assert result.secondMatrix() == Matrix([[Fraction(-5, 3), Fraction(2, 3)], [Fraction(4, 3), Fraction(-1, 3)]])


def test_escalation_2x2_no_solution():
    numbers = ["0", "1", "0", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(2, 2, i)
    x = escalation.escalation(matriz)
    assert x.firstMatrix() == Matrix([[Fraction(1, 1), Fraction(0, 1)],
                                    [Fraction(0, 1), Fraction(0, 1)]])


def test_escalation_4x4():
    numbers = ["0", "0", "0", "0", "1", "0", "0", "0", "3", "2", "0", "0", "3", "4", "5", "0"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    # augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, matrixAsker.makeIdentityMatrix(4))
    result = escalation.escalation(matriz)
    assert result.firstMatrix().getMatrix() == Matrix([[Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
                                                        [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
                                                        [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)],
                                                        [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]]).getMatrix()


def test_escalation_4x4_full_of_zeros():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    result = escalation.escalation(matriz)
    assert result.secondMatrix() == Matrix([[Fraction(-1, 1), Fraction(37, 14), Fraction(-23, 14), Fraction(1, 7)],
                                            [Fraction(0, 1), Fraction(-9, 14), Fraction(9, 14), Fraction(-1, 7)],
                                            [Fraction(2, 1), Fraction(-121, 14), Fraction(79, 14), Fraction(-1, 7)],
                                            [Fraction(-1, 1), Fraction(43, 7), Fraction(-29, 7), Fraction(1, 7)]])


def test_escalation_4x4_makePivotOnColumn_0():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, matrixAsker.makeIdentityMatrix(4))
    escalation.makePivotOnColumn(augMatrix, 0, 0)
    assert matriz[0] == [1, 2, 3,  4]


def test_escalation_4x4_makePivotOnColumn_0_plus_putZerosInColumn():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    identityMatrix = escalation.makeIdentityMatrix(4)
    augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.makePivotOnColumn(augmentedMatrixExample, 0, 0)
    escalation.putZerosInColumn(augmentedMatrixExample, 0, 0)
    assert matriz[1][0] == Fraction(0) and matriz[2][0] == Fraction(0) and matriz[3][0] == Fraction(0)


def test_escalation_4x4_makePivotOnColumn_1():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    identityMatrix = escalation.makeIdentityMatrix(4)
    augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.makePivotOnColumn(augmentedMatrixExample, 0, 0)
    escalation.putZerosInColumn(augmentedMatrixExample, 0, 0)
    escalation.makePivotOnColumn(augmentedMatrixExample, 1, 1)
    assert matriz[1] == [Fraction(0), Fraction(1), Fraction(7, 3), Fraction(10, 3)]


def test_escalation_4x4_makePivotOnColumn_1_plus_putZerosInColumn():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    identityMatrix = escalation.makeIdentityMatrix(4)
    augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.makePivotOnColumn(augmentedMatrixExample, 0, 0)
    escalation.putZerosInColumn(augmentedMatrixExample, 0, 0)
    escalation.makePivotOnColumn(augmentedMatrixExample, 1, 1)
    escalation.putZerosInColumn(augmentedMatrixExample, 1, 1)
    assert matriz[0][1] == Fraction(0) and matriz[2][1] == Fraction(0) and matriz[3][1] == Fraction(0)


def test_escalation_4x4_makePivotOnColumn_2():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    identityMatrix = escalation.makeIdentityMatrix(4)
    augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.makePivotOnColumn(augmentedMatrixExample, 0, 0)
    escalation.putZerosInColumn(augmentedMatrixExample, 0, 0)
    escalation.makePivotOnColumn(augmentedMatrixExample, 1, 1)
    escalation.putZerosInColumn(augmentedMatrixExample, 1, 1)
    escalation.makePivotOnColumn(augmentedMatrixExample, 2, 2)
    assert matriz[2] == [Fraction(0), Fraction(0), Fraction(1), Fraction(1)]


def test_escalation_4x4_makePivotOnColumn_2_plus_putZerosInColumn():
    numbers = ["9", "9", "2", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "2", "1"]
    i = inputFake(numbers)
    matriz = matrixAsker.askMatrix(4, 4, i)
    identityMatrix = escalation.makeIdentityMatrix(4)
    augmentedMatrixExample = augmentedMatrix.AugmentedMatrix(matriz, identityMatrix)
    escalation.makePivotOnColumn(augmentedMatrixExample, 0, 0)
    escalation.putZerosInColumn(augmentedMatrixExample, 0, 0)
    escalation.makePivotOnColumn(augmentedMatrixExample, 1, 1)
    escalation.putZerosInColumn(augmentedMatrixExample, 1, 1)
    escalation.makePivotOnColumn(augmentedMatrixExample, 2, 2)
    escalation.putZerosInColumn(augmentedMatrixExample, 2, 2)
    assert matriz[0][2] == Fraction(0) and matriz[1][2] == Fraction(0) and matriz[3][2] == Fraction(0)


def test_putZerosInColumn_8():
    numbers = ["9", "1", "2", "9"]                  # 9 2
    i = inputFake(numbers)                          # 1 9
    matriz = matrixAsker.askMatrix(2, 2, i)
    augMatrix = augmentedMatrix.AugmentedMatrix(matriz, matrixAsker.makeIdentityMatrix(2))
    escalation.putZerosInColumn(augMatrix, 1, 0)
    assert matriz.getMatrix() == [[Fraction(0, 1), Fraction(-79, 1)],
                                  [Fraction(1, 1), Fraction(9, 1)]]


if __name__ == "__main__":
    test_escalation_4x4()