from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_char = request.form['guess']
    global random_string, count, no_of_turns, guessed_char
    
    if user_char.isalpha() and len(user_char) == 1:
        if user_char in random_string and user_char not in guessed_char:
            count += 1
            guessed_char.add(user_char)
            if count == len(set(random_string)):
                message = "Congrats! You won the game by guessing the word '{}' correctly.".format(random_string)
                return render_template('game.html', word_progress=get_word_progress(), message=message)
        elif user_char in guessed_char:
            no_of_turns -= 1
            message = "The character '{}' is already guessed. Turns left: {}. Please enter a new character.".format(user_char, no_of_turns)
            return render_template('game.html', word_progress=get_word_progress(), message=message)
        else:
            no_of_turns -= 1
            message = "Sorry, '{}' is not in the word. Turns left: {}".format(user_char, no_of_turns)
            return render_template('game.html', word_progress=get_word_progress(), message=message)
    else:
        message = "Please enter a single alphabetic character."
        return render_template('game.html', word_progress=get_word_progress(), message=message)

@app.route('/new_game')
def new_game():
    global random_string, count, no_of_turns, guessed_char
    random_string = random.choice(List_of_words)
    count = 0
    no_of_turns = 12
    guessed_char = set()
    return render_template('index.html')

def get_word_progress():
    word_progress = ""
    for char in random_string:
        if char in guessed_char:
            word_progress += char
        else:
            word_progress += "_ "
    return word_progress

if __name__ == '__main__':
    User_Name = input("Enter your name: ")
    print("Hi, {}! Welcome to Hangman Game created by Radam Sumana.".format(User_Name))
    print("Your hint: US states")

    List_of_words = ['texas', 'california', 'ohio', 'newyork', 'florida', 'georgia', 'arizona', 'idaho',
                     'oregon', 'missouri', 'indiana', 'virginia']
    random_string = random.choice(List_of_words)
    count = 0
    no_of_turns = 12
    guessed_char = set()

    app.run(debug=True)
