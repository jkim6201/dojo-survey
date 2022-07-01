from flask import Flask, render_template,session, redirect, request
app = Flask(__name__)
app.secret_key="1<3ra3"

@app.route('/')
def dojo():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/survey')


@app.route('/survey')
def survey():
    return render_template('survey.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)# Run the app in debug mode.

