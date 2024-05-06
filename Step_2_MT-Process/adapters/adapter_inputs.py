from mr_pe_mt_process import MR_PE
from mr_pr_mt_process import MR_PR
from mr_pc_mt_process import MR_PC
from mr_sa_mt_process import MR_SA
from mr_am_mt_process import MR_AM
from mr_as_mt_process import MR_AS
from mr_sm_mt_process import MR_SM
from mr_ms_mt_process import MR_MS

class AdapterInputs():
    def __init__(self, test_data_one_input, test_data_two_input):
        self.test_data_one_input = test_data_one_input
        self.test_data_two_input = test_data_two_input

    def _mr_pe(self):
        return MR_PE(self.test_data_one_input, self.test_data_two_input).followUpTD()
        
    def _mr_pr(self):
        return MR_PR(self.test_data_one_input, self.test_data_two_input).followUpTD()

    def _mr_pc(self):
        return MR_PC(self.test_data_one_input, self.test_data_two_input).followUpTD()

    def _mr_sa(self, const):
        return MR_SA(self.test_data_one_input, self.test_data_two_input, const).followUpTD()

    def _mr_am(self):
        return MR_AM(self.test_data_one_input, self.test_data_two_input).followUpTD()

    def _mr_as(self, const, subset_size):
        return MR_AS(self.test_data_one_input, self.test_data_two_input, const, subset_size).followUpTD()

    def _mr_sm(self, const):
        return MR_SM(self.test_data_one_input, self.test_data_two_input, const).followUpTD()

    def _mr_ms(self, const, subset_size):
        return MR_MS(self.test_data_one_input, self.test_data_two_input, const, subset_size).followUpTD()

    def ttd_all_mrs(self, const):
        subset_size = len(self.test_data_one_input) * len(self.test_data_one_input[0]) // 4  # Example calculation
        return {
            'td_a': self.test_data_one_input,
            'td_b': self.test_data_two_input,
            'ttd_mr_pe': self._mr_pe(),
            'ttd_mr_pr': self._mr_pr(),
            'ttd_mr_pc': self._mr_pc(),
            'ttd_mr_sa': self._mr_sa(const),
            'ttd_mr_am': self._mr_am(),
            'ttd_mr_as': self._mr_as(const, subset_size),
            'ttd_mr_sm': self._mr_sm(const),
            'ttd_mr_ms': self._mr_ms(const, subset_size),
        }
