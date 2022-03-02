from flask import Flask
from random import randint

Flask_App = Flask(__name__)


def higher_lower_game(function):
    random_number = randint(0, 9)
    def warpped(number):
        gussed_number = int(function(number))
        if gussed_number == random_number:
            return f"<h1>WoW you did it the random number is {random_number}</h1>" \
                   "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        elif gussed_number > random_number:
            return f"<h1>No it is too high the random number is {random_number}</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
        else:
            return f"<h1>No it is too low the random number is {random_number}</h1>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    return warpped


@Flask_App.route("/")
def guss_welcome():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@Flask_App.route("/<number>")
@higher_lower_game
def gussed_number(number):
    return number


if __name__ == '__main__':
    Flask_App.run(debug=True)
