from db import db

def get_all():
    sql = "SELECT id, title FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def add_topic(title):
    sql = "INSERT INTO topics (title) VALUES (:title)"
    db.session.execute(sql, {"title":title})
    db.session.commit()
