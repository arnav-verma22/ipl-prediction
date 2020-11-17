# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 06:44:28 2020

@author: Arnav Verma
"""
import pandas as pd

#def predict_score(bat_team, bowl_team):
dataset = pd.read_csv("ipl2017.csv")

#removed unnecessary columns
columns_to_drop = ['date', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5', 'striker', 'non-striker','runs']
data = dataset.drop(columns = columns_to_drop)
data = data[(data['bat_team'] == 'Chennai Super Kings') | (data['bowl_team'] == 'Royal Challengers Bangalore')]

#creating dummy variables of all batsmen of batting team
dummies2 = pd.get_dummies(data[data['bat_team'] == 'Chennai Super Kings']['batsman'], prefix = 'batsman')
matchid = data['mid']
batters = pd.concat([matchid, dummies2], axis = 1)
