import os
import random

from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue1": "#30336b",
    "darkblue": "#be2edd",
    "pink": "#130f40",
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue1","darkblue","pink"])

@app.route("/")
def main():
    print(color)
    return render_template('index.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('index.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('index.html', name=socket.gethostname(), contents=contents, color=color_codes[color])
    
@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
