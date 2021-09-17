from flask import Flask, render_template, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    height = 25
    width = 25
    if request.method == "POST":
        height = request.form["height"]
        width = request.form["width"]
    GameOfLife(width=int(width), height=int(height))
    return render_template("index.html", width=width, height=height)


@app.route("/live")
def live():
    game_on = GameOfLife()
    if game_on.counter > 0:
        game_on.form_new_generation()
    game_on.counter += 1
    return render_template("live.html", game_on=game_on)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
