from app import app
from flask import redirect, render_template, request, session
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
        return render_template("error.html", message="Topic title must be between 1-40 characters long.")

    if not topics.add_topic(title):
        return render_template("error.html", message="Operation failed.")
    return redirect("/")

@app.route("/remove_topic", methods=["POST"])
def remove_topic():
    title = request.form["title"]

    if not topics.get_topic(title):
        return render_template("error.html", message="Topic with a given title not found. Check the topic title.")

    if not topics.remove_topic(title):
        return render_template("error.html", message="Operation failed.")
    return redirect("/")

@app.route("/topic/<int:topic_id>")
def topic(topic_id):
    session["topic_id"] = topic_id
    threads = topics.get_threads(topic_id)
    return render_template("topic.html", threads=threads)

@app.route("/thread/<int:thread_id>")
def thread(thread_id):
    session["thread_id"] = thread_id
    messages = topics.get_messages(thread_id)
    return render_template("thread.html", messages=messages)

@app.route("/create_thread", methods=["GET", "POST"])
def create_thread():
    if request.method == "GET":
        return render_template("new_thread.html")

    if request.method == "POST":
        title = request.form["title"]
        message_content = request.form["message_content"]
        user_id = session["user_id"]
        topic_id = session["topic_id"]

        if len(title) < 1 or len(title) > 40:
            return render_template("error.html", message="Thread title must be between 1-40 characters long.")
        
        if not topics.create_thread(title, message_content, user_id, topic_id):
            return render_template("error.html", message="Operation failed.")
        return redirect(f"/topic/{topic_id}")

@app.route("/create_message")
def create_message():
    pass
