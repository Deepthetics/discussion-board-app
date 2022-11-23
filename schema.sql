CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT, 
    role INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY, 
    title TEXT UNIQUE
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY, 
    title TEXT, 
    created_at TIMESTAMP, 
    user_id INTEGER REFERENCES users, 
    topic_id INTEGER REFERENCES topics
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY, 
    content TEXT, 
    created_at TIMESTAMP, 
    user_id INTEGER REFERENCES users, 
    thread_id INTEGER REFERENCES threads
);