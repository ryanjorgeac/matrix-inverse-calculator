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
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            userIO.print(matrix[i][j], end=" ")
        userIO.print("")


def makeIdentityMatrix(sizeOfMatrix):
    matrix = makeMatrix(sizeOfMatrix)
    for i in range(sizeOfMatrix):
        matrix[i][i] = Fraction(1)

    return matrix
