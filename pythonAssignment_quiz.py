#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:00:58 2019

@author: pooja
"""

import json


with open("./quiz.json") as datafile:
    data = json.load(datafile)

print("Select one group to start your Quiz", "1. Sport    2. Maths", sep="\n")
selected = input().lower()


def que_function(sm_dict):
    ans_list = []
    orig_ans_list = []
    total_que = 0
    for que in sm_dict.keys():
        total_que = total_que + 1
        print ("Question: ", sm_dict[que]['question'])
        print ("Options: ", sm_dict[que]['options'])
        ans = input('Enter your Answer : ')
        ans_list.append(ans)
        orig_ans_list.append(sm_dict[que]['answer'])
    
    score = 0
    for user_ans in ans_list:
        for orig_ans in orig_ans_list:
            if user_ans.lower() == orig_ans.lower():
                score = score + 1
    
    return score,total_que
    

if selected == '1' or selected == 'sport':
    sport_dict = data['quiz']['sport']
    marks,total = que_function(sport_dict)
    print('Your score is : ', marks, '/', total)
    

elif selected == '2' or selected == 'Maths':
    maths_dict = data['quiz']['maths']
    marks,total = que_function(maths_dict)
    print('Your score is : ', marks, '/' , total)
    
else:
    print('PLEASE ENTER VALID CHOICE')
    
