class Matrix:

    # Умножение матриц
    def mn(self, aMatrix, bMatrix):
        res = []
        for i in range(len(aMatrix)):
            row = []
            for j in range(len(aMatrix[i])):
                sum = 0
                for k in range(len(bMatrix)):
                    sum += aMatrix[i][k] * bMatrix[k][j]
                row.append(sum)
            res.append(row)
        return res
    
    # Возведение матрицы в степень
    def powMatrix(self, matrix, p):
        oMat = Matrix()
        if p == 1:
            return matrix
        if p % 2 == 0:
            x = self.powMatrix(matrix, p / 2)
            return oMat.mn(x, x)
        return oMat.mn(matrix, self.powMatrix(matrix, p-1))

# Число Фибоначчи с помощью возведения матрицы в степень
def fastFib(n):
    oMat = Matrix()
    return oMat.powMatrix([[1, 1], [1, 0]], n)[0][1]