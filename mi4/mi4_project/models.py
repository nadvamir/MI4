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
        self.username = row[2]

    # get an agent by user id
    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = 'SELECT u.id, bio, username FROM users, auth_user as u WHERE u.id = ? AND u.id = users.id'
        row = cursor.execute(query, (id, )).fetchone()
        return Agent(row) if None != row else None

    # get a list of agents
    @staticmethod
    def list():
        cursor = connection.cursor()
        query = 'SELECT id FROM auth_user'
        return [Agent.get(row[0]) for row in
                cursor.execute(query).fetchall()]

    # save to a database
    def save(self):
        cursor = connection.cursor()
        query = 'UPDATE users SET bio = ? WHERE id = ?'
        print self.bio
        print self.id
        cursor.execute(query, (self.bio, self.id))
        connection.commit()

    # convert to dicitonary
    def toDict(self):
        return {
            'id': self.id,
            'bio': self.bio,
            'username': self.username
        }

# messages information
class Message:
    # constructor from sql
    def __init__(self, row):
        self.id = row[0]
        self.fromId = row[1]
        self.toId = row[2]
        self.message = row[3]
        if len(row) > 4:
            self.fromName = row[4]
            self.toName = row[5]

    # get a list of messages for a user
    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = '''SELECT
                    messages.id, fromId, toId, message,
                    u1.username, u2.username
                FROM messages, auth_user as u1,
                    auth_user as u2
                WHERE fromID = u1.id AND
                    toID = u2.id AND
                    (fromID = ? OR toID = ?)
                ORDER BY messages.id DESC'''
        return [Message(row) for row in cursor.execute(query, (id, id)).fetchall()]

    # store a new message
    def save(self):
        cursor = connection.cursor()
        query = 'INSERT INTO messages VALUES (?, ?, ?, ?)'
        cursor.execute(query, (self.id, self.fromId, self.toId, self.message))
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
        row = cursor.execute(query, (matr, )).fetchone()
        return Client(row) if None != row else None

    # list all clients
    @staticmethod
    def list():
        cursor = connection.cursor()
        query = 'SELECT matr FROM clients'
        return [Client.get(row[0]) for row in
                cursor.execute(query).fetchall()]

    # store updated information
    def save(self):
        cursor = connection.cursor()
        query = '''UPDATE clients SET 
                    name = ?,
                    surname = ?,
                    dob = ?,
                    email = ?,
                    contact_Phone = ?,
                    role = ?,
                    undercoverName = ?,
                    undercoverSurname = ?,
                    passphrase = ?
                WHERE 
                    matr = ?'''
        cursor.execute(query, (
                self.name,
                self.surname,
                self.DOB,
                self.email,
                self.contactPhone,
                self.role,
                self.undercoverName,
                self.undercoverSurname,
                self.passphrase,
                self.matr))
        connection.commit()

    def toDict(self):
        return {
            'matr': self.matr,
            'name': self.name,
            'surname': self.surname,
            'DOB': self.DOB,
            'email': self.email,
            'contactPhone': self.contactPhone,
            'role': self.role,
            'undercoverName': self.undercoverName,
            'undercoverSurname': self.undercoverSurname,
            'passphrase': self.passphrase
        }
