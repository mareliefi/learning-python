import os
import sqlite3
import sys

db_filename = "mydatabase.db"
inid = sys.argv[1]
innat = sys.argv[2]

exists = os.path.exists(db_filename)
if exists:
  os.unlink(db_filename)

conn = sqlite3.connect(db_filename)
schema = """create table person (
  id integer primary key autoincrement not null,
  name text not null,
  dob date,
  nationality text,
  gender text)
"""
conn.executescript(schema)

people = """insert into person (name,dob, nationality, gender)
values ("James Hetfield","1955-02-21","South African","male");
insert into person (name, dob, nationality,gender)
values ("Maria Nunes","1995-03-16","Spanish","female")
"""
conn.executescript(people)

cursor = conn.cursor()
cursor.execute("select id, name, dob, nationality, gender from person")
for row in cursor.fetchall():
  id, name, dob, nationality, gender = row
  print ("%3d %15s %12s %10s %6s" % (id,name,dob,nationality,gender))

query = "update person set nationality = :nat where id = :id"
cursor.execute(query, {'id':inid, 'nat':innat})
cursor.execute("select id, name, dob, nationality, gender from person")
for row in cursor.fetchall():
  id, name, dob, nationality, gender = row
  print ("%3d %15s %12s %10s %6s" % (id,name,dob,nationality,gender))