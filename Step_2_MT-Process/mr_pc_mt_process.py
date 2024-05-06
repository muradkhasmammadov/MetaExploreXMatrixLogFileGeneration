import numpy as np
import random
import traceback

class MR_PC:
    """
    MR_PC (Permutation of Columns): Shuffle the order of columns in each of the matrices.
    """
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
    
    def followUpTD(self, matrix):
        # Transpose, shuffle, and transpose back to permute columns
        transposed = np.transpose(matrix).tolist()
        random.shuffle(transposed)
        return np.transpose(transposed).tolist()

    def mrChecker(self, outputTD_a, outputTD_b):
        self.ttd_a = self.followUpTD(self.matrix_a)
        self.ttd_b = self.followUpTD(self.matrix_b)
        self.outputTD_a = outputTD_a
        self.outputTD_b = outputTD_b
        
        try:
            if self.outputTD_a == self.ttd_a and self.outputTD_b == self.ttd_b:
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
