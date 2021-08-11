from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import redirect 

app = Flask(__name__)

@app.route("/")
def welcomepage():
    return f"hi"


"""
        <form action="/login" method="post">
            <textarea rows = "20" cols = "60" name ="description">#Set x equal to 5 and y = 2. Set variable z to the addition of x and y, and then set variable a to x to the power of y, and then set variable b to the square root of variable a. 
def ArithmeticTest()
    #TYPE BELOW
    x =
    y =
    z = 
    a =
    b = 
    #STOP TYPING
    listanswer = []
    listanswer.append(z)
    listanswer.append(a)
    listanswer.append(b)
    return listanswer
            </textarea><br>
            <input type="submit" value="Submit">
        </form>
        <p>Welcome to the Mountain Lion Computer Science Camp Python Course!</p>
"""

#HTTP METHOD?
#worked prints in terminal
#tab doesn't work
@app.route('/VariableTest', methods=['POST'])
def VariableTest():
    code = request.form['VTAnswer']
    print(code)
    code += '\nvaribaleanswer = VariableTest()'
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
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    try:
        exec(code, globalS, loc)
    except Exception as failure:
        return str(failure) + " Press the Back Button and Try Again!"
    answer = loc['variableanswer']
    if answer == [7, 25, 5]:
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
def FLTest():
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
def FLTest():
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



with app.test_request_context():
    url_for('static', filename='index.html')
    url_for('static', filename='MLCSPython3/Home.html')
    url_for('static', filename='MLCSPython3/Python-3-Syntax.html')
    url_for('static', filename='MLCSPython3/How-To-Install-Python-3.html')
    url_for('static', filename='MLCSPython3/Conditionals.html')
    url_for('static', filename='MLCSPython3/Loops.html')
    print(url_for('welcomepage'))
    print(url_for('VariableTest'))
