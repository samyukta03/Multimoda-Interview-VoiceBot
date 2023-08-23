# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:52:12 2023

@author: Dhanya
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

ws = openpyxl.load_workbook('MI_score.xlsx')
sheet = ws['Mutual Information']


values_row_5 = [cell.value for cell in sheet[5]]
values_row_6 = [cell.value for cell in sheet[6]]
values_row_11 = [cell.value for cell in sheet[6]]

values_row_11 = values_row_11[1:]
values_row_11 = [float(value) for value in values_row_11]

# Sort the values
values_row_11_sorted = sorted(values_row_11)
# Plot each row as a separate line graph
plt.plot(values_row_11_sorted,label='Excited')
plt.xlabel('Lexical Features')
plt.ylabel('Mutual Information')
plt.title('Mutual Information between Lexical Features and attribute')

# Add legend
plt.legend()

# Display the graph
plt.show()

#plt.plot(values_row_6, label='Excited')
#plt.plot(values_row_11, label='Friendly')

# Add labels and title