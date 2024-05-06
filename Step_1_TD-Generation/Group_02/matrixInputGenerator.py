import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import pathlib
import time
import shortuuid
import json

def fuzzer(input_type):
    low = int(np.random.uniform(-20, -5))
    high = int(np.random.uniform(5, 20))

    if input_type == 'int':
        rows = np.random.randint(1, 10)
        cols = np.random.randint(1, 10)
        matrix_a = np.random.randint(low, high, size=(rows, cols)).tolist()
        matrix_b = np.random.randint(low, high, size=(rows, cols)).tolist()
        return matrix_a, matrix_b
    elif input_type == 'float':
        rows = np.random.randint(1, 10)
        cols = np.random.randint(1, 10)
        matrix = np.random.uniform(low, high, size=(rows, cols)).tolist()
        return matrix
    else:
        return []


def save_json(df, output, savePath):
    result = df.to_json(orient="index")
    parsed = json.loads(result)  # Convert JSON string to JSON object
    with open(os.path.join(savePath, output + '.json'), 'w') as f:
        json.dump(parsed, f, indent=4)

def save_csv(df, output, savePath):
    df.to_csv(os.path.join(savePath, output + '.csv'))

if __name__ == '__main__':
    import click 

    @click.command()
    @click.option('-it', '--input_type', 'input_type')
    @click.option('-t', '--t_end', 't_end')
    @click.option('-o', '--output', 'output', help='Output file name')

    def main(input_type, t_end, output):
        mainPath = str(pathlib.Path().absolute()) + '/inputs'
        if not os.path.exists(mainPath):
            os.makedirs(mainPath)

        t_end = time.time() + float(t_end)
        auxList = []

        while time.time() < t_end:
            inputs = fuzzer(input_type)
            if input_type == 'int':
                input_a, input_b = inputs
            elif input_type == 'float':
                input_a = inputs
                input_b = []

            id = shortuuid.uuid(name=str(input_a))
            data_dict = {
                'id': id,
                'td_a': input_a,
                'td_b': input_b,
                'td_type_a': str(type(input_a)),
                'td_type_b': str(type(input_b)),
                'size_td_a': len(input_a), 
                'size_td_b': len(input_b) if input_b else 0
            }
            auxList.append(data_dict)

        df = pd.DataFrame(auxList)
        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

    main()
