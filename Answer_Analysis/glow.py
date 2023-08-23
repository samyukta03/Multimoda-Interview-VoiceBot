from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

@app.route('/run', methods=['POST'])
def run():
    arg = request.form.get('arg')
    if arg == 'on':
        print("Glow on")
        return 'on'
    elif arg == 'off':
        print("Glow off")
        return 'off'
    else:
        return 'invalid argument'