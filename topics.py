from db import db

def get_all():
    sql = "SELECT id, title FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics
