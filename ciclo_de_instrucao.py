# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:27:29 2019

@author: Vito
"""
import os

pc = 0
ir = ''
             #op code        A         B            C
memoria = [[0b00000010, 0b00001010, 0b00001101, 0b00000111], #0 | end( 7) <- end(13) + end(10) | end( 7) = 11
           [0b00000100, 0b00000000, 0b00000000, 0b00000111], #1 | end( 7)++                    | end( 7) = 12
           [0b00000010, 0b00001000, 0b00000111, 0b00001000], #2 | end( 8) <- end( 7) + end( 8) | end( 8) = 12
           [0b00001001, 0b00000000, 0b00000000, 0b00001000], #3 | end( 8) >> 1                 | end( 8) = 6
           [0b00000101, 0b00000000, 0b00000000, 0b00001000], #4 | end( 8)--                    | end( 8) = 5
           [0b00001000, 0b00000000, 0b00000000, 0b00001000], #5 | end( 8) << 1                 | end( 8) = 10
           [0b00000011, 0b00001000, 0b00000111, 0b00001110], #6 | end(14) <- end( 7) - end( 8) | end( 8) = 2
           [0b11111111, 0b00000000, 0b00000000, 0b00000000], #7
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #8
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #9
           [0b00000000, 0b00000000, 0b00000000, 0b00001010], #10
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #11
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #12
           [0b00000000, 0b00000000, 0b00000000, 0b00000001], #13
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #14
           [0b00000000, 0b00000000, 0b00000000, 0b00000000], #15
           ]

def add(memoria,pc): # 0000 0010
    end_c = memoria[pc][3]
    end_b = memoria[pc][2]
    end_a = memoria[pc][1]
    memoria[end_c][3] = memoria[end_b][3] + memoria[end_a][3]
    return '{} <- {} + {}'.format(hex(end_c), hex(end_b), hex(end_a))
    
def sub(memoria,pc): # 0000 0011
    end_c = memoria[pc][3]
    end_b = memoria[pc][2]
    end_a = memoria[pc][1]
    memoria[end_c][3] = memoria[end_b][3] - memoria[end_a][3]
    return '{} <- {} - {}'.format(hex(end_c), hex(end_b), hex(end_a))

def inc(memoria,pc): # 0000 0100
    end_c = memoria[pc][3]
    memoria[end_c][3] += 1
    return '{} ++'.format(hex(end_c))
    
def dec(memoria,pc): # 0000 0101
    end_c = memoria[pc][3]
    memoria[end_c][3] -= 1
    return '{} --'.format(hex(end_c))
    
def desloc_esquerda(memoria,pc): # 0000 1000
    end_c = memoria[pc][3]
    memoria[end_c][3] <<= 1
    return '{} << 1'.format(hex(end_c))

def desloc_direita(memoria,pc): # 0000 1001
    end_c = memoria[pc][3]
    memoria[end_c][3] >>= 1
    return '{} >> 1'.format(hex(end_c))    
    
def printa_memoria(memoria):
    for i in range(len(memoria)):
        print('')
        print('{}'.format(hex(i)), end=' ')
        for j in range(len(memoria[0])):            
            print('{:0>8}'.format(bin(memoria[i][j])[2:]), end=' ')
    
continua = True
while(continua):
    if(memoria[pc][0]) == 0b00000010:
        ir = add(memoria,pc)
    elif(memoria[pc][0]) == 0b00000011:
        ir = sub(memoria,pc)
    elif(memoria[pc][0]) == 0b00000100:    
        ir = inc(memoria,pc)
    elif(memoria[pc][0]) == 0b00000101:
        ir = dec(memoria,pc)
    elif(memoria[pc][0]) == 0b00001000:    
        ir = desloc_esquerda(memoria,pc)
    elif(memoria[pc][0]) == 0b00001001:    
        ir = desloc_direita(memoria,pc)
    elif(memoria[pc][0]) == 0b11111111:
        continua = False
    pc += 1
    
    print('\nEstado atual da memória:')
    printa_memoria(memoria) 
    print('\n\n\
          Estado atual dos registradores:\n\n\
          Instruction Register (IR): {}\n\
               Program Counter (PC): {}\n\n'.format(ir,pc))   
    os.system('pause')
    


    
    
    
    
    
    
    
    
    
    
    



