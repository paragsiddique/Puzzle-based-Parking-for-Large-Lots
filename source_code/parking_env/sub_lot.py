#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

def no_of_cars_in_a_sublot(sublot_rows, sublot_columns):
    if sublot_columns==3:
        if sublot_rows%2==0:
            no_of_cars = (sublot_rows*sublot_columns-2)/2
        else:
            no_of_cars = (sublot_rows*sublot_columns-3)/2
                    
    else:    
        if sublot_rows*sublot_columns%2==0:
            no_of_cars = (sublot_rows*sublot_columns-6)/2
        else:
            no_of_cars = (sublot_rows*sublot_columns-5)/2
    return int(no_of_cars)

class ModularLot():
    def __init__(self, width, length, sublot_rows, sublot_columns, cell_size=9, min_sub_lot_rows=3):
        self.width = width
        self.length = length
        self.sublot_rows = sublot_rows
        self.sublot_columns = sublot_columns
        self.cell_size = cell_size
        self.min_sub_lot_rows = min_sub_lot_rows
           
    def rows(self):
        return (self.width//self.cell_size)-2
    
    def columns(self):
        return self.length//self.cell_size
       
    def goal_cells(self):
        columns = self.columns()
        
        mid_value = [(columns//2)-1, columns//2]
        
        goal_cells = []
        for x in mid_value:
            goal_cells.append((self.rows(), x))
        
        return [tuple(goal_cells)]
    
#%% 
    def row_blocks(self):
        return self.rows()//self.sublot_rows
    
    def size_of_a_column_block(self):
        return (2*self.sublot_columns + 2)
    
    def column_blocks(self):
        return self.columns()//self.size_of_a_column_block()
    
    def remaining_rows(self):
        return self.rows()%self.sublot_rows
    
    def remaining_columns(self):
        return self.columns()%self.size_of_a_column_block()
        
    def traditional_column_blocks(self):
        return self.remaining_columns()//6
    
    def reamining_traditional_column_blocks(self):
        return self.remaining_columns()%6
    

#%%
    
    def no_of_cars_row_blocks(self):
        return 2*no_of_cars_in_a_sublot(self.sublot_rows, self.sublot_columns)
    
    def no_of_cars_remaining_rows(self):
        if self.remaining_rows() >= self.min_sub_lot_rows:
            n = 2*no_of_cars_in_a_sublot(self.remaining_rows(), self.sublot_columns)
        else:
            n = 2*self.remaining_rows()
        return n
                                         
    def no_of_cars_in_a_column_block(self):
        return self.no_of_cars_row_blocks()*self.row_blocks() + self.no_of_cars_remaining_rows()
    
    def no_of_cars_in_all_the_column_blocks(self):
        return self.no_of_cars_in_a_column_block()*self.column_blocks()
    
    def no_of_cars_traditional_column_blocks(self):
        return 2*self.rows()*self.traditional_column_blocks()
    
    def no_of_cars_remaining_traditional_columns(self):
        remainder_trad = self.remaining_columns()%6
        if remainder_trad >= 4:
            n = self.rows()
        else:
            n = 0
        return n
    
    def total_no_of_cars(self):
        total = self.no_of_cars_in_all_the_column_blocks() + self.no_of_cars_remaining_traditional_columns()\
        + self.no_of_cars_traditional_column_blocks()
        return total
    
#%%
    def vert_driving_lanes(self):
        rows = self.rows()
        column_blocks = self.column_blocks()
        x = self.sublot_columns
        vertical_lanes = []
        for _ in range(column_blocks):
            lane = []
            for i in range(rows):
                lane.extend(((i, x), (i, x+1)))
            vertical_lanes.extend(lane)
            x = vertical_lanes[-1][-1]+(2*self.sublot_columns)+1

        return vertical_lanes    

    def hor_driving_lanes(self):
        rows = self.rows()
        columns = self.columns()            
        horizontal_lane = []
        for i in [rows, rows+1]:
            for j in range(columns):
                horizontal_lane.append((i, j))

        return horizontal_lane
            
        
    def trad_coln_blocks_driving_lane(self):
        if self.traditional_column_blocks() != 0:
            rows = self.rows()
            column_blocks = self.traditional_column_blocks()
            columns = self.columns()
            x = 2+self.size_of_a_column_block()*self.column_blocks()
            vertical_lanes = []
            for _ in range(column_blocks):
                lane = []
                for i in range(rows):
                    lane.extend(((i, x), (i, x+1)))
                vertical_lanes.extend(lane)
                x = vertical_lanes[-1][-1]+5
        else:
            vertical_lanes = []
        return vertical_lanes
    
    def remaining_trad_coln_blocks_driving_lane(self):
        rows = self.rows()
        if self.no_of_cars_remaining_traditional_columns != 0:
            frac_coln_lane = []
            y = self.column_blocks()*self.size_of_a_column_block() + 6*self.traditional_column_blocks()
            for i in range(rows):
                frac_coln_lane.extend(((i, y), (i, y+1)))
        else:
            frac_coln_lane = []
            
        return frac_coln_lane
    
    def driving_lanes(self):
        total = self.vert_driving_lanes()+self.trad_coln_blocks_driving_lane()+\
                self.remaining_trad_coln_blocks_driving_lane()+self.hor_driving_lanes()
        return total
            
        
    def side_rt_state(self):
        rows = self.rows()
        column_blocks = self.column_blocks()
        x = self.sublot_columns - 2
        state = []
        for _ in range(column_blocks):
            left_column = []
            right_column = []
            for i in range(rows):
                left_column.append(((i, x), (i, x+1)))
                right_column.append(((i, x+4), (i, x+5)))
                column = left_column + right_column
            state.extend(column)
            x = state[-1][-1][-1] - 1 + 2*self.sublot_columns - 2
        return state
    
    def traditional_state(self):
        if self.traditional_column_blocks() != 0:
            rows = self.rows()
            column_blocks = self.traditional_column_blocks()
            x = self.size_of_a_column_block()*self.column_blocks()
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
        else:
            state = []
            
        return state
        
    def remaining_traditional_state(self):
        if self.no_of_cars_remaining_traditional_columns() != 0:
            rows = self.rows()
            remainder_trad = self.reamining_traditional_column_blocks()
            y = self.column_blocks()*self.size_of_a_column_block() + 6*self.traditional_column_blocks()+2
            frac_coln = []
            if remainder_trad >= 4:
                for i in range(rows):
                    frac_coln.append(((i, y), (i, y+1)))
            else: frac_coln = []
        else:
            frac_coln = []
        return frac_coln
    
    def state(self):
        total = self.side_rt_state()+self.traditional_state()+self.remaining_traditional_state()
        return total