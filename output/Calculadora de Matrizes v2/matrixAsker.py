from fractions import Fraction
from matrix import Matrix


def makeMatrix(quantLines, quantColumns):
    if quantLines <= 0 or quantColumns <= 0:
        raise ValueError("O tamanho da matriz precisa ser um valor positivo maior que 0")
    matrix = []
    for i in range(quantLines):
        matrix.append([])
        for j in range(quantColumns):
            matrix[i].append(Fraction(0))

    return Matrix(matrix)


def askMatrix(quantLines, quantColumns, userIO):
    matrixMade = makeMatrix(quantLines, quantColumns)
    for i in range(quantLines):
        for j in range(quantColumns):
            viewMatrix(matrixMade, userIO)
            while True:
                number = userIO.input(f"Informe o número da posição Matriz L{i + 1}, C{j + 1}:\n")
                if not number:
                    number = "0"
                try:
                    matrixMade[i][j] = Fraction(number)
                    break
                except ValueError as error:
                    print("Esse tipo de entrada não é permitido, informe o dado corretamente.")
                    continue

    return matrixMade


def viewMatrix(matrix, userIO):
    for i in range(matrix.numberOfLines()):
        for j in range(matrix.numberOfColumns()):
            userIO.print(matrix[i][j], end=" ")
        userIO.print("")


def makeIdentityMatrix(sizeOfMatrix):
    matrix = makeMatrix(sizeOfMatrix, sizeOfMatrix)
    for i in range(sizeOfMatrix):
        matrix[i][i] = Fraction(1)

    return matrix
