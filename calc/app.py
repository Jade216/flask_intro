from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def to_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def to_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def to_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def to_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

#further study

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<oper>')
def do_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[oper](a,b)

    return str(result)