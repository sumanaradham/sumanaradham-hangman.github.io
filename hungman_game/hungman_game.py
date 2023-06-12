import random

def start_game():
    List_of_words = ['texas', 'california', 'ohio', 'newyork', 'florida', 'georgia', 'arizona', 'idaho',
                     'oregon', 'missouri', 'indiana', 'virginia']
    random_string = random.choice(List_of_words)
    count = 0
    no_of_turns = 12
    guessed_char = set()
    return random_string, count, no_of_turns, guessed_char

def play_game(random_string, count, no_of_turns, guessed_char, user_char):
    if user_char.isalpha() and len(user_char) == 1:
        if user_char in random_string and user_char not in guessed_char:
            count += 1
            guessed_char.add(user_char)
            if count == len(set(random_string)):
                message = "Congrats! You won the game by guessing the word '{}' correctly.".format(random_string)
                return count, no_of_turns, guessed_char, message
        elif user_char in guessed_char:
            no_of_turns -= 1
            message = "The character is already guessed. Turns left: {}. Please enter a new character.".format(no_of_turns)
            return count, no_of_turns, guessed_char, message
        else:
            no_of_turns -= 1
            message = "Sorry, '{}' is not in the word. Turns left: {}".format(user_char, no_of_turns)
            return count, no_of_turns, guessed_char, message
    else:
        message = "Please enter a single alphabetic character."
        return count, no_of_turns, guessed_char, message


def no_of_turns():
        word_progress = ""
        for char in random_string:
           if char in guessed_char:
    
    
            #print("check2",char)
            word_progress += char
        else:
            word_progress += "_" + " "
    
    print(word_progress)