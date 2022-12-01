import re
from flask import redirect, render_template, request, session
from app import app
import discussions
import users


@app.route("/")
def index():
    return render_template("index.html", topics=discussions.get_all())

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

    if not discussions.add_topic(title):
        return render_template("error.html", message="Operation failed.")
    return redirect("/")

@app.route("/remove_topic", methods=["POST"])
def remove_topic():
    title = request.form["title"]

    if not discussions.get_topic(title):
        return render_template("error.html", message="Topic with a given title not found. Check the topic title.")

    if not discussions.remove_topic(title):
        return render_template("error.html", message="Operation failed.")
    return redirect("/")

@app.route("/topic/<int:topic_id>")
def topic(topic_id):
    session["topic_id"] = topic_id
    threads = discussions.get_threads(topic_id)
    return render_template("topic.html", threads=threads)

@app.route("/thread/<int:thread_id>")
def thread(thread_id):
    session["thread_id"] = thread_id
    messages = discussions.get_messages(thread_id)
    times = []

    for message in messages:
        times.append(re.search(r"\d+:\d+:\d+", message.created_at.time().isoformat()).group())

    return render_template("thread.html", messages=messages, times=times, zip=zip)

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

        if not discussions.create_thread(title, message_content, user_id, topic_id):
            return render_template("error.html", message="Operation failed.")
        return redirect(f"/topic/{topic_id}")

@app.route("/create_message", methods=["GET", "POST"])
def create_message():
    if request.method == "GET":
        return render_template("new_message.html")

    if request.method == "POST":
        content = request.form["content"]
        user_id = session["user_id"]
        thread_id = session["thread_id"]

    if not discussions.create_message(content, user_id, thread_id):
        return render_template("error.html", message="Operation failed.")
    return redirect(f"/thread/{thread_id}")

@app.route("/edit_message/<int:message_id>/<message_content>/<username>", methods=["GET", "POST"])
def edit_message(message_id, message_content, username):
    if session["username"] != username:
        return render_template("error.html", message="Unauthorized action.")

    if request.method == "GET":
        return render_template("edit_message.html", message_id=message_id, message_content=message_content, username=username)

    if request.method == "POST":
        content = request.form["content"]
        discussions.edit_message(message_id, content)

    thread_id = session["thread_id"]
    return redirect(f"/thread/{thread_id}")

@app.route("/remove_message/<int:message_id>/<username>")
def remove_message(message_id, username):
    if session["username"] != username:
        return render_template("error.html", message="Unauthorized action.")

    if not discussions.remove_message(message_id):
        return render_template("error.html", message="Operation failed.")

    thread_id = session["thread_id"]
    return redirect(f"/thread/{thread_id}")
