from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title = "Home")


@app.route('/contact')
def contact():
    return render_template("contact.html", title = "contact")


@app.route('/about')
def about():
    return render_template("about.html", title = "about")


@app.route('/all_frogs')
def all_frogs():
    conn = sqlite3.connect('frog.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Frogs')
    frogs = cur.fetchall()
    return render_template("all_pizzas.html", frogs=frogs)





if __name__ == "__main__":  
    app.run(debug=True)