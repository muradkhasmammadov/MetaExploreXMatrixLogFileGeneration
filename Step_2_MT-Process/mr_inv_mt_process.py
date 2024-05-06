import math
import traceback

class MR_INV():
    """ MR MR_INV 
    Change in the input -> Take the inverse of each element 
    Expected change in the output -> Decrease or remain constant
    """
    
    ttd = None
    vs = None
    vs_string = None
    td_output = None
    ttd_output = None
    
    def __init__(self, test_data_one_input):
        self.test_data_one_input = test_data_one_input
    
    def followUpTD(self):
        aux_list = []

        # Check if the input data is a list and not empty
        if len(self.test_data_one_input) != 0 and isinstance(self.test_data_one_input, list):    
            for sublist in self.test_data_one_input:
                # Ensure sublist is actually a list of numbers
                if isinstance(sublist, list):
                    sub_aux_list = []
                    for item in sublist:
                        if item != 0:
                            sub_aux_list.append(1 / item)
                        else:
                            sub_aux_list.append('ZeroDivisionError')  # or float('inf') for mathematical handling
                    aux_list.append(sub_aux_list)
                else:
                    raise ValueError("Each item must be a list of numbers.")
        
        return aux_list

    
    def mrChecker(self, outputTD, outputTTD):
        error_message = None

        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()
        
        try:
            if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0) or outputTD > outputTTD:
                self.vs = 0
                self.vs_string = 'No-violate'
            
            else:
                self.vs = 1
                self.vs_string = 'Violate'
                
            return self.mrCheckerResult()

        except TypeError:
            error_message = traceback.format_exc()
            self.vs = 'error'
            self.vs_string = 'error'
            return self.mrCheckerResult()

    def mrCheckerResult(self):
        
        return {
            'td' : self.test_data_one_input,
            'ttd': self.ttd,
            'td_output': self.td_output,
            'ttd_output': self.ttd_output,
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
        
            
            