# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:27:29 2019

@author: Vito
"""
          #op code     A      B        C
memoria = [[0b0001, 0b1010 ,0b1011, 0b1100],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,7],
           [0,0,0,20],
           [0,0,0,0],
           [0,0,0,0],
           ]
pc = 0
ir = ''

def add(memoria,pc):
    end_c = memoria[pc][3]
    end_b = memoria[pc][2]
    end_a = memoria[pc][1]
    memoria[end_c][3] = memoria[end_b][3] + memoria[end_a][3]
    return '{} <- {} + {}'.format(hex(end_c), hex(end_b), hex(end_a))
    
def sub(memoria,pc):
    end_c = memoria[pc][3]
    end_b = memoria[pc][2]
    end_a = memoria[pc][1]
    memoria[end_c][3] = memoria[end_b][3] + memoria[end_a][3]
    
ir = add(memoria,pc)