# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:08:04 2021

@author: mnaganuma
"""

import sys
import pandas as pd
import pickle


def csv2pkl(input_filename, output_filename):
    print('Converted csv --> pkl.')
    df = pd.read_csv(input_filename)
    with open(output_filename, 'wb') as f:
        pickle.dump(df, f)


def tsv2pkl(input_filename, output_filename):
    print('Converted tsv --> pkl.')
    df = pd.read_table(input_filename)
    with open(output_filename, 'wb') as f:
        pickle.dump(df, f)


def pkl2csv(input_filename, output_filename):
    print('Converted pkl --> csv.')
    with open(input_filename, 'rb') as f:
        df = pickle.load(f)
    df.to_csv(output_filename, index=False)


def main(opt, input_filename, output_filename):
    if opt == 'c2p':
        csv2pkl(input_filename, output_filename)
    elif opt == 't2p':
        tsv2pkl(input_filename, output_filename)
    elif opt == 'p2c':
        pkl2csv(input_filename, output_filename)
    else:
        print('Option Error: option is c2p or p2c.')

    
if __name__ == '__main__':
    args = sys.argv
    
    if len(args) == 4:
        option = args[1]
        input_filename  = args[2]
        output_filename = args[3]
        main(option, input_filename, output_filename)
    else:
        print('usage: python csv2pkl.py option input_filename output_filenname')
        print('option : c2p ------ Csv file is converted to pkl file.')
        print('       : t2p ------ Tsv file is converted to pkl file.')
        print('       : p2c ------ Pkl file is converted to csv file.')
