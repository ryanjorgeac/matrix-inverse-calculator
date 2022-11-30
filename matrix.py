class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __getitem__(self, line):
        return self.matrix[line]

    def __setitem__(self, line, value):
        self.matrix[line] = value

    def __eq__(self, otherMatrix):
        return self.matrix == otherMatrix.matrix

    def getMatrix(self):
        return self.matrix

    def numberOfLines(self):
        return len(self.matrix)

    def numberOfColumns(self):
        return len(self.matrix[0])