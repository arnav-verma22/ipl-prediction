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
#batsmen played in each match
batters = batters.groupby('mid',as_index=False).sum()
batters = batters.drop(['mid'], axis = 1)

#creating dummy variables of all bowlers of bowling team
data.drop_duplicates(subset =["mid", "bowler"], keep = "first", inplace = True)
dummies = pd.get_dummies(data[data['bowl_team'] == 'Royal Challengers Bangalore']['bowler'], prefix = 'bowler')

matchid = data['mid']
bowlers = pd.concat([matchid, dummies], axis = 1)

#Summarising the each match to 1 row instead of each ball detail
data = data.drop_duplicates(subset =["mid"], keep = "first")
data.reset_index(inplace = True)
data = data.drop(['index'], axis = 1)

#bowlers played in each match
bowlers = bowlers.groupby('mid',as_index=False).sum()
bowlers = bowlers.drop(['mid'], axis = 1)

#concatinating dummy variables of bowlers and batsman
final_data = pd.concat([data, bowlers, batters], axis = 1)

