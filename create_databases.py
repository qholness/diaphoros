import sqlite3
import csv

conn = sqlite3.connect("./data/databases/diadb.db")
c = conn.cursor()

def make_unlocode(c = c):
	# Make UN/LOCODE table http://www.unece.org/cefact/locode/service/location.html
	c.execute('''drop table if exists unlocode''')
	c.execute('''create table unlocode (location_id text, location text)''')

	with open("./data/raw_data/unlocode.csv") as unlocode_csv:
		locodes = [i for i in csv.reader(unlocode_csv)]

	c.executemany("insert into unlocode values (?,?)",locodes)
	conn.commit()

