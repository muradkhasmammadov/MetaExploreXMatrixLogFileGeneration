import random
import json
import math

import numpy as np
import random

def MR_PE(matrix_a, matrix_b):
    """ 
    MR_PE (Permutation of Elements): Shuffle all elements in both matrices
    while preserving their dimensions.
    """
    def permute_elements(matrix):
        flat_list = [item for sublist in matrix for item in sublist]
        random.shuffle(flat_list)
        return np.reshape(flat_list, (len(matrix), len(matrix[0]))).tolist()

    return permute_elements(matrix_a), permute_elements(matrix_b)

def MR_PR(matrix_a, matrix_b):
    """ 
    MR_PR (Permutation of Rows): Shuffle the order of rows in both matrices.
    """
    def permute_rows(matrix):
        matrix_copy = matrix.copy()
        random.shuffle(matrix_copy)
        return matrix_copy

    return permute_rows(matrix_a), permute_rows(matrix_b)

def MR_PC(matrix_a, matrix_b):
    """
    MR_PC (Permutation of Columns): Shuffle the order of columns in both matrices.
    """
    def permute_columns(matrix):
        transposed = np.transpose(matrix).tolist()
        random.shuffle(transposed)
        return np.transpose(transposed).tolist()

    return permute_columns(matrix_a), permute_columns(matrix_b)

def MR_SA(matrix_a, matrix_b, constant):
    """ 
    MR_SA (Scalar Addition): Add a constant to every element in both matrices.
    """
    def scalar_addition(matrix, const):
        return [[item + const for item in row] for row in matrix]

    return scalar_addition(matrix_a, constant), scalar_addition(matrix_b, constant)

def MR_AM(matrix_a, matrix_b):
    """
    MR_AM (Addition of Matrices): Perform element-wise addition of two matrices
    of the same dimensions.
    """
    return (np.array(matrix_a) + np.array(matrix_b)).tolist(), (np.array(matrix_b) + np.array(matrix_a)).tolist()

def MR_AS(matrix_a, matrix_b, constant, subset_size):
    """
    MR_AS (Addition to a Subset): Add a constant to a randomly selected subset of elements within both matrices.
    """
    def add_to_subset(matrix, const, size):
        flat_list = [item for sublist in matrix for item in sublist]
        indices = random.sample(range(len(flat_list)), size)
        for idx in indices:
            flat_list[idx] += const
        return np.reshape(flat_list, (len(matrix), len(matrix[0]))).tolist()

    return add_to_subset(matrix_a, constant, subset_size), add_to_subset(matrix_b, constant, subset_size)

def MR_SM(matrix_a, matrix_b, constant):
    """
    MR_SM (Scalar Multiplication): Multiply every element in both matrices by a constant.
    """
    def scalar_multiplication(matrix, const):
        return [[item * const for item in row] for row in matrix]

    return scalar_multiplication(matrix_a, constant), scalar_multiplication(matrix_b, constant)

def MR_MS(matrix_a, matrix_b, constant, subset_size):
    """
    MR_MS (Multiplication to a Subset): Multiply a randomly selected subset of elements in both matrices by a constant.
    """
    def multiply_subset(matrix, const, size):
        flat_list = [item for sublist in matrix for item in sublist]
        indices = random.sample(range(len(flat_list)), size)
        for idx in indices:
            flat_list[idx] *= const
        return np.reshape(flat_list, (len(matrix), len(matrix[0]))).tolist()

    return multiply_subset(matrix_a, constant, subset_size), multiply_subset(matrix_b, constant, subset_size)


    
def save_json(json_object, output_file):
    with open(output_file, "w") as json_file:
        json.dump(json_object, json_file, indent=4)
    print("JSON object saved to", output_file)
    
import click
import json
import random

global auxList
auxList = []

@click.command()
@click.option('-i', '--input_path', required=True, help="Input JSON file path containing matrices.")
@click.option('-o', '--output_file', required=True, help="Output JSON file path to save transformed matrices.")
def main(input_path, output_file):
    with open(input_path, 'r') as file:
        data = json.load(file)

    for i in range(len(data)):
        td_a = data[str(i)]['td_a']
        td_b = data[str(i)]['td_b']

        data[str(i)]['td_ttd_a_MR_PE'], data[str(i)]['td_ttd_b_MR_PE'] = MR_PE(td_a, td_b)
        data[str(i)]['td_ttd_a_MR_PR'], data[str(i)]['td_ttd_b_MR_PR'] = MR_PR(td_a, td_b)
        data[str(i)]['td_ttd_a_MR_PC'], data[str(i)]['td_ttd_b_MR_PC'] = MR_PC(td_a, td_b)
        data[str(i)]['td_ttd_a_MR_SA'], data[str(i)]['td_ttd_b_MR_SA'] = MR_SA(td_a, td_b, 5)
        data[str(i)]['td_ttd_a_MR_AM'], data[str(i)]['td_ttd_b_MR_AM'] = MR_AM(td_a, td_b)
        data[str(i)]['td_ttd_a_MR_AS'], data[str(i)]['td_ttd_b_MR_AS'] = MR_AS(td_a, td_b, 5, len(td_a) * len(td_a[0]) // 4)
        data[str(i)]['td_ttd_a_MR_SM'], data[str(i)]['td_ttd_b_MR_SM'] = MR_SM(td_a, td_b, 2)
        data[str(i)]['td_ttd_a_MR_MS'], data[str(i)]['td_ttd_b_MR_MS'] = MR_MS(td_a, td_b, 2, len(td_a) * len(td_a[0]) // 4)

    save_json(data, output_file)

if __name__ == '__main__':
    main()