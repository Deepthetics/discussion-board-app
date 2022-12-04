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

def create_thread(title, message_content, user_id, topic_id):
    try:
        sql = "INSERT INTO threads (title, created_at, user_id, topic_id) VALUES (:title, NOW(), :user_id, :topic_id) RETURNING id"
        result = db.session.execute(sql, {"title":title, "user_id":user_id, "topic_id":topic_id})
        thread_id = result.fetchone()[0]
    except:
        return False
    return create_message(message_content, user_id, thread_id)

def create_message(content, user_id, thread_id):
    try:
        sql = "INSERT INTO messages (content, created_at, user_id, thread_id) VALUES (:content, NOW(), :user_id, :thread_id)"
        db.session.execute(sql, {"content":content, "user_id":user_id, "thread_id":thread_id})
        db.session.commit()
    except:
        return False
    return True

def edit_thread(thread_id, title):
    sql = "UPDATE threads SET title=:title WHERE id=:thread_id RETURNING title"
    db.session.execute(sql, {"thread_id":thread_id, "title":title})
    db.session.commit()

def edit_message(message_id, content):
    sql = "UPDATE messages SET content=:content WHERE id=:message_id"
    db.session.execute(sql, {"message_id":message_id, "content":content})
    db.session.commit()

def remove_thread(thread_id):
    try:
        sql = "DELETE FROM threads WHERE id=:thread_id"
        db.session.execute(sql, {"thread_id":thread_id})
        db.session.commit()
    except:
        return False
    return True

def remove_message(message_id):
    try:
        sql = "DELETE FROM messages WHERE id=:message_id"
        db.session.execute(sql, {"message_id":message_id})
        db.session.commit()
    except:
        return False
    return True
