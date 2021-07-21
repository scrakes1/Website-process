from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import redirect 

app = Flask(__name__)

@app.route("/")
def welcomepage():
    return '''
        <form action="/login" method="post">
            <textarea rows = "20" cols = "60" name ="description">
            </textarea><br>
            <input type="submit" value="Submit">
        </form>
        <p>Welcome to the Mountain Lion Computer Science Camp Python Course!</p>
    '''

#HTTP METHOD?
#worked prints in terminal
#tab doesn't work
@app.route('/login', methods=['POST'])
def login():
    code = request.form['description']
    print(code)
    code += '\nanswer2 = fizzbuzz(30)'
    #code += '\nprint(fizzbuzz(30))'
    loc = {}
    globalS = {'__builtins__': None, 'range': range, 'str': str}
    exec(code, globalS, loc)
    answer = loc['answer2']
    if answer == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16","17","Fizz","19","Buzz","Fizz","22","23","Fizz","Buzz","26","Fizz","28","29","FizzBuzz"]:
        return "Good Job!"
    return code

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
    print(url_for('welcomepage'))
    print(url_for('hello', name=''))
    #print(url_for('login'))
