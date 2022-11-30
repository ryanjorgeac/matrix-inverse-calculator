class ElementaryOperation:
    def apply(self, matrix):
        raise NotImplementedError()

class swapTwoRows(ElementaryOperation):
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def apply(self, matrix):
        matrix[self.line1], matrix[self.line2] = matrix[self.line2], matrix[self.line1]

class multiplyRowByANonZeroScalar(ElementaryOperation):
    def __init__(self, nonZeroScalar, line):
        self.nonZeroScalar = nonZeroScalar
        self.line = line

    def apply(self, matrix):
        matrix[self.line] = [self.nonZeroScalar * element for element in matrix[self.line]]

class addToOneRowAScalarMultipleOfAnother(ElementaryOperation):
    def __init__(self, scalarMultiple, lineToBeIncremented, lineToBeMultiplied):
        self.scalar = scalarMultiple
        self.lineToBeIncremented = lineToBeIncremented
        self.lineToBeMultiplied = lineToBeMultiplied

    def apply(self, matrix):
        matrix[self.lineToBeIncremented] = [self.scalar * matrix[self.lineToBeMultiplied][i]
                                            + matrix[self.lineToBeIncremented][i] for i in range
                                            (len(matrix[self.lineToBeMultiplied]))]
