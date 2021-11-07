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


sub_lot_10x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)),
                ((3, 5), (4, 5)), ((3, 6), (4, 6)), ((3, 7), (4, 7)), ((3, 8), (4, 8)), ((3, 9), (4, 9)),
                ((0, 8), (0, 9)), ((1, 8), (1, 9)), ((2, 8), (2, 9)),
                ((0, 6), (0, 7)), ((1, 6), (1, 7)),
                ((0, 2), (0, 3)), ((1, 2), (1, 3)),
                ((2, 6), (2, 7)), ((2, 2), (2, 3)), 
                ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1)))


sub_lot_9x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)),
               ((3, 5), (4, 5)), ((3, 6), (4, 6)), ((3, 7), (4, 7)), ((3, 8), (4, 8)),
               ((0, 7), (0, 8)), ((1, 7), (1, 8)), ((2, 7), (2, 8)), 
               ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1)), 
               ((0, 2), (0, 3)), ((1, 2), (1, 3)), ((2, 2), (2, 3)), 
               ((0, 5), (0, 6)), ((2, 5), (2, 6))) 


sub_lot_8x5 =  (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)),
               ((3, 5), (4, 5)), ((3, 6), (4, 6)), ((3, 7), (4, 7)),
               ((0, 6), (0, 7)), ((1, 6), (1, 7)), ((2, 6), (2, 7)), 
               ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1)),
               ((0, 2), (1, 2)), ((0, 3), (1, 3)), ((0, 5), (1, 5)))


sub_lot_7x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)),
               ((3, 5), (4, 5)), ((3, 6), (4, 6)), 
               ((0, 5), (0, 6)), ((1, 5), (1, 6)), ((2, 5), (2, 6)), 
               ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1)), 
               ((0, 2), (1, 2)), ((0, 4), (1, 4))) 


sub_lot_6x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)), ((3, 5), (4, 5)),
               ((0, 4), (0, 5)), ((1, 4), (1, 5)), ((2, 4), (2, 5)), 
               ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((2, 0), (2, 1))) 

sub_lot_5x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)), ((3, 4), (4, 4)),
               ((0, 3), (0, 4)), ((1, 3), (1, 4)), ((2, 3), (2, 4)), ((0, 1), (0, 2)), ((2, 1), (2, 2))) 

sub_lot_4x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((3, 3), (4, 3)),
               ((0, 2), (0, 3)), ((1, 2), (1, 3)), ((2, 2), (2, 3)))

sub_lot_3x5 = (((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (4, 2)), ((0, 1), (0, 2)), ((2, 1), (2, 2)))


def main():

    states = [sub_lot_3x5, sub_lot_4x5, sub_lot_5x5, sub_lot_6x5, 
              sub_lot_7x5, sub_lot_8x5, sub_lot_9x5, sub_lot_10x5] 
    
    states_names = ['sub_lot_3x5', 'sub_lot_4x5', 'sub_lot_5x5', 'sub_lot_6x5', 
              'sub_lot_7x5', 'sub_lot_8x5', 'sub_lot_9x5', 'sub_lot_10x5'] 
    
    rows_list = [3, 4, 5, 6, 7, 8, 9, 10]
    
    columns = 5
    
    sub_lot_col_05_results = {}
    for state, rows, states_name in zip(states, rows_list, states_names):
        try:
            sub_lot_results = comp_cost(state, columns, rows)
            # while writing the function I missplaced columns and row positions, later never changed the code
            print(states.index(state))
            sub_lot_col_05_results[states_name] = sub_lot_results
        except:
            pass
    
    pickle.dump(sub_lot_col_05_results, open('sub_lot_col_05_results.pkl', 'wb')) 

    return sub_lot_col_05_results
    
if __name__ == '__main__':
    sub_lot_col_05_results = main()




