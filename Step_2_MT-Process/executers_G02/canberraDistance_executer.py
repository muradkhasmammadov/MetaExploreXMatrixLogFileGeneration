from pathlib import Path
import pandas as pd
import traceback
import pathlib
import json
import sys
import os

all_methods_path = Path(__file__).parent / 'C:/Users/Murad/OneDrive - Khazar University/Desktop/Django_apps/SelectingConstrainingMRsScSoft/matrix_python_files'

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../executers'))
from adapters.adapter_inputs import AdapterInputs
from adapters.adapter_mr_checker import AdapterMRchecker

# Making sure the directory exists
if not all_methods_path.is_dir():
    raise ImportError(f"The directory {all_methods_path} does not exist")

# Add the parent directory of AllMethods to the Python path
sys.path.append(str(all_methods_path.parent))

from matrix_python_files.addABm import add_matrices

def _get_ttd(input):
    
    return AdapterInputs(test_data_one_input = input).ttd_all_mrs(const=2)

def _get_outputs(all_inputs):
    error_message = None
    
    inputs_outputs = all_inputs.copy()
    print(all_inputs)
    
    try:
        inputs_outputs['td_output'] = add_matrices(all_inputs['td_a'], all_inputs['td_b'] )
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['td_output'] = 'error'
    try:
        inputs_outputs['ttd_output_mr_pe'] = add_matrices(all_inputs['td_ttd_a_MR_PE'], all_inputs['td_ttd_b_MR_PE'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_pe'] = 'error'
        
    try:
        inputs_outputs['ttd_output_mr_pr'] = add_matrices(all_inputs['td_ttd_a_MR_PR'], all_inputs['td_ttd_b_MR_PR'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_pr'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_pc'] = add_matrices(all_inputs['td_ttd_a_MR_PC'], all_inputs['td_ttd_b_MR_PC'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_pc'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_sa'] = add_matrices(all_inputs['td_ttd_a_MR_SA'], all_inputs['td_ttd_b_MR_SA'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_sa'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_am'] = add_matrices(all_inputs['td_ttd_a_MR_AM'], all_inputs['td_ttd_b_MR_AM'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_am'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_as'] = add_matrices(all_inputs['td_ttd_a_MR_AS'], all_inputs['td_ttd_b_MR_AS'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_as'] = 'error'   
    
    try:
        inputs_outputs['ttd_output_mr_sm'] = add_matrices(all_inputs['td_ttd_a_MR_SM'], all_inputs['td_ttd_b_MR_SM'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_sm'] = 'error'   
    
    try:
        inputs_outputs['ttd_output_mr_ms'] = add_matrices(all_inputs['td_ttd_a_MR_MS'], all_inputs['td_ttd_b_MR_MS'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_ms'] = 'error'   
        
    return inputs_outputs

def mr_checker(inputs_outputs):
    
    return AdapterMRchecker(inputs_outputs,2).all_mrs_checker()

def save_json(df, output, savePath):
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")
    print('*** Done ***')
    print('Saved in: ', savePath + '/' + output + '.json')

def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')
    print('Saved in: ', savePath + '/' + output + '.csv')
    print('*****')

if __name__ == '__main__':
    
    import click
    
    global mainDF
    mainDF = pd.DataFrame()
    
    global auxList
    auxList = []
    
    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output_file', 'output_file')

    def main(input_path, output_file):
        
        mainPathMRChecker = str(pathlib.Path().absolute()) + '/' + 'Logs'

        try:
            os.mkdir(mainPathMRChecker)
        except:
            pass
        
        with open(input_path, 'r') as readfiles:
            inputs = json.load(readfiles)
            json.dumps(inputs, indent=4)
            
        for i in range(0, len(inputs)):

            all_inputs = {
                'td_a' : inputs[str(i)]['td_a'],
                'td_b' :inputs[str(i)]['td_b'],
                'td_ttd_a_MR_PE' :inputs[str(i)]['td_ttd_a_MR_PE'],
                'td_ttd_b_MR_PE' : inputs[str(i)]['td_ttd_b_MR_PE'],
                'td_ttd_a_MR_PR' :inputs[str(i)]['td_ttd_a_MR_PR'],
                'td_ttd_b_MR_PR' : inputs[str(i)]['td_ttd_b_MR_PR'],
                'td_ttd_a_MR_PC' :inputs[str(i)]['td_ttd_a_MR_PC'],
                'td_ttd_b_MR_PC' : inputs[str(i)]['td_ttd_b_MR_PC'],
                'td_ttd_a_MR_SA' :inputs[str(i)]['td_ttd_a_MR_SA'],
                'td_ttd_b_MR_SA' : inputs[str(i)]['td_ttd_b_MR_SA'],
                'td_ttd_a_MR_AM' :inputs[str(i)]['td_ttd_a_MR_AM'],
                'td_ttd_b_MR_AM' : inputs[str(i)]['td_ttd_b_MR_AM'],
                'td_ttd_a_MR_AS' :inputs[str(i)]['td_ttd_a_MR_AS'],
                'td_ttd_b_MR_AS' : inputs[str(i)]['td_ttd_b_MR_AS'],
                'td_ttd_a_MR_SM' : inputs[str(i)]['td_ttd_a_MR_SM'],
                'td_ttd_b_MR_SM' : inputs[str(i)]['td_ttd_b_MR_SM'],
                'td_ttd_a_MR_MS' : inputs[str(i)]['td_ttd_a_MR_MS'],
                'td_ttd_b_MR_MS' : inputs[str(i)]['td_ttd_b_MR_MS']
            }            

            input_outputs = _get_outputs(all_inputs)
            # ttd_outputs = _get_outputs(ttd_a, ttd_b)
            checkers = mr_checker(input_outputs)
            
            auxList.append(checkers)

        final_df = pd.DataFrame(auxList)
        
        save_csv(final_df, output_file, mainPathMRChecker)
        save_json(final_df, output_file, mainPathMRChecker)
        
main()
    