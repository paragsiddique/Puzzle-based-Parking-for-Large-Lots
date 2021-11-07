#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parking_env.utils import *



def horizontal_car_moves(car_pos):
    sorted_car_position = sorted(car_pos)


    if sorted_car_position[0][0] == sorted_car_position[1][0] and\
        sorted_car_position[0][1] + 1 ==  sorted_car_position[1][1]:       


        i = sorted_car_position[0][0]
        j = sorted_car_position[0][1]


        #01 right
        move_right = tuple(sorted([(i, j+1), (i, j+2)]))
        move_right_req_cells = tuple([(i, j+2)])

        #02 left
        move_left = tuple(sorted([(i, j-1), (i, j)]))
        move_left_req_cells = tuple([(i, j-1)])

        #03 right angle right up
        move_ra_rightup = tuple(sorted([(i-2, j+2), (i-1, j+2)]))
        move_ra_rightup_req_cells = tuple(sorted([(i, j+2), (i-1, j+1), (i-2, j+2), (i-1, j+2)]))

        #04 right angle right down
        move_ra_rightdown = tuple(sorted([(i+1, j+2), (i+2, j+2)]))
        move_ra_rightdown_req_cells = tuple(sorted([(i, j+2), (i+1, j+1), (i+1, j+2), (i+2, j+2)]))

        #05 right angle left up 
        move_ra_leftup = tuple(sorted([(i-2, j-1), (i-1, j-1)]))   
        move_ra_leftup_req_cells = tuple(sorted([(i, j-1), (i-1, j), (i-2, j-1), (i-1, j-1)]))

        #06 right angle left down
        move_ra_leftdown = tuple(sorted([(i+1, j-1), (i+2, j-1)]))
        move_ra_leftdown_req_cells = tuple(sorted([(i, j-1), (i+1, j), (i+1, j-1), (i+2, j-1)]))

        #07 parallel rightdown
        move_par_rightup = tuple(sorted([(i-1, j+2), (i-1, j+3)]))
        move_par_rightup_req_cells = tuple(sorted([(i, j+2), (i-1, j+1), (i-1, j+2), (i-1, j+3)]))

        #08 parallel rightup
        move_par_rightdown = tuple(sorted([(i+1, j+2), (i+1, j+3)]))
        move_par_rightdown_req_cells = tuple(sorted([(i, j+2), (i+1, j+1), (i+1, j+2), (i+1, j+3)]))

        #09 parallel leftdown 
        move_par_leftup = tuple(sorted([(i-1, j-2), (i-1, j-1)]))
        move_par_leftup_req_cells = tuple(sorted([(i, j-1), (i-1, j), (i-1, j-2), (i-1, j-1)]))

        #10 parallel leftup
        move_par_leftdown = tuple(sorted([(i+1, j-2), (i+1, j-1)]))
        move_par_leftdown_req_cells = tuple(sorted([(i, j-1), (i+1, j), (i+1, j-2), (i+1, j-1)]))


        hor_car_moves_all = {}
        hor_car_moves_all['move_right'] = move_right, move_right_req_cells
        hor_car_moves_all['move_left'] = move_left, move_left_req_cells

        hor_car_moves_all['move_ra_rightup'] = move_ra_rightup, move_ra_rightup_req_cells
        hor_car_moves_all['move_ra_rightdown'] = move_ra_rightdown, move_ra_rightdown_req_cells                      

        hor_car_moves_all['move_ra_leftup'] = move_ra_leftup, move_ra_leftup_req_cells
        hor_car_moves_all['move_ra_leftdown'] = move_ra_leftdown, move_ra_leftdown_req_cells                     

        hor_car_moves_all['move_par_rightup'] = move_par_rightup, move_par_rightup_req_cells
        hor_car_moves_all['move_par_rightdown'] = move_par_rightdown, move_par_rightdown_req_cells

        hor_car_moves_all['move_par_leftup'] = move_par_leftup, move_par_leftup_req_cells
        hor_car_moves_all['move_par_leftdown'] = move_par_leftdown, move_par_leftdown_req_cells
        
    return hor_car_moves_all

