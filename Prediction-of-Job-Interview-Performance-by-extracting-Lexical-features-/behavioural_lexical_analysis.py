# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:21:08 2023

@author: Dhanya
"""

import os
import subprocess
import cmd
import Engaging_Tone_lexical_analysis as f1
import Excited_lexical_analysis as f2
import Calm_lexical_analysis as f3
import Focused_lexical_analysis as f4
import Friendly_lexical_analysis as f5
import NoFillers_lexical_analysis as f6
import paused_lexical_analysis as f7
import speaking_rate_lexical_analysis as f8
import structured_answers_lexical_analysis as f9
import total_lexical_analysis as f11
import recommend_hiring_lexical_analysis as f10

def run_func():
    #f1 = os.path.abspath('D:/Prediction-of-Job-Interview-Performance-by-extracting-Lexical-features-/Engaging_Tone_lexical_analysis.py')
    #p1=subprocess.run(['C:/Users/Dhanya/AppData/Local/Programs/Python/Python311/python.exe',f1])
    f1.run_code()
    f2.run_code()
    f3.run_code()
    f4.run_code()
    f5.run_code()
    f6.run_code()
    f7.run_code()
    f8.run_code()
    f9.run_code()
    f10.run_code()
    f11.run_code()
