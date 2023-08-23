# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:45:20 2023

@author: Dhanya
"""
from flask import Flask, render_template
from datetime import datetime
import signal
import os
import time

def signal_handler(sig, frame):
    os._exit(1)

signal.signal(signal.SIGINT, signal_handler)

app = Flask(__name__)

@app.route('/')
def index():
    print("In here 1")
    return render_template('timer.html')

@app.route('/timer', methods=['POST'])
def timer():
    print("hey")
    with open('templates/timer.html', 'r') as file:
     html = file.read()
     time_left=3
     new_element = '<script> function countdown() {{ var time_left = {0}; document.getElementById("timer").innerHTML = time_left; if (time_left == 0) {{ clearInterval(interval); document.getElementById("timer").innerHTML = "Time\'s up!"; }} time_left--; }} var interval = setInterval(countdown, 1000);</script>'.format(time_left)
     html = html.replace('<body>', f'<body>{new_element}')
    with open('templates/timer.html', 'w') as file:
      file.write(html)
    print("done")
    return "true"

if __name__ == '__main__':
    print("hello")
    app.run()
