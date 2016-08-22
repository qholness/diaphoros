from flask import render_template
from app import app
from main_events import *

@app.route("/")
@app.route("/index")
def introduction():
	this_guy = player(state = random_US_state())
	return render_template("home.html", state = this_guy.state)

@app.route("/game")
def MainGame():
	return render_template("Game.html")
@app.route("/game/<daynumber>")
def advanceDays(daynumber):
	return render_template("advanceDays.html", dayCount = daynumber)