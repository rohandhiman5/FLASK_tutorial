#integrating Html with Flask
from flask import Flask, render_template, url_for, redirect,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>33:
        res= "pass"
    else:
        res= "fail"
    return render_template('results.html',result=res)


@app.route('/fail/<int:score>')
def fail(score):
    return "you have failed the examination "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>33:
        return redirect(url_for("success",score= marks))
    else:
        result=fail
        return redirect(url_for("fail",score= marks))


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science +maths+c+datascience)/4
   
    return redirect(url_for("success",score=total_score))




    

if __name__=='__main__':
    app.run(debug=True)