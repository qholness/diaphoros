from flask import Flask, render_template
import main_events as me 


app = Flask(__name__)

@app.route("/")
def hello():
    return "{}".format(me.random_US_state())

if __name__ == "__main__":
    app.run(debug=True)