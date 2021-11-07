# -*- coding: utf-8 -*-

import numpy as np


def create_the_grid(rows, columns):
    grid = np.zeros((rows, columns), dtype=np.str)
    grid = np.char.zfill(grid, 6)
    for i in range(rows):
        for j in range(columns):
            grid[i,j] = str((i, j))
            
    print(grid)
    return 


def layout_display(state, rows, columns):
    grid = np.zeros((rows, columns), dtype=np.str)
    grid = np.char.zfill(grid, 2)
    for i in range(0,rows):
        for j in range(0,columns):
            grid[i,j] = '  '
   
    for i in range(len(state)):
        for j in range(2):
            grid[state[i][j]] = str(1+i)
    grid = np.char.zfill(grid, 2)
    return grid


def car_positions(rows, columns):
    row_positions = [((i, j), (i, j+1))for i in range(rows) for j in range(columns-1)]
    column_positions = [((i, j), (i+1, j))for i in range(rows-1) for j in range(columns)]
    return sorted(row_positions + column_positions)


def multidim_intersect(arr1, arr2):
    arr1_view = arr1.view([('',arr1.dtype)]*arr1.shape[1])
    arr2_view = arr2.view([('',arr2.dtype)]*arr2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return intersected.view(arr1.dtype).reshape(-1, arr1.shape[1])


# for plots
marker_list = ['o', 'v', 'x', '^', '+', '<', 'p', '>']



def running_time_convert(running_time):
    '''
    converts seconds into days, hours, mins and sec

    '''
    day = running_time // (24 * 3600)
    running_time = running_time % (24 * 3600)
    hour = running_time // 3600
    running_time %= 3600
    minutes = running_time // 60
    running_time %= 60
    seconds = running_time
    return "%dd %dh %dm %ds" %(day, hour, minutes, seconds)


