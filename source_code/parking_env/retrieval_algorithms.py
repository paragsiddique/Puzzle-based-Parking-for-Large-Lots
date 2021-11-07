#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
import random

from parking_env.parking_lot import *
from parking_env.sub_lot import *
from parking_env.traditional_lot import *
#%%
def build_path_single_car(start_node, winner_node, came_from):
    current_node = winner_node
    path = []

    while current_node != start_node:
        path.append(current_node)
        current_node = came_from[current_node]


    path.append(start_node)
    path.reverse()
    return path


#%%
def a_star_search_single_car_in_the_lot(start_node, goal, h_value_dict, rows=4, columns=4 , weight=1):

    #frontier
    queue = [(start_node, 0)]

    #explored nodes
    explored = set()

    #tracking parent child
    came_from = {}
    came_from[start_node] = None

    while queue:
        #to pop first N items [my_list.pop(0) for _ in range(N)]
        pre_current_node = queue.pop(0)
        current_node = pre_current_node[0]
        if current_node[0] == goal:
            #return current_node, came_from
            winner_node = current_node
            path = build_path_single_car(start_node, winner_node, came_from)
            return path, len(explored)

        explored.add(current_node[0])

        neighbours = move_a_car_single_car_in_the_lot(current_node, rows, columns)

        for neighbour in neighbours:

            h_value = weight*h_value_dict[neighbour[0]]
            if neighbour[0] not in [x for x in explored] and neighbour[0] not in [x[0][0] for x in queue]:

                queue.append((neighbour, neighbour[1] + h_value))
            elif neighbour[0] in [x[0][0] for x in queue]:
                find_index = [x[0][0] for x in queue].index(neighbour[0])
                if queue[find_index][1] > (neighbour[1] + h_value):
                    del queue[find_index]
                    queue.append((neighbour, neighbour[1] + h_value))
            came_from[neighbour] = current_node
            queue.sort(key=lambda tup: tup[1])

    return "path doesn't exist"

#%%
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self)-> bool:
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def get_rand(self):
        rand_move = random.choice(range(len(self.elements)))
        return self.elements.pop(rand_move)[1]
    
#%%
def build_path_multi_car(start_node, winner_node, came_from, cost_so_far):
    current_node = winner_node
    path = []

    while current_node != start_node:
        path.append(current_node)
        current_node = came_from[current_node]

    path.append(start_node)
    path.reverse()
    path_cost = [(x, cost_so_far[x]) for x in path]
    return path_cost    
#%%
def a_star_search(state, target_car, goal, h_value_dict, rows=4, columns=4, weight=1):
    initial_state = state
    target_car_index = initial_state.index(target_car)

    #frontier
    frontier = PriorityQueue()
    frontier.put(initial_state, 0)

    #explored nodes
    cost_so_far = {}
    cost_so_far[initial_state] = 0

    #tracking parent child
    came_from = {}
    came_from[initial_state] = None

    while not frontier.empty():
        current_state = frontier.get()
        if current_state[target_car_index] == goal:
            #return current_state, came_from, cost_so_far
            path = build_path_multi_car(initial_state, current_state, came_from, cost_so_far)
            return current_state, cost_so_far[current_state], path, len(cost_so_far)

        neighbours = move_all_the_cars(current_state, rows, columns)

        for neighbour in neighbours:
            new_cost = cost_so_far[current_state] + neighbour[1]
            if neighbour[0] not in cost_so_far or new_cost < cost_so_far[neighbour[0]]:
                cost_so_far[neighbour[0]] = new_cost
                h_value = weight*h_value_dict[neighbour[0][target_car_index]]
                f_value = new_cost + h_value
                frontier.put(neighbour[0], f_value)
                came_from[neighbour[0]] = current_state

    return "path doesn't exist"


#%%

# def build_path_single_car_in_the_lot_side_rt(start_node, winner_node, came_from):
#     current_node = winner_node
#     path = []

#     while current_node != start_node:
#         path.append(current_node)
#         current_node = came_from[current_node]


#     path.append(start_node)
#     path.reverse()
#     return path


def a_star_search_single_car_in_the_lot_side_rt(start_node, goal_cells, h_value_dict, rows=4, columns=4 , weight=1):

    #frontier
    queue = [(start_node, 0)]

    #explored nodes
    explored = set()

    #tracking parent child
    came_from = {}
    came_from[start_node] = None

    while queue:
        #to pop first N items [my_list.pop(0) for _ in range(N)]
        pre_current_node = queue.pop(0)
        current_node = pre_current_node[0]
        if current_node[0] in goal_cells:
            #return current_node, came_from
            winner_node = current_node
            path = build_path_single_car(start_node, winner_node, came_from)
            return path, len(explored)

        explored.add(current_node[0])

        neighbours = move_a_car_single_car_in_the_lot(current_node, rows, columns)

        for neighbour in neighbours:
            h_value = weight*h_value_dict[neighbour[0]]
            if neighbour[0] not in [x for x in explored] and neighbour[0] not in [x[0][0] for x in queue]:
                queue.append((neighbour, neighbour[1] + h_value))
            elif neighbour[0] in [x[0][0] for x in queue]:
                find_index = [x[0][0] for x in queue].index(neighbour[0])
                if queue[find_index][1] > (neighbour[1] + h_value):
                    del queue[find_index]
                    queue.append((neighbour, neighbour[1] + h_value))
            came_from[neighbour] = current_node
            queue.sort(key=lambda tup: tup[1])

    return "path doesn't exist"
