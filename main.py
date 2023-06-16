# The main skeleton File
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 18:56:12 2023

@author: AD
"""

import pandas as pd
import json


def AI_function(inp_str):
    print("This is AI Function")
    print(inp_str)
    return "Output From AI Function" + inp_str

steps=['What do you want to build the game about',
       'Characters',
       'Story',
       'Game Universe',
       'Anything Else']

def chat():
    print("This is the chat function")
    print("--------------------------------")
    inp_status = input("Should we start - y/n ?")
    if inp_status.upper() == 'Y':
        print("*******")
        print("Welcome to World Builder LLC \n")
        base_idea = input(steps[0] + " - ")
        game_inp=[]
        for i in range(1,len(steps)):
            cur_inp = input(steps[i]+ " - ")
            game_inp.append(cur_inp)
        
        final_inp = input("Do you have anything additional to add (press N if nothing else to add)")
        while final_inp.upper() != 'N':
            game_inp.append(final_inp+ " - ")
            final_inp =input("Do you have anything additional to add (press N if nothing else to add)")
            
        return base_idea,game_inp
    else:
        
        return "NO INPUT",[]
    
main_game, game_attr= chat()

AI_function("We are creating game with idea of " + main_game)

for cur_attr in game_attr:
    AI_function(" The attribute to pass to LLM is " + cur_attr)
            
