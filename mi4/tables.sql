CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text,
    password text,
    bio text
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fromID INTEGER,
    toID INTEGER
    message text
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    data text
);
