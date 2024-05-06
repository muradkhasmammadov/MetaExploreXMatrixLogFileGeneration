import numpy as np
import random
import traceback

class MR_PR:
    """ MR_PR
    Change in the input -> Permute the order of rows in each matrix.
    Expected change in the output -> Remain constant
    """
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
    
    def followUpTD(self, matrix):
        matrix_copy = matrix.copy()
        random.shuffle(matrix_copy)
        return matrix_copy

    def mrChecker(self, outputTD_a, outputTD_b):
        self.ttd_a = self.followUpTD(self.matrix_a)
        self.ttd_b = self.followUpTD(self.matrix_b)
        self.outputTD_a = outputTD_a
        self.outputTD_b = outputTD_b
        
        try:
            if outputTD_a == self.ttd_a and outputTD_b == self.ttd_b:
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

