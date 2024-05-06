import numpy as np
import random
import traceback

class MR_MS:
    """
    MR_MS (Multiplication to a Subset): Multiply a randomly selected subset of elements in two matrices by a constant.
    """
    def __init__(self, matrix_a, matrix_b, constant, subset_size):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.constant = constant
        self.subset_size = subset_size

    def followUpTD(self, matrix):
        flat_list = [item for sublist in matrix for item in sublist]
        indices = random.sample(range(len(flat_list)), min(self.subset_size, len(flat_list)))
        for idx in indices:
            flat_list[idx] *= self.constant
        return np.reshape(flat_list, (len(matrix), len(matrix[0]))).tolist()

    def mrChecker(self, outputTD_a, outputTD_b):
        self.outputTD_a = outputTD_a  # Store outputTD_a as an instance variable
        self.outputTD_b = outputTD_b  # Store outputTD_b as an instance variable
        self.ttd_a = self.followUpTD(self.matrix_a)
        self.ttd_b = self.followUpTD(self.matrix_b)
        
        try:
            # Correctly use np.all() with np.isclose() to compare arrays properly
            if np.all(np.isclose(self.outputTD_a, self.ttd_a)) and np.all(np.isclose(self.outputTD_b, self.ttd_b)):
                self.vs = 0
                self.vs_string = 'No-violate'
            else:
                self.vs = 1
                self.vs_string = 'Violate'
            return self.mrCheckerResult()
        
        except TypeError:
            self.vs = 'error'
            self.vs_string = 'error'
            return self.mrCheckerResult()

    def mrCheckerResult(self):
        return {
            'td_a': self.matrix_a,
            'td_b': self.matrix_b,
            'ttd_a': self.ttd_a,
            'ttd_b': self.ttd_b,
            'td_output_a': self.outputTD_a,  # Use the stored output variable
            'td_output_b': self.outputTD_b,  # Use the stored output variable
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
