#sample skeleton of flask webframe

from flask import Flask
#WSGI standard
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome NIGGA TO TO TO to my web page"

@app.route('/member')
def members():
    return "yo hello fuck  members"

if __name__ == '__main__':
    app.run(debug=True)
