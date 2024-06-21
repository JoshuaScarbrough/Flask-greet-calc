# Put your app in here.
from flask import Flask, request
import math 
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/')
def startup():
    return "Joshua Scarbrough"


@app.route('/add')
def add():
    """Add a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = a + b
    return str(result)

@app.route('/sub')
def sub():
    """Substract b from a."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = a - b
    return str(result)

    return a - b

@app.route('/mult')
def mult():
    """Multiply a and b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = a * b
    return str(result)

@app.route('/div')
def div():
    """Divide a by b."""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = a / b
    return str(result)



if __name__ == '__main__':
    app.run(debug=True)