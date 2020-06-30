# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:05:32 2020

@author: johnn
"""
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc

# class QuadracticVotingKnob:
    
    
#     def __init__(self,max_value):
#         self.max_val = max_value
#         self.min_val = 0.0
#         self.current_val = 0.0
        
               
class QuadraticVotingMachine:
    
    def __init__(self,num_knobs, budget):
        self.knobs = np.zeros(num_knobs)
        self.squared = self.knobs
        self.initial = budget
        self.remaining = budget
        
        
    def knobClickedToMove(self,knob_id):
        # returns new max for that knob
        return self.remaining + self.squared[knob_id]
    
    def knobMoved(self,knob_id,new_val):
        new_max = self.knobClickedToMove(knob_id)
        if (new_val**2) <= new_max :
            self.knobs[knob_id]=new_val
            self.updateBudget()
            return "updated ok"
        else:
            #self.knobs[knob_id]=new_max
            self.updateBudget()
            return "insufficient budget"
            
        
    def updateBudget(self):
        self.squared = self.knobs**2
        self.remaining = self.initial - sum(self.squared)
        print("Knob values: "+str(self.knobs))
        print("Squared values: "+str(self.squared))
        print("Remaining budget: "+str(self.remaining))
        
# other functions - not part of QVM class


def updateOutput(slider_id):
        return slider_id
        