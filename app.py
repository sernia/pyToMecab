from controller.mecab import mecab_result

from flask import Flask
from flask import render_template
app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, World!"

# @app.route('/')
# def hello():
#     name = "Hello World"
#     return name

# @app.route('/good')
# def good():
#     name = "Good"
#     return name

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='flask test', name=name) #変更

@app.route('/mecab')
def mecab():
    #return name
    name = mecab_result()
    return render_template('mecab.html', title='mecabss', name=name) #変更

# if __name__ == "__main__":
#     app.run(debug=True, port=8099, threaded=True)  