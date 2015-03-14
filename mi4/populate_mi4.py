import csv, sqlite3, sys
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Run with setUp or tearDown as arguments to set up or teardown DB
# Run without arguements to print database


if len(sys.argv)==2:
    mode = sys.argv[1]


    if mode == "setUp":

        with open ('tables.sql') as f:
            schema = f.read()
        c.executescript(schema)
        conn.commit()
        csv_reader = csv.reader(open('data.txt'))
        to_db = tuple([i.decode('utf-8') for i in line] for line in csv_reader)
        to_db
        c.executemany("INSERT INTO users VALUES (?,?,?,?);", to_db)
        


        print "\ndatabase is set up\n"
        print c.execute("SELECT * FROM users").fetchall()

    if mode == "tearDown":
        c.executescript("DROP TABLE users; DROP TABLE messages; DROP TABLE clients;")
        conn.commit()
        print "database cleared"

else:
	print c.execute("SELECT * FROM users;").fetchall()
    print c.execute("SELECT * FROM messages;").fetchall()
    print c.execute("SELECT * FROM clients;").fetchall()
