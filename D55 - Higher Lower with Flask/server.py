from flask import Flask
import random

random_number = random.randint(1, 9)

app = Flask(__name__)

@app.route("/")
def guess():
    return ('<h1 style="text-align: center">Guess a number between 0 and 9!</h1>'
            '<center><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3NpcDhkdWdmNXh0eW1qaDNrNHU4NHZtOGdvaDY4d3o3dXhhYmMxOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gT9BPNXovhAs0/giphy.gif"></center>')

@app.route("/<number>")
def high_or_low(number):
    if int(number) > random_number:
        return ('<h1 style="color:red">Too high!</h1><br>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeno0cGs3NGZ3aGhncWJ3Yzc0djk3d2J0eWwxdTl0bDR6dnFnbTJxNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V4g5wHFqnpVFMP0VDa/giphy.gif">')
    elif int(number) < random_number:
        return ('<h1 style="color:blue">Too low!</h1><br>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmtzYjRwZGRnZzAxaTdsYjNwazB1NmVybzZmYWN2bTdkMTMyenYxayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OnE1lUUmQLvKX95lOZ/giphy.gif">')
    else:
        return ('<h1 style="color:green">Correct!</h1><br>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHg2dWt6MzF4NXpsaGl0Z2NtZjg4dnJ4MHZyOXo1eXAzZW9jYzJqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7znrdTgB4Xbyv2woFv/giphy.gif">')

@app.route("/flapjacks")
def flapjacks():
    return '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXFnOWM2eHIwYzRwZjF3MGloenljaHA2NGMxZTc2NzJ3MHBsZjl4cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2SnYiMRDxK3F6/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)

