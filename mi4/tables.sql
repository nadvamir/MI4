CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    bio TEXT
);

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fromID INTEGER,
    toID INTEGER,
    message TEXT
);

CREATE TABLE clients (
    Matr INTEGER,
    Name TEXT,
    Surname TEXT,
    DOB TEXT,
    Email TEXT,
    Contact_Phone TEXT,
    Role TEXT,
    UndercoverName TEXT,
    UndercoverSurname TEXT,
    Passphrase TEXT
);
