import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl
from scipy.stats import kurtosis
import pathlib
import time
import os
import shortuuid
import warnings

import numpy as np
from scipy.stats import skew

def compute_moment4_and_variance(data):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            
            # Calculating the fourth moment (kurtosis)
            # The 'fisher=False' argument returns the excess kurtosis
            # If you need kurtosis without adjustment, set 'fisher=True'
            moment4 = kurtosis(data, fisher=False, bias=False)

            # Calculating the sample variance
            sample_variance = np.var(data, ddof=1)

        return moment4, sample_variance

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error occurred: {e}")
        return None, None


# def fuzzer(low, high, input_type):
def fuzzer(input_type):
    
    low = np.random.uniform(low=-20, high=-5, size=1).astype(int)
    high = np.random.uniform(low=5, high=20, size=1).astype(int)

    if input_type == 'int':
        size = np.random.uniform(low=2, high=15, size=1).astype(int)
        a = np.random.randint(low[0],high[0],size).tolist()
        
        moment3, sample_variance = compute_moment4_and_variance(a)
        
        return a, moment3, sample_variance
    

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')


if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxList
    auxList = []

    @click.command()
    # @click.option('-l', '--low', 'low')
    # @click.option('-h', '--high', 'high')
    @click.option('-it', '--input_type', 'input_type')
    @click.option('-t', '--t_end', 't_end')
    @click.option('-o', '--output', 'output', help = 'Output file name')

    # def main(low, high, input_type, t_end, output):
    def main(input_type, t_end, output):
    
        mainPath = str(pathlib.Path().absolute()) + '/' + 'inputs'
        print(mainPath)

        try:
            os.mkdir(mainPath)
        except:
            pass

        t_end = time.time() + float(t_end)
        index = 0
        while time.time() < t_end:
            # newInput = fuzzer(int(low),int(high), input_type)
            input_a, moment3, sample_variance = fuzzer(input_type)
            
            id = shortuuid.uuid(name = str(input_a) )

            mainDF = {
                'id': id,
                'td_size': len(input_a),
                'td_moment3': moment3,
                'td_sample_variance': sample_variance,
                'td_type_size': str(type(len(input_a))),
                'td_type_moment3': str(type(moment3)),
                'td_type_sample_variance': str(type(sample_variance)),
            }
            index = index + 1
            
            auxList.append(mainDF)
        
        df = pd.DataFrame(auxList)

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

main()