def ver_car_moves(car_pos):    

    sorted_car_position = sorted(car_pos)

        
    if sorted_car_position[0][0] + 1 == sorted_car_position[1][0] and\
        sorted_car_position[0][1] ==  sorted_car_position[1][1]:
        
        i = sorted_car_position[0][0]
        j = sorted_car_position[0][1]
        
        
        
        #01 up
        move_up = tuple(sorted([(i-1, j), (i, j)]))
        move_up_req_cells = tuple([(i-1, j)])
        
        #02 down
        move_down = tuple(sorted([(i+1, j), (i+2, j)]))
        move_down_req_cells = tuple([(i+2, j)])
        
        #03 right angle upright
        move_ra_upright = tuple(sorted([(i-1, j+1), (i-1, j+2)]))
        move_ra_upright_req_cells = tuple(sorted([(i-1, j), (i, j+1), (i-1, j+1), (i-1, j+2)]))
        
        #04 right angle upleft
        move_ra_upleft = tuple(sorted([(i-1, j-2), (i-1, j-1)]))
        move_ra_upleft_req_cells = tuple(sorted([(i-1, j), (i, j-1), (i-1, j-2), (i-1, j-1)]))
        
        #05 right angle down right
        move_ra_downright = tuple(sorted([(i+2, j+1), (i+2, j+2)]))
        move_ra_downright_req_cells = tuple(sorted([(i+1, j+1), (i+2, j), (i+2, j+1), (i+2, j+2)]))
        
        
        #06 right angle downleft
        move_ra_downleft = tuple(sorted([(i+2, j-2), (i+2, j-1)]))
        move_ra_downleft_req_cells = tuple(sorted([(i+1, j -1), (i+2, j), (i+2, j-2), (i+2, j-1)]))
        
        #07 parallel up right
        move_par_upright = tuple(sorted([(i-2, j+1), (i-1, j+1)]))
        move_par_upright_req_cells = tuple(sorted([(i-1, j), (i, j+1), (i-2, j+1), (i-1, j+1)]))
        
        #08 parallel up left
        move_par_upleft = tuple(sorted([(i-2, j-1), (i-1, j-1)]))
        move_par_upleft_req_cells = tuple(sorted([(i-1, j), (i, j-1), (i-2, j-1), (i-1, j-1)]))
        
        #09 parallel down right
        move_par_downright = tuple(sorted([(i+2, j+1), (i+3, j+1)]))
        move_par_downright_req_cells = tuple(sorted([(i+2, j), (i+1, j+1), (i+2, j+1), (i+3, j+1)]))

        #10 parallel down left 
        move_par_downleft = tuple(sorted([(i+2, j-1), (i+3, j-1)]))
        move_par_downleft_req_cells = tuple(sorted([(i+2, j), (i+1, j-1), (i+2, j-1), (i+3, j-1)]))
        
        
        ver_car_moves_all = {}
        
        ver_car_moves_all['move_up'] = move_up, move_up_req_cells
        ver_car_moves_all['move_down'] = move_down, move_down_req_cells
        
        ver_car_moves_all['move_ra_upright'] = move_ra_upright, move_ra_upright_req_cells
        ver_car_moves_all['move_ra_upleft'] = move_ra_upleft, move_ra_upleft_req_cells
        ver_car_moves_all['move_ra_downright'] = move_ra_downright, move_ra_downright_req_cells
        ver_car_moves_all['move_ra_downleft'] = move_ra_downleft, move_ra_downleft_req_cells
        
        ver_car_moves_all['move_par_upright'] = move_par_upright, move_par_upright_req_cells
        ver_car_moves_all['move_par_downright'] = move_par_downright, move_par_downright_req_cells
        ver_car_moves_all['move_par_upleft'] = move_par_upleft, move_par_upleft_req_cells
        ver_car_moves_all['move_par_downleft'] = move_par_downleft, move_par_downleft_req_cells
        
    return ver_car_moves_all


def move_a_car_single_car_in_the_lot(node, rows=4, columns=4):
    target_car = node[0]
    if target_car[0][0] == target_car[1][0]:
        target_car_moves = horizontal_car_moves(target_car)
    elif target_car[0][1] == target_car[1][1]:
        target_car_moves = ver_car_moves(target_car)
    else:
        print('wrong input')
    
    valid_moves = []    
    for move in list(target_car_moves.keys()):
        move_req = np.array(target_car_moves[move][1])
        if ((move_req < (rows, columns)).all() and (move_req >= (0,0)).all()):
            valid_moves.append((target_car_moves[move][0], node[1]+len(target_car_moves[move][1])))
        else:
            pass

    return valid_moves


def move_a_car(node, target_car, rows=4, columns=4):
    if target_car[0][0] == target_car[1][0]:
        target_car_moves = horizontal_car_moves(target_car)
    elif target_car[0][1] == target_car[1][1]:
        target_car_moves = ver_car_moves(target_car)
    else:
        print('wrong input')
        
    other_cars_ = np.array([x for x in node[0] if x != target_car])
    other_cars = other_cars_.reshape(int(other_cars_.size/2), 2)
    
    target_car_index = node[0].index(target_car)
    valid_moves = []
    for move in list(target_car_moves.keys()):
        move_req = np.array(target_car_moves[move][1])
        if ((move_req < (rows, columns)).all() and (move_req >= (0,0)).all()) and multidim_intersect(move_req, other_cars).size == 0:
            node_ = list(node[0])
            node_[target_car_index] = target_car_moves[move][0]
            valid_moves.append((tuple(node_), node[1]+len(move_req)))
        else:
            pass
            
    return valid_moves


def move_all_the_cars(state, rows=4, columns=4):
    all_moves = []
    for target_car in state:
        all_moves.extend(move_a_car((state, 0), target_car, rows, columns))
    return all_moves



def move_a_car_in_the_driving_lane(node, driving_lane):
    target_car = node[0]
    if target_car[0][0] == target_car[1][0]:
        target_car_moves = horizontal_car_moves(target_car)
    elif target_car[0][1] == target_car[1][1]:
        target_car_moves = ver_car_moves(target_car)
    else:
        print('wrong input')
    
    valid_moves = []    
    for move in list(target_car_moves.keys()):
        move_req = target_car_moves[move][1]
        if all(item in driving_lane for item in move_req)==True:
            valid_moves.append((target_car_moves[move][0], node[1]+len(target_car_moves[move][1])))
        else:
            pass
    return valid_moves
