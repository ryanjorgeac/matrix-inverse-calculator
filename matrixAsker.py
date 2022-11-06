from fractions import Fraction


def makeMatrix(sizeOfMatrix):
    if sizeOfMatrix <= 0:
        raise ValueError("O tamanho da matriz precisa ser um valor positivo maior que 0")
    matrix = []
    for i in range(sizeOfMatrix):
        matrix.append([])
        for j in range(sizeOfMatrix):
            matrix[i].append(Fraction(0))

    return matrix


def askMatrix(sizeOfMatrix, userIO):
    matrixMade = makeMatrix(sizeOfMatrix)
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            viewMatrix(matrixMade, userIO)
            number = Fraction(userIO.input(f"Informe o número da posição Matriz L{i + 1}, C{j + 1}:\n"))
            matrixMade[i][j] = number

    return matrixMade


def viewMatrix(matrix, userIO):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            userIO.print(matrix[i][j], end=" ")
        userIO.print("")


def makeIdentityMatrix(sizeOfMatrix):
    matrix = makeMatrix(sizeOfMatrix)
    for i in range(sizeOfMatrix):
        matrix[i][i] = Fraction(1)

    return matrix
