#!/usr/bin/env python
# coding: utf-8


parag_windows = 'C:\\Users\\parag\\Dropbox (Personal)\\sub_lot_paper\\source_code\\'
parag_mac = '/Users/paragsiddique/LoDI Dropbox/sub_lot_paper/source_code/'
import sys
sys.path.append(parag_windows)


from parking_env.parking_lot import *
from parking_env.search_algorithm import *
from parking_env.side_retrieval import *
from parking_env.sub_lot import *
from parking_env.traditional_lot import *
from parking_env.utils import *
from parking_env.sublot_cost_function import *


sub_lot_10x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), 
                 ((2, 5), (3, 5)), ((2, 6), (3, 6)), ((2, 7), (3, 7)), ((2, 8), (3, 8)), ((2, 9), (3, 9)), 
                 ((0, 0), (0, 1)), ((0, 8), (0, 9)), ((1, 0), (1, 1)), ((1, 8), (1, 9)), 
                 ((0, 2), (0, 3)), ((1, 2), (1, 3)), ((0, 4), (0, 5)))

sub_lot_9x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), ((2, 5), (3, 5)),
               ((2, 6), (3, 6)), ((2, 7), (3, 7)), ((2, 8), (3, 8)), 
               ((0, 0), (0, 1)), ((0, 2), (0, 3)), ((0, 5), (0, 6)), ((0, 7), (0, 8)), 
               ((1, 0), (1, 1)), ((1, 7), (1, 8)))

sub_lot_8x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), ((2, 5), (3, 5)),
               ((2, 6), (3, 6)), ((2, 7), (3, 7)), 
               ((0, 0), (0, 1)), ((0, 6), (0, 7)), ((1, 0), (1, 1)), ((1, 6), (1, 7)), ((0, 2), (0, 3)))

sub_lot_7x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), ((2, 5), (3, 5)),
               ((2, 6), (3, 6)), 
               ((0, 0), (0, 1)), ((0, 5), (0, 6)), 
               ((1, 0), (1, 1)), ((1, 5), (1, 6)))


sub_lot_6x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), ((2, 5), (3, 5)), 
               ((0, 4), (0, 5)), ((1, 4), (1, 5)), ((0, 0), (0, 1)))


sub_lot_5x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), ((2, 4), (3, 4)), 
               ((0, 3), (0, 4)), ((1, 3), (1, 4)))


sub_lot_4x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)), ((2, 3), (3, 3)), 
               ((0, 2), (0, 3)))


sub_lot_3x4 = (((2, 0), (3, 0)), ((2, 1), (3, 1)), ((2, 2), (3, 2)))

def main():

    states = [sub_lot_3x4, sub_lot_4x4, sub_lot_5x4, sub_lot_6x4, 
              sub_lot_7x4, sub_lot_8x4, sub_lot_9x4, sub_lot_10x4] 
    
    states_names = ['sub_lot_3x4', 'sub_lot_4x4', 'sub_lot_5x4', 'sub_lot_6x4', 
              'sub_lot_7x4', 'sub_lot_8x4', 'sub_lot_9x4', 'sub_lot_10x4'] 
    
    rows_list = [3, 4, 5, 6, 7, 8, 9, 10]
    
    columns = 4
    
    sub_lot_col_04_results = {}
    for state, rows, states_name in zip(states, rows_list, states_names):
        try:
            sub_lot_results = comp_cost(state, columns, rows) 
            # while writing the function I missplaced columns and row positions, later never changed the code
            print(states.index(state))
            sub_lot_col_04_results[states_name] = sub_lot_results
        except:
            pass
    
    pickle.dump(sub_lot_col_04_results, open('sub_lot_col_04_results.pkl', 'wb')) 

    return sub_lot_col_04_results
    
if __name__ == '__main__':
    sub_lot_col_04_results = main()




