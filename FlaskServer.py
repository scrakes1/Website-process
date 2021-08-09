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
    code += '\nanswer2 = VariableTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str, 'float': float}
    try:
        exec(code, globalS, loc)
    except Exception as e:
        print(e)
        return str(e) + " Press the Back Button and Try Again!"
    answer = loc['answer2']
    print(answer)
    print(loc['answer2'])
    if answer == 5.0:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/ArithmeticTest', methods=['POST'])
def ArithmeticTest():
    code = request.form['ATAnswer']
    print(code)
    code += '\nanswer2 = ArithmeticTest()'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    exec(code, globalS, loc)
    answer = loc['answer2']
    if answer == [7, 25, 5]:
        return "Good Job!"
    return "Press the Back Button and Try Again!"

@app.route('/Python3Syntax')
def Python3Syntax():
    return f"hi"

    

#Ask about moving static files
#Don't know how to access post method from website
#How to add templates
    #move it to template folder (don't have)

"""@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(f.filename)}")
"""
#How to upload files


with app.test_request_context():
    url_for('static', filename='index.html')
    url_for('static', filename='NewVersion2/Home.html')
    url_for('static', filename='NewVersion2/Python-3-Syntax.html')
    url_for('static', filename='NewVersion2/How-To-Install-Python-3.html')
    print(url_for('welcomepage'))
    #print(url_for('login'))
