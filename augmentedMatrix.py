class AugmentedMatrix:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def __len__(self):
        return len(self.matrix1)

    def __getitem__(self, item):
        class LineOfAugmentedMatrix:
            def __init__(self, matrix1, matrix2, line):
                self.matrix1 = matrix1
                self.matrix2 = matrix2
                self.line = line

            def __getitem__(self, column):
                if column < len(self.matrix1[self.line]):
                    return self.matrix1[self.line][column]
                return self.matrix2[self.line][column-len(self.matrix1[self.line])]

        return LineOfAugmentedMatrix(self.matrix1, self.matrix2, item)

    def firstMatrix(self):
        return self.matrix1

    def secondMatrix(self):
        return self.matrix2

    def applyElementaryOperations(self, operation):
        operation.apply(self.matrix1)
        operation.apply(self.matrix2)
