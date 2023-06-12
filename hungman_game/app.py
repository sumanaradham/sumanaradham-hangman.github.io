from flask import Flask, render_template, request
from  hungman_game import start_game, play_game

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    name = request.form['name']
    random_string, count, no_of_turns, guessed_char = start_game()
    return render_template('game.html', name=name, random_string=random_string, count=count, no_of_turns=no_of_turns, guessed_char=guessed_char)

@app.route('/guess', methods=['POST'])
def guess():
    name = request.form['name']
    random_string = request.form['random_string']
    count = int(request.form['count'])
    no_of_turns = int(request.form['no_of_turns'])
    guessed_char = set(request.form['guessed_char'].split(','))
    user_char = request.form['char']
    
    count, no_of_turns, guessed_char, message = play_game(random_string, count, no_of_turns, guessed_char, user_char)
    
    return render_template('game.html', name=name, random_string=random_string, count=count, no_of_turns=no_of_turns, guessed_char=guessed_char, message=message)

if __name__ == '__main__':
    app.run(debug=True)
