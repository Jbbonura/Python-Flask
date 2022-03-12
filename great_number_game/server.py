from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "shh its a secret"

@app.route('/')
def index():
    if 'the_number' not in session:
        session['the_number'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['user_guess'] = request.form['guess']
    if session['the_number'] == int(session['user_guess']):
        session['message']= "You guessed it!"

    elif session['the_number'] < int(session['user_guess']): 
        session['message']= "Too high"
    
    else:
        session['message'] = "Too low"

    if 'guesses' not in session:
        session['guesses'] = 1
    else:
        session['guesses'] += 1
    return redirect('/')

@app.route('/play_again', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)