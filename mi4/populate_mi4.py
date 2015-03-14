import csv, sqlite3, sys

mode =  sys.argv[1]
print mode
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

if mode == "setUp":
	
	with open ('tables.sql') as f:
		schema = f.read()
	c.execute(schema)
	conn.commit()
	csv_reader = csv.reader(open('data.txt'))
	to_db = tuple([i.decode('utf-8') for i in line] for line in csv_reader)
	to_db
	print "database set up"

if mode == "tearDown":
	c.execute("DROP TABLE users")
	conn.commit()
	print "database cleared"
	
