#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

class TraditionalLot():
    def __init__(self, width, length, cell_size=9):
        self.width = width
        self.length = length
        self.cell_size = cell_size
        
    def rows(self):
        return int((self.width//self.cell_size) - 2)
    
    def columns(self):
        return int(self.length//self.cell_size)
    
    def column_blocks(self):
        return int(self.length//(6*self.cell_size))
    
    def frac_coln_block(self):
        return self.columns()%6
   
    def no_of_cars(self):
        return 2*self.rows()*self.column_blocks()
    
    def no_of_cars_frac_column_block(self):
        remainder_trad = self.frac_coln_block()
        if remainder_trad >= 4:
            n = self.rows()
        else:
            n = 0
        return n
    
    def total_cars(self):
        return self.no_of_cars() + self.no_of_cars_frac_column_block()
    
    def goal_cells(self):
        columns = self.columns()
        
        mid_value = [(columns//2)-1, columns//2]
        
        goal_cells = []
        for x in mid_value:
            goal_cells.append((self.rows(), x))
        
        return [tuple(goal_cells)]
    
    def driving_lanes(self):
        rows = self.rows()
        column_blocks = self.column_blocks()
        columns = self.columns()
        x = 2
        vertical_lanes = []
        for _ in range(column_blocks):
            lane = []
            for i in range(rows):
                lane.extend(((i, x), (i, x+1)))
            vertical_lanes.extend(lane)
            x = vertical_lanes[-1][-1]+5

        horizontal_lane = []
        for i in [rows, rows+1]:
            for j in range(columns):
                horizontal_lane.append((i, j))
                
        if self.no_of_cars_frac_column_block() != 0:
            frac_coln_lane = []
            y = 6*self.column_blocks()
            for i in range(rows):
                frac_coln_lane.extend(((i, y), (i, y+1)))
        else:frac_coln_lane = []
            

        driving_lanes = vertical_lanes + frac_coln_lane + horizontal_lane
        return driving_lanes
    
    def state(self):
        rows = self.rows()
        column_blocks = self.column_blocks()
        x = 0
        state = []
        for _ in range(column_blocks):
            left_column = []
            right_column = []
            for i in range(rows):
                left_column.append(((i, x), (i, x+1)))
                right_column.append(((i, x+4), (i, x+5)))
                column = left_column + right_column
            state.extend(column)
            x = state[-1][-1][-1]+1
        
        remainder_trad = self.frac_coln_block()
        y = 6*self.column_blocks()+2
        frac_coln = []
        if remainder_trad >= 4:
            for i in range(rows):
                frac_coln.append(((i, y), (i, y+1)))
        else: frac_coln = []
        return state+frac_coln
    

    
    def car_positions(self):
        rows = self.rows() +2
        columns = self.columns()
        row_positions = [((i, j), (i, j+1))for i in range(rows) for j in range(columns-1)]
        column_positions = [((i, j), (i+1, j))for i in range(rows-1) for j in range(columns)]
        return sorted(row_positions + column_positions)
    
