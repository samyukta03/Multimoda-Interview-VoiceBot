# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:46:31 2023

@author: Dhanya
"""

import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file
df = pd.read_excel('coeff.xlsx', sheet_name='Coeff')

# Get the values from column 2
values = df.iloc[:, 1]

# Get the labels from column 1
labels = df.iloc[:, 0]

# Create the horizontal bar graph
plt.barh(labels, values)

# Add labels and title
plt.xlabel('Correlation Coefficient')
plt.ylabel('Attributes')


# Display the graph
plt.show()
