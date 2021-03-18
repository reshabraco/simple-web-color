import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name___)

color_codes = {
    "red": "#e74c3c",
    "green": "16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","pink","darkblue"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

if __name__== "__main__":
    app.run(host="0.0.0.0", port="8080") 
