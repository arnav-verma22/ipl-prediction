# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 06:11:18 2020

@author: Arnav Verma
"""
import pandas as pd

#def predict_score(bat_team, bowl_team):
dataset = pd.read_csv("ipl2017.csv")

#removed unnecessary columns    
columns_to_drop = ['date', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5', 'striker', 'non-striker','runs']
data = dataset.drop(columns = columns_to_drop)
#data = data[(data['bat_team'] == 'Chennai Super Kings') | (data['bowl_team'] == 'Royal Challengers Bangalore')]

