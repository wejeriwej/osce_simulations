from flask import Flask, render_template, url_for, request, flash
from datetime import datetime
import subprocess



app = Flask(__name__)
app.secret_key = "yes"


@app.route("/") #flash("hi "+ str(request.form['name_input'])+", great to see you")
def index():
    flash("Click the button to go to the first case.")
    return render_template('index.html')

@app.route("/second_page", methods=["POST", "GET"])
def second_page():
    return render_template('trial.html')

@app.route("/recording", methods=["POST", "GET"])
def recording():
    subprocess.call(["python",'testing2.py'], shell=True,) 
    return 'successful, well done'


if __name__ == "__main__":
        app.run(debug=True)