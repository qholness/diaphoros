from flask import Flask, render_template
import main_events as me 

app = Flask(__name__)

@app.route("/")
def hello():
	this_guy = me.player(state = me.random_US_state())
	return """
		<h2>Looks like you\'re getting placed in {0}!</h2>
		<p>And you live in a {1} neighborhood</p>
		""".format(this_guy.state, this_guy.neighborhood)

    # Proposal: more granularity. Choose MSA within a STATE
 #    state_choice = me.random_US_state()
	# msa_choice = random_US_MSA(state_choice)
if __name__ == "__main__":
    app.run(debug=True)