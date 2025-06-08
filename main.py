from flask import Flask, render_template
from functions import generate_character

app = Flask(__name__)

@app.route("/")
def home():
    character = generate_character()
    return render_template("index.html", character=character)

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=81)

@app.route('/regenerate')
def regenerate():
    return redirect(url_for('home'))