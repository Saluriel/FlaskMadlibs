from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def form():
    parts_of_speech = story1.prompts

    return render_template("form.html", prompts=parts_of_speech )

@app.route('/story')
def story():
    text = story1.generate(request.args)
    
    return render_template('completed.html', words = text)