# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:41:48 2023

@author: Dhanya
"""

import matplotlib.pyplot as plt

values = [90.086, 85.87754768339886, 99.87652560151428]
labels = ['L', 'P', 'L+P']

plt.bar(labels, values)
plt.xlabel('Features')
plt.ylabel('Accuracy')
plt.title('How Each Feature affects the Excited Attribute')

