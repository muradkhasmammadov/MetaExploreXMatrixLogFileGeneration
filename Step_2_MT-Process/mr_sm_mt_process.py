import numpy as np
import random
import traceback

class MR_SM:
    """MR_SM: Multiply every element in two matrices by a constant."""
    def __init__(self, matrix_a, matrix_b, constant):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.constant = constant

    def followUpTD(self, matrix):
        return [[item * self.constant for item in row] for row in matrix]

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
