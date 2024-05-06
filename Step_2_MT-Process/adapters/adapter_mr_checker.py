from mr_pe_mt_process import MR_PE
from mr_pr_mt_process import MR_PR
from mr_pc_mt_process import MR_PC
from mr_sa_mt_process import MR_SA
from mr_am_mt_process import MR_AM
from mr_as_mt_process import MR_AS
from mr_sm_mt_process import MR_SM
from mr_ms_mt_process import MR_MS

class AdapterMRchecker():
    
    def __init__(self, inputs_outputs, const):
        self.inputs_outputs = inputs_outputs
        self.test_data_one_input = inputs_outputs['td_a']
        self.test_data_two_input = inputs_outputs['td_b']  
        self.cons = const

    def _mr_pe(self):
        mr = MR_PE(self.test_data_one_input, self.test_data_two_input)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_pe'])
        
    def _mr_pr(self):
        mr = MR_PR(self.test_data_one_input, self.test_data_two_input)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_pr'])

    def _mr_pc(self):
        mr = MR_PC(self.test_data_one_input, self.test_data_two_input)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_pc'])

    def _mr_sa(self):
        mr = MR_SA(self.test_data_one_input, self.test_data_two_input, self.cons)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_sa'])

    def _mr_am(self):
        mr = MR_AM(self.test_data_one_input, self.test_data_two_input)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_am'])
         
    def _mr_as(self):
        mr = MR_AS(self.test_data_one_input, self.test_data_two_input, self.cons, len(self.test_data_one_input) * len(self.test_data_one_input[0]) // 4)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_as'])
    
    def _mr_sm(self):
        mr = MR_SM(self.test_data_one_input, self.test_data_two_input, self.cons)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_sm'])
    
    def _mr_ms(self):
        mr = MR_MS(self.test_data_one_input, self.test_data_two_input, self.cons, len(self.test_data_one_input) * len(self.test_data_one_input[0]) // 4)
        return mr.mrChecker(self.inputs_outputs['td_output'], self.inputs_outputs['ttd_output_mr_ms'])
    
    def all_mrs_checker(self):
        results = {
            'vs_str_mr_pe': self._mr_pe()['vs_str'],
            'vs_str_mr_pr': self._mr_pr()['vs_str'],
            'vs_str_mr_pc': self._mr_pc()['vs_str'],
            'vs_str_mr_sa': self._mr_sa()['vs_str'],
            'vs_str_mr_am': self._mr_am()['vs_str'],
            'vs_str_mr_as': self._mr_as()['vs_str'],
            'vs_str_mr_sm': self._mr_sm()['vs_str'],
            'vs_str_mr_ms': self._mr_ms()['vs_str'],
            'vs_mr_pe': self._mr_pe()['vs'],
            'vs_mr_pr': self._mr_pr()['vs'],
            'vs_mr_pc': self._mr_pc()['vs'],
            'vs_mr_sa': self._mr_sa()['vs'],
            'vs_mr_am': self._mr_am()['vs'],
            'vs_mr_as': self._mr_as()['vs'],
            'vs_mr_sm': self._mr_sm()['vs'],
            'vs_mr_ms': self._mr_ms()['vs']
        }
        # Update inputs_outputs with results
        self.inputs_outputs.update(results)
        return self.inputs_outputs
