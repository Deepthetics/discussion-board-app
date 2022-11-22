from db import db

def get_all():
    sql = "SELECT id, title FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def get_topic(title):
    sql = "SELECT id, title FROM topics WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    topic = result.fetchone()

    if not topic:
        return False

    return topic

def add_topic(title):
    try:
        sql = "INSERT INTO topics (title) VALUES (:title)"
        db.session.execute(sql, {"title":title})
        db.session.commit()
    except:
        return False
    return True

def remove_topic(title):
    try:
        sql = "DELETE FROM topics WHERE title=:title"
        db.session.execute(sql, {"title":title})
        db.session.commit()
    except:
        return False
    return True
