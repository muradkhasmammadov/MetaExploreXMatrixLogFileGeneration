class Array2DRowRealMatrix:
    def __init__(self, data):
        self.data = data

    def getRowDimension(self):
        return len(self.data)

    def getColumnDimension(self):
        return len(self.data[0]) if self.data else 0

    def add(self, other):
        if self.getRowDimension() != other.getRowDimension() or \
           self.getColumnDimension() != other.getColumnDimension():
            raise ValueError("Matrices are not addition compatible")

        row_dimension = self.getRowDimension()
        column_dimension = self.getColumnDimension()
        result_data = [[0 for _ in range(column_dimension)] for _ in range(row_dimension)]

        for i in range(row_dimension):
            for j in range(column_dimension):
                result_data[i][j] = self.data[i][j] + other.data[i][j]

        return Array2DRowRealMatrix(result_data)

def add(matrix_data1, matrix_data2):
    matrix1 = Array2DRowRealMatrix(matrix_data1)
    matrix2 = Array2DRowRealMatrix(matrix_data2)
    result_matrix = matrix1.add(matrix2)
    return result_matrix.data
