#building URL dynamically
from flask import Flask,redirect, url_for


app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my webpage"


@app.route('/success/<int:score>')
def success(score):
    return "you have passed the examination and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "u have failed the examination and the score is "+str(score)

@app.route('/result/<int:marks>')
def result(marks):
    if marks>33:
        return redirect(url_for("success",score=marks ))
    else:
        return redirect(url_for("fail",score=marks))

if __name__=='__main__':
    app.run(debug=True)