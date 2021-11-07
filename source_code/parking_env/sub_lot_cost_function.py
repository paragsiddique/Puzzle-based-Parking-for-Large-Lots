# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:02:56 2021

@author: parag
"""


from parking_env.parking_lot import *
from parking_env.sub_lot import *
from parking_env.traditional_lot import *
from parking_env.retrieval_algorithms import *
from parking_env.sub_lot_utils import *
from parking_env.utils import *

import concurrent
import multiprocessing 

import math
import numpy as np


import time
import pickle


    
    
def cost(state, x, goal_cells, heuristic_01, rows,  columns, weight):
    return a_star_search_side_rt(state, x, goal_cells, heuristic_01, rows, columns, weight)[1]


def sub_lot_cost_function(state, rows,  columns, weight=1):   
    
    car_position = car_positions(rows, columns) 

    heuristic_00 = {}
    for x in car_position:
        heuristic_00[x] = 0
        
    goal_cells = [((rows-2, i), (rows-1, i)) for i in range(columns)]+[((rows-1, i), (rows-1, i+1)) for i in range(columns)]
    
    heuristic_01 = {}
    for x in car_position:
        heuristic_01[x] = a_star_search_single_car_in_the_lot_side_rt((x, 0), 
                                                                      goal_cells, 
                                                                      heuristic_00, 
                                                                      rows, 
                                                                      columns, 
                                                                      weight)[0][-1][-1]

    cost_list = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
    #with concurrent.futures.ProcessPoolExecutor(mp_context=multiprocessing.get_context('fork')) as executor:
        results = executor.map(cost, 
                               [state for _ in range(len(state))], 
                               state, 
                               [goal_cells for _ in range(len(state))], 
                               [heuristic_01 for _ in range(len(state))], 
                               [rows for _ in range(len(state))], 
                               [columns for _ in range(len(state))], 
                               [weight for _ in range(len(state))])
        for f in results:
            cost_list.append(f)
            
    return cost_list

def comp_cost(state, rows, columns):
    start_time = time.time()
    comp_cost = sub_lot_cost_function(state, rows, columns)
    end_time = time.time()
    running_time = end_time - start_time

    results = {}
    results['rows'] = rows
    results['columns'] = columns
    results['initial_state'] = state
    results['comp_cost'] = comp_cost
    results['running_time'] = running_time_convert(running_time)
    return results