#!/usr/bin/env python
# coding: utf-8


parag_windows = 'C:\\Users\\parag\\Dropbox (Personal)\\sub_lot_paper\\source_code\\'
parag_mac = '/Users/paragsiddique/LoDI Dropbox/sub_lot_paper/source_code/'
import sys
sys.path.append(parag_windows)


from parking_env.parking_lot import *
from parking_env.sub_lot import *
from parking_env.traditional_lot import *
from parking_env.retrieval_algorithms import *
from parking_env.sub_lot_utils import *
from parking_env.utils import *
from parking_env.sub_lot_cost_function import *


sub_lot_10x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), ((0, 5), (1, 5)),
               ((0, 6), (1, 6)), ((0, 7), (1, 7)), ((0, 8), (1, 8)), ((0, 9), (1, 9)),
               ((2, 0), (2, 1)), ((2, 2), (2, 3)), ((2, 6), (2, 7)), ((2, 8), (2, 9)))

sub_lot_9x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), ((0, 5), (1, 5)),
               ((0, 6), (1, 6)), ((0, 7), (1, 7)), ((0, 8), (1, 8)),
               ((2, 0), (2, 1)), ((2, 2), (2, 3)), ((2, 7), (2, 8)))

sub_lot_8x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), ((0, 5), (1, 5)),
               ((0, 6), (1, 6)), ((0, 7), (1, 7)), 
               ((2, 0), (2, 1)), ((2, 2), (2, 3)), ((2, 6), (2, 7)))

sub_lot_7x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), ((0, 5), (1, 5)),
               ((0, 6), (1, 6)), 
               ((2, 0), (2, 1)), ((2, 5), (2, 6)))

sub_lot_6x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), ((0, 5), (1, 5)),
               ((2, 0), (2, 1)), ((2, 4), (2, 5)))

sub_lot_5x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (1, 4)), 
               ((2, 0), (2, 1)))

sub_lot_4x3 = (((0, 0), (1, 0)), ((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((2, 0), (2, 1)))

sub_lot_3x3 = (((1, 0), (2, 0)), ((1, 1), (2, 1)), ((1, 2), (2, 2)))  

def main():

    states = [sub_lot_3x3, sub_lot_4x3, sub_lot_5x3, sub_lot_6x3, 
              sub_lot_7x3, sub_lot_8x3, sub_lot_9x3, sub_lot_10x3] 
    
    states_names = ['sub_lot_3x3', 'sub_lot_4x3', 'sub_lot_5x3', 'sub_lot_6x3', 
              'sub_lot_7x3', 'sub_lot_8x3', 'sub_lot_9x3', 'sub_lot_10x3'] 
    
    rows_list = [3, 4, 5, 6, 7, 8, 9, 10]
    
    columns = 3
    
    sub_lot_col_03_results = {}
    for state, rows, states_name in zip(states, rows_list, states_names):
        try:
            sub_lot_results = comp_cost(state, columns, rows)
            # while writing the function I missplaced columns and row positions, later never changed the code
            print(states.index(state))
            sub_lot_col_03_results[states_name] = sub_lot_results
        except:
            pass
    
    #pickle.dump(sub_lot_col_03_results, open('sub_lot_col_03_results.pkl', 'wb')) 

    return sub_lot_col_03_results
    
if __name__ == '__main__':
    sub_lot_col_03_results = main()




