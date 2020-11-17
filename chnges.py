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

#creating dummy variables of all batsmen of batting team
dummies2 = pd.get_dummies(data['batsman'], prefix = 'batsman')
matchid = data['mid']
batters = pd.concat([matchid, dummies2], axis = 1)
#batsmen played in each match
batters = batters.groupby('mid',as_index=False).sum()
batters = batters.drop(['mid'], axis = 1)

#creating dummy variables of all bowlers of bowling team
data.drop_duplicates(subset =["mid", "bowler"], keep = "first", inplace = True)
dummies = pd.get_dummies(data['bowler'], prefix = 'bowler')

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

#creating dummy variables of bat_team, bowl_team and venue and removing their categorical columnsq
dummies3 = pd.get_dummies(final_data['bat_team'], prefix = 'bat_team')
dummies4 = pd.get_dummies(final_data['bowl_team'], prefix = 'bowl_team')
dummies5 = pd.get_dummies(final_data['venue'], prefix = 'venue')
final_data = pd.concat([final_data, dummies3, dummies4, dummies5], axis = 1)

backup = final_data
categorical_features = ['venue', 'bat_team', 'bowl_team', 'batsman', 'bowler']
final_data = final_data.drop(columns = categorical_features)

y = final_data['total']
x = final_data.drop(['total'], axis = 1)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
forest=RandomForestRegressor()
forest.fit(x_train,y_train)
y_pred = forest.predict(x_test)
forest.score(x_test,y_test)
forest.score(x_train,y_train)

from sklearn.model_selection import cross_val_score
cv_scores=cross_val_score(RandomForestRegressor(),x,y,cv=5)
cv_scores