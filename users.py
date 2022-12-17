import secrets
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


def login(username, password):
    sql = "SELECT id, username, password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        return False

    if not check_password_hash(user[2], password):
        return False

    session["user_id"] = user[0]
    session["username"] = user[1]
    session["role"] = user[3]
    session["csrf_token"] = secrets.token_hex(16)
    return True

def logout():
    del session["user_id"]
    del session["username"]
    del session["role"]

def register(username, password, role):
    password_hash = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password, role)
                 VALUES (:username, :password, :role)"""
        db.session.execute(sql, {"username":username, "password":password_hash, "role":role})
        db.session.commit()
    except:
        return False
    return login(username, password)
