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

def get_threads(topic_id):
    sql = """SELECT threads.id, threads.title, threads.created_at, users.username FROM threads, users
             WHERE threads.user_id=users.id AND threads.topic_id=:topic_id ORDER BY threads.id;"""
    result = db.session.execute(sql, {"topic_id":topic_id})
    threads = result.fetchall()
    return threads

def get_messages(thread_id):
    sql = """SELECT messages.id, messages.content, messages.created_at, users.username FROM messages, users
             WHERE messages.user_id=users.id AND messages.thread_id=:thread_id ORDER BY messages.id;"""
    result = db.session.execute(sql, {"thread_id":thread_id})
    messages = result.fetchall()
    return messages
