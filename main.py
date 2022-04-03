from flask import Flask, render_template
import random
app = Flask(__name__)

randnum = random.randint(0,9)
print(randnum)

@app.route("/")
def index():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/hello")
def hello():
    return "hello"

@app.route("/<int:guess>")
def guessed_num(guess):
    if guess == randnum:
        return "<img src='https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif'>"
    elif guess < randnum:
        return "<img src='https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif'>"
    else:
        return "<img src='https://media.giphy.com/media/MXi8nBJjIBgKbyA1MM/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)
