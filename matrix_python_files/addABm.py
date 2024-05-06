def add_matrices(matrix_data1, matrix_data2):
    if len(matrix_data1) != len(matrix_data2):
        raise ValueError("Matrices are not addition compatible: different number of rows")

    result_matrix = []

    for i in range(len(matrix_data1)):
        row1 = matrix_data1[i]
        row2 = matrix_data2[i]

        if len(row1) != len(row2):
            raise ValueError(f"Matrices are not addition compatible: row {i} has different lengths")

        row_result = []
        for j in range(len(row1)):
            # Check if both elements can be added, if not, handle the exception gracefully
            try:
                element1 = row1[j]
                element2 = row2[j]

                # Ensure both elements are numbers before attempting to add
                if (isinstance(element1, (int, float)) and isinstance(element2, (int, float))):
                    row_result.append(element1 + element2)
                else:
                    raise ValueError(f"Non-numeric data found in row {i}, column {j}")

            except TypeError as e:
                print(f"Error adding elements at row {i}, column {j}: {e}")
                row_result.append("Error")

        result_matrix.append(row_result)

    return result_matrix

# Example usage of the function with simplified data
matrix_data1 = [[1, 2], [3, 4]]
matrix_data2 = [[5, 6], [7, 8]]

try:
    result_matrix_data = add_matrices(matrix_data1, matrix_data2)
    print("Resultant Matrix:")
    for row in result_matrix_data:
        print(row)
except ValueError as e:
    print(e)