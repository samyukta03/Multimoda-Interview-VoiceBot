# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:43:23 2023

@author: Dhanya
"""

from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/page')
def index():
    print("Hello from test1")
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 20:
            break
        time_left = 20 - int(elapsed_time)
        return render_template('timer.html', time_left=time_left)

if __name__ == '__main__':
    app.run(debug=True)