#%%



# def build_path_side_rt(start_node, winner_node, came_from, cost_so_far):
#     current_node = winner_node
#     path = []

#     while current_node != start_node:
#         path.append(current_node)
#         current_node = came_from[current_node]

#     path.append(start_node)
#     path.reverse()
#     path_cost = [(x, cost_so_far[x]) for x in path]
#     return path_cost


def a_star_search_side_rt(state, target_car, goal_cells, h_value_dict, rows=4, columns=4, weight=1):
    initial_state = state
    target_car_index = initial_state.index(target_car)

    #frontier
    frontier = PriorityQueue()
    frontier.put(initial_state, 0)
    #queue = [(start_node, 0)]

    #explored nodes
    cost_so_far = {}
    cost_so_far[initial_state] = 0

    #tracking parent child
    came_from = {}
    came_from[initial_state] = None

    while not frontier.empty():
        current_state = frontier.get()
        if current_state[target_car_index] in goal_cells:
            #return current_state, came_from, cost_so_far
            path = build_path_multi_car(initial_state, current_state, came_from, cost_so_far)
            return current_state, cost_so_far[current_state], path, len(cost_so_far)

        neighbours = move_all_the_cars(current_state, rows, columns)

        for neighbour in neighbours:
            new_cost = cost_so_far[current_state] + neighbour[1]
            if neighbour[0] not in cost_so_far or new_cost < cost_so_far[neighbour[0]]:
                cost_so_far[neighbour[0]] = new_cost
                h_value = weight*h_value_dict[neighbour[0][target_car_index]]
                f_value = new_cost + h_value
                frontier.put(neighbour[0], f_value)
                came_from[neighbour[0]] = current_state

    return "path doesn't exist"



#%%
class PriorityQueue_driving_lane:
    def __init__(self):
        self.elements = []

    def empty(self)-> bool:
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)

    def get_rand(self):
        rand_move = random.choice(range(len(self.elements)))
        return self.elements.pop(rand_move)[1]

def rt_in_the_driving_lane(target_car, goal_cells, driving_lane):
    
    initial_state = target_car

    #frontier
    frontier = PriorityQueue_driving_lane()
    frontier.put(initial_state, 0)
    #explored nodes
    cost_so_far = {}
    cost_so_far[initial_state] = 0

    #tracking parent child
    came_from = {}
    came_from[initial_state] = None

    while not frontier.empty():
        current_state_cost, current_state = frontier.get()
        if current_state in goal_cells:
            path = build_path_multi_car(initial_state, current_state, came_from, cost_so_far)
            return current_state, current_state_cost, path, len(cost_so_far)

        neighbours = move_a_car_in_the_driving_lane((current_state, 0), driving_lane)

        for neighbour in neighbours:
            new_cost = cost_so_far[current_state] + neighbour[1]
            if neighbour[0] not in cost_so_far or new_cost < cost_so_far[neighbour[0]]:
                cost_so_far[neighbour[0]] = new_cost
                frontier.put(neighbour[0], new_cost)
                came_from[neighbour[0]] = current_state

    return "path doesn't exist"

#%%
def rt(width, length, sublot_columns, sublot_rows = 10):
    modular_parking_lot = ModularLot(width, length, sublot_rows, sublot_columns)
    state = modular_parking_lot.state()
    driving_lanes = modular_parking_lot.driving_lanes()
    goal_cells = modular_parking_lot.goal_cells()
    rt_dict = {}
    for target_car in state:
        goal_pos, rt_moves, rt_path, visited_nodes = rt_in_the_driving_lane(target_car, 
                                                                            goal_cells, 
                                                                            driving_lanes)
        rt_dict[target_car] = rt_moves
    x = np.array(list(rt_dict.values())) 
    return x

def rt_trad(width, length):
    traditional_parking_lot = TraditionalLot(width, length)
    state = traditional_parking_lot.state()
    driving_lanes = traditional_parking_lot.driving_lanes()
    goal_cells = traditional_parking_lot.goal_cells()
    rt_dict = {}
    for target_car in state:
        goal_pos, rt_moves, rt_path, visited_nodes = rt_in_the_driving_lane(target_car, 
                                                                            goal_cells, 
                                                                            driving_lanes)
        rt_dict[target_car] = rt_moves
    x = np.array(list(rt_dict.values())) 
    return x