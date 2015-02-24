import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')
cur = con.cursor()

theCities = (('New York City', 'NY'),
('Boston', 'MA'),
('Chicago', 'IL'),
('Miami', 'FL'),
('Dallas', 'TX'),
('Seattle', 'WA'),
('Portland', 'OR'),
('San Francisco', 'CA'),
('Los Angeles', 'CA'),
('Washington', 'DC'),
('Houston', 'TX'),
('Las Vegas', 'NV'),
('Atlanta', 'GA'))

theWeather = (('New York City', 2013, 'July', 'January', 62),
('Boston', 2013, 'July', 'January', 62),
('Chicago', 2013, 'July', 'January', 59),
('Miami', 2013, 'August', 'January', 84),
('Dallas', 2013, 'July', 'January', 77),
('Seattle', 2013, 'July', 'January', 61),
('Portland', 2013, 'July', 'December', 63),
('San Francisco', 2013, 'September', 'December', 64),
('Los Angeles', 2013, 'September', 'December', 75),
('Washington', 2013, 'July', 'January', 55),
('Houston', 2013, 'July', 'January', 79),
('Las Vegas', 2013, 'July', 'December', 88),
('Atlanta', 2013, 'July', 'January', 72))

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE cities(name text, state text)")
	cur.executemany("INSERT INTO cities VALUES(?,?)", theCities)
	cur.execute("CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", theWeather)
	cur.execute("SELECT name, state FROM cities INNER JOIN weather on NAME = city WHERE warm_month = 'July'")
	rows = cur.fetchall()
	df = pd.DataFrame(rows)

i = 0
total = df[0].count()
sentence = "The cities that are warmest in July are: "
while i < total - 1:
    sentence = sentence + str(df.loc[i,0]) + ', ' + str(df.loc[i,1]) + ', '
    i += 1

sentence = sentence + 'and ' + str(df.loc[i,0]) + ', ' + str(df.loc[i,1]) + '.'
print sentence