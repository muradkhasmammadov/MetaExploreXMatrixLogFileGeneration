import numpy as np
import random
import traceback

class MR_AS:
    """MR_AS: Add a constant to a subset of elements in two matrices."""
    def __init__(self, matrix_a, matrix_b, constant, subset_size):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.constant = constant
        self.subset_size = subset_size

    def followUpTD(self, matrix):
        flat_list = [item for sublist in matrix for item in sublist]
        indices = random.sample(range(len(flat_list)), min(self.subset_size, len(flat_list)))
        for idx in indices:
            flat_list[idx] += self.constant
        return np.reshape(flat_list, (len(matrix), len(matrix[0]))).tolist()

    def mrChecker(self, outputTD_a, outputTD_b):
        self.outputTD_a = outputTD_a  
        self.outputTD_b = outputTD_b  
        self.ttd_a = self.followUpTD(self.matrix_a)
        self.ttd_b = self.followUpTD(self.matrix_b)
        
        try:
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
            'td_output_a': self.outputTD_a, 
            'td_output_b': self.outputTD_b,  
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
