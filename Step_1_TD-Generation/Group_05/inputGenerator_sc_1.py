import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl
import pathlib
import time
import os
import shortuuid


# def fuzzer(low, high, input_type):
def fuzzer(input_type):
    
    low = np.random.uniform(low=-20, high=-5, size=1).astype(int)
    high = np.random.uniform(low=5, high=20, size=1).astype(int)

    if input_type == 'int':
        # Generate a random size for the array (as an integer)
        size = int(np.random.uniform(low=1, high=15))

        a = np.random.randint(low[0],high[0],size).tolist()
        # Calculate the mean of the array
        try:
            b = np.mean(a)
        except (TypeError, ValueError, ZeroDivisionError, RuntimeWarning):
            b = None

        return a, b
    
    if input_type == 'float':
        size = np.random.uniform(low=0, high=15, size=1).astype(int)
        a = np.random.random(size).tolist()
        return a
    else:
        return 0

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
            input_a, input_b = fuzzer(input_type)
            
            id = shortuuid.uuid(name = str(input_a) )

            mainDF = {
                'id': id,
                'td_a': input_a,
                'td_b': input_b,
                'td_type_a': str(type(input_a)),
                'td_type_b': str(type(input_b)),
                'size_td_a': len(input_a)}
            index = index + 1
            
            auxList.append(mainDF)
        
        df = pd.DataFrame(auxList)

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

main()
