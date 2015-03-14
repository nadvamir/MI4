from django.db import models, connection
# class User():
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE UserProfile(UserName varchar(128)")
#
#     cursor.execute("INSERT INTO UserProfile('Jim')")


# agent information
class Agent:
    # constructor from sql
    def __init__(self, row):
        self.id = row[0]
        self.bio = row[1]

    # get an agent by user id
    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE id = ?'
        return Agent(cursor.execute(query, id).fetchone())

    # save to a database
    def save(self):
        cursor = connection.cursor()
        query = 'UPDATE users SET bio = ? WHERE id = ?'
        cursor.execute(query, bio, id)
        connection.commit()

# messages information
class Message:
    # constructor from sql
    def __init__(self, row):
        self.id = row[0]
        self.fromId = row[1]
        self.toId = row[2]
        self.message = row[3]
        self.fromName = row[4]
        self.toName = row[5]

    # get a list of messages for a user
    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = '''SELECT
                    id, fromId, toId, message,
                    u1.username, u2.username
                FROM messages, auth_user as u1,
                    auth_user as u2
                WHERE fromID = u1.id AND
                    toID = u2.id AND
                    (fromID = ? OR toID = ?)'''
        return [Message(row) for row in cursor.execute(query, id, id).fetchall()]

    # store a new message
    def save(self, id):
        cursor = connection.cursor()
        query = 'INSERT INTO messages VALUES (?, ?, ?, ?)'
        cursor.execute(query, self.id, self.fromId, self.toId, self.message)
        connection.commit()

# client information
class Client:
    # construction for a row
    def __init__(self, row):
        self.matr = row[0]
        self.name = row[1]
        self.surname = row[2]
        self.DOB = row[3]
        self.email = row[4]
        self.contactPhone = row[5]
        self.role = row[6]
        self.undercoverName = row[7]
        self.undercoverSurname = row[8]
        self.passphrase = row[9]

    # get an instance by matr id
    @staticmethod
    def get(matr):
        cursor = connection.cursor()
        query = 'SELECT * FROM clients WHERE Matr = ?'
        return Agent(cursor.execute(query, matr).fetchone())

    # store updated information
    def save(self):
        cursor = connection.cursor()
        query = '''UPDATE clients SET 
                    name = ?,
                    surname = ?,
                    dob = ?,
                    email = ?,
                    contactPhone = ?,
                    role = ?,
                    undercoverName = ?,
                    undercoverSurname = ?,
                    passphrase = ?
                WHERE 
                    matr = ?'''
        cursor.execute(query,
                self.name,
                self.surname,
                self.DOB,
                self.email,
                self.contactPhone,
                self.role,
                self.undercoverName,
                self.undercoverSurname,
                self.passphrase,
                self.matr)
        connection.commit()

