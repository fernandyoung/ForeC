from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

#connection
class connection(object):
	"""docstring for connection"""
	def __init__(self,app):
		self.mysql = MySQL(app)

	#check username
	def check_username(self, username):
		cursor = self.mysql.connection.cursor()
		cursor.execute('SELECT * FROM user WHERE username=%s',(username,))
		akun = cursor.fetchone()
		return akun

	def insert(self, username, password):
		cursor = self.mysql.connection.cursor()
		cursor.execute('INSERT INTO user(`username`, `password`, `type`) VALUES(%s,%s,0)',(username,generate_password_hash(password)))
		insert = self.mysql.connection.commit()
		return insert