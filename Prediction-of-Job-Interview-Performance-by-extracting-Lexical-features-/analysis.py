# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:47:31 2023

@author: Dhanya
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel sheet into a Pandas DataFrame
data = pd.read_excel("D:/Prediction-of-Job-Interview-Performance-by-extracting-Lexical-features-/MI_score.xlsx",sheet_name='Mutual Information')
num_columns = data.shape[1]
col_data=[]
print(data)
print("heyy")
# Iterate over each row in the DataFrame
for _, row in data.iterrows():
    print("e")
    # Extract the x-axis label from the first column of the row
    x_label = row.iloc[0]
    # Extract the top seven values from the other columns as y-axis data
    for i in range(2,num_columns):
      col_data.append(row.iloc[i])
    col_data.sort()
    y_data=col_data[1:7]
    # Plot the graph
    plt.xlabel(x_label)
    plt.ylabel('Features')
    plt.plot(y_data, label=x_label)
    plt.show()
    print("hey")

# Add labels and legend to the graph
# Display the graph
