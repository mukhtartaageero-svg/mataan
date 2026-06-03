import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/room")
def room():

    conn = sqlite3.connect("mataan.db")
    c = conn.cursor()

    c.execute(
        "SELECT sender, message FROM messages"
    )

    messages = c.fetchall()

    conn.close()

    return render_template(
        "room.html",
        messages=messages
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("mataan.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return "User Created ✅"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def user_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("mataan.db")
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = c.fetchone()

        conn.close()

        if user:
            return render_template("home.html")

        return "Invalid Login ❌"

    return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/send", methods=["POST"])
def send():

    sender = "you"
    receiver = "fatima"

    message = request.form["message"]

    conn = sqlite3.connect("mataan.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages(sender,receiver,message) VALUES(?,?,?)",
        (sender, receiver, message)
    )

    conn.commit()
    conn.close()

    return redirect("/room")


app.run(host="0.0.0.0", port=5000)
