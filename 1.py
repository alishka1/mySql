# MySQL for Python
import MySQLdb
import sys

try:
	db = MySQLdb.connect(
		host = 'localhost',
		user = 'root',
		passwd = '',
		db = 'test'
		)
except Exception as e:
	sys.exit('We cant get into the database')

cursor = db.cursor()
cursor.execute('INSERT INTO first (title, text, age) VALUES ("yandex", "money", "2017")')
cursor.execute('SELECT * FROM first')
result = cursor.fetchall()

if result:
	for i in result:
		print i[1] + ' ' + i[2]