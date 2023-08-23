# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:06:13 2023

@author: Dhanya
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import openpyxl
from sklearn.model_selection import train_test_split

def run_code():
    xx = pd.read_excel('D:/Prediction-of-Job-Interview-Performance-by-extracting-Lexical-features-/Prosody/prosodic_features1.xlsx',sheet_name = 'updated_sheet')
    column_names= xx.columns.tolist()
    ##print(column_names)
    x = xx.iloc[:,0:]
    ym = pd.read_excel('D:/Prediction-of-Job-Interview-Performance-by-extracting-Lexical-features-/Prosody/turker_scores_3.xlsx')
    y = ym.iloc[0:,7:8]
    
    ##print(x,"hey")
    ##print(y,"hey")
    #splitting the dataset into training and testing set
    
    from sklearn.ensemble import RandomForestRegressor
    regressor1 = RandomForestRegressor(n_estimators = 100, random_state = 0)
    regressor1.fit(x,y)
    
    from sklearn.model_selection import cross_val_score
    accuracies1 = cross_val_score(estimator = regressor1, X = x, y = y, cv = 5)
    print(accuracies1,"Accuracies")
    accuracies1.mean()
    accuracies1.std()
    
    df=pd.read_excel('D:/Prediction-of-Job-Interview-Performance-by-extracting-Lexical-features-/Prosody/MyProsodyFeatures.xlsx',sheet_name = 'Prosody')
    df_subset = df[column_names]
    
    #print(df_subset)
    y_pred = regressor1.predict(df_subset)
    #print(y_pred*10)
    print(y_pred)
    
     
    wb = openpyxl.load_workbook('D:/final_result/myprosody_final.xlsx')
    ws=wb['Final']
    ws.cell(row=2,column=8,value=(y_pred[0]*10))
    wb.save('D:/final_result/myprosody_final.xlsx')