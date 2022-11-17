from app import app
from flask import redirect, render_template, request, session
import users

@app.route("/")
def index():
    return render_template("index.html")

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

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
