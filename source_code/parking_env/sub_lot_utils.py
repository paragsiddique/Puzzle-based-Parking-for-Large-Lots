# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 00:22:46 2021

@author: parag
"""
from parking_env.parking_lot import *
from parking_env.sub_lot import *
from parking_env.traditional_lot import *
from parking_env.retrieval_algorithms import *
from parking_env.utils import *

import math
import numpy as np
from sympy import symbols, Eq, solve
import itertools
import pickle


def compute_width_length(no_of_cars, ratio, cell_size=9):
    a, b = symbols('a b')
    eq1 = Eq(2*a*b - no_of_cars, 0)
    eq2 = Eq((6*a/b) - ratio, 0)
    soln = solve((eq1,eq2), (a, b))
    for a, b in soln:
        if a>=0 and b>=0:
            width = math.floor(a)*6*cell_size
            length = math.floor(b)*cell_size
            traditional_parking_lot = TraditionalLot(width, length)
            state = traditional_parking_lot.state()
            return width, length, len(state)
        
def compute_shapes(width, length):
    r = np.arange(0.0, 2.1, 0.1) .tolist()
    area = width*length
    
    new_shape = {}
    for x in r:
        W, L = symbols('W L')
        eq1 = Eq(W*L - area, 0)
        eq2 = Eq(W/L - x, 0)
        soln = solve((eq1,eq2), (W, L))
        for a, b in soln:
            if a>=0 and b>=0:
                new_shape[round(x, 1)] = (math.floor(a), math.floor(b))
    return new_shape

def compute_sub_lot_sizes(min_rows=3, max_rows=11, min_cols=3, max_cols=7):
    test_rows = list(range(min_rows, max_rows))
    test_cols = list(range(min_cols, max_cols))
    sub_lot_sizes = []
    for i in test_rows:
        for j in test_cols:
            sub_lot_sizes.append((i, j))
    return sub_lot_sizes



def save_results(new_shape, trd_lot, sub_lot_sizes, sublot_cars, rt_trad_val, sublot_rt, save_path, N):
    dataset = {}
    dataset['large_lot_shapes'] = new_shape
    dataset['no_of_cars_traditional'] = trd_lot
    dataset['sub_lot_sizes'] = sub_lot_sizes
    dataset['no_of_cars_sublot'] = sublot_cars
    dataset['retrieval_traditional'] = rt_trad_val
    dataset['retrieval_driving_lane'] = sublot_rt    
    pickle.dump(dataset, open(save_path+'dataset_lot_capacity_'+str(N)+'.pkl', 'wb'))
    return dataset