CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT, 
    role INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY, 
    title TEXT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY, 
    title TEXT, 
    created_at TIMESTAMP, 
    user_id INTEGER REFERENCES
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY, 
    title TEXT, 
    created_at TIMESTAMP, 
    user_id INTEGER REFERENCES
);