
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import url_for
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("static/MLCSPython3/Home.html", code=302)

@app.route('/VariableTest', methods=['POST'])
def VariableTest():
    code = request.form['VTAnswer']
    code += '\nvariableanswer = VariableTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str, 'float': float}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    #print(answer)
    #print(loc['variableanswer'])
    if answer == 5.0:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/ArithmeticTest', methods=['POST'])
def ArithmeticTest():
    code = request.form['ATAnswer']
    code += '\nvariableanswer = ArithmeticTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str, 'pow':pow}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == [7, 25, 5.0]:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/IfTest', methods=['POST'])
def IfTest():
    code = request.form['IfAnswer']
    code += '\nvariableanswer = IfStatementTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 1:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/ElifTest', methods=['POST'])
def ElifTest():
    code = request.form['ElifAnswer']
    code += '\nvariableanswer = ElseIfStatementTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 9:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/ComparatorTest', methods=['POST'])
def ComparatorTest():
    code = request.form['ComparatorAnswer']
    code += '\nvariableanswer = ComparatorTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == False:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/NestedIfTest', methods=['POST'])
def NestedIfTest():
    code = request.form['NestedIfAnswer']
    code += '\nvariableanswer = NestedIfStatementTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 3:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/FLTest', methods=['POST'])
def FLTest():
    code = request.form['FLAnswer']
    code += '\nvariableanswer = ForLoopTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 4:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/WLTest', methods=['POST'])
def WLTest():
    code = request.form['WLAnswer']
    code += '\nvariableanswer = WhileLoopTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 55:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/NFLTest', methods=['POST'])
def NFLTest():
    code = request.form['NFLAnswer']
    code += '\nvariableanswer = NestedForLoopTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 40:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/LP', methods=['POST'])
def LP():
    code = request.form['LPAnswer']
    code += '\nvariableanswer = LoopPractice()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 25:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/ListTest', methods=['POST'])
def ListTest():
    code = request.form['ListAnswer']
    code += '\nvariableanswer = ListTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str, 'len':len}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == [1, 3, 4]:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/DictTest', methods=['POST'])
def DictTest():
    code = request.form['DictAnswer']
    code += '\nvariableanswer = DictionaryTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if (1, "goodbye") in answer.items():
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/TupleTest', methods=['POST'])
def TupleTest():
    code = request.form['TupleAnswer']
    code += '\nvariableanswer = TupleTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == (1, 2, 3, 7, 8, 9):
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/LDTP', methods=['POST'])
def LDTP():
    code = request.form['LDTPAnswer']
    code += '\nvariableanswer = List/Dictionary/TuplePractice()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == 66:
        return "Good Job!"
    return "Press the Back Button and Try Again!"


with app.test_request_context():
    url_for('static', filename='MLCSPython3/Home.html')
    url_for('static', filename='MLCSPython3/Python-3-Syntax.html')
    url_for('static', filename='MLCSPython3/How-To-Install-Python-3.html')
    url_for('static', filename='MLCSPython3/Conditionals.html')
    url_for('static', filename='MLCSPython3/Loops.html')
    url_for('static', filename='MLCSPython3/Lists-Dictionaries-Tuples.html')

