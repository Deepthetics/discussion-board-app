from app import app
from flask import redirect, render_template, request
import topics
import users

@app.route("/")
def index():
    return render_template("index.html", topics=topics.get_all())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Incorrect username or password.")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        
        if len(username) < 3 or len(username) > 20:
            return render_template("error.html", message="Username must be between 3-20 characters long.")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        
        if password1 != password2:
            return render_template("error.html", message="Given passwords do not match.")
        
        if len(password1) < 6 or len(password1) > 20:
            return render_template("error.html", message="Password must be between 5-20 characters long.")
        
        role = request.form["role"]
        
        if role != "1" and role != "2":
            return render_template("error.html", message="Unknown user role.")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Registration failed.")
        return redirect("/")

@app.route("/add_topic", methods=["POST"])
def add_topic():
    title = request.form["title"]

    if len(title) < 1 or len(title) > 40:
        render_template("error.html", message="Topic title must be between 1-40 characters long.")
    
    topics.add_topic(title)
    return redirect("/")
