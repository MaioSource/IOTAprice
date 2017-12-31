from flask import Flask, render_template, request
import re
import base64
import MySQLdb


app = Flask(__name__)
conn = MySQLdb.connect(host="your_host", user="your_user", passwd="your_pass", db="your_db_name")

def emailToDB(email):
	cursor = conn.cursor()
	ee = base64.b64encode(str(email))
	query = ("INSERT INTO Subscriber () VALUES ('%s')" %(ee))
	cursor.execute(query)
	conn.commit()

def existe(email):
	cursor = conn.cursor()
	ee = base64.b64encode(str(email))
	query = ("SELECT Mail FROM Subscriber WHERE Mail = '%s'" %(ee))
	cursor.execute(query)
	data = cursor.fetchall()
	if str(data) != '()':
		return True
	return False

def checked(email):
	m = re.search('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', str(email))
	try:
		m.group()
	except Exception as e:
		return ["Mail not correct", False]

	if existe(email):
		return ["You are already subscribed", False]

	if len(str(email)) > 50:
		return ["Mail too large", False]
	return ["OK", True]

@app.route('/', methods=['POST', 'GET'])
def inicio():
	if request.method == 'POST':
		email = request.form['email']
		validation = checked(email)
		if validation[1]:
			emailToDB(email)
			return render_template('ok.html', email = email)
		else:
			return render_template("index.html", error=True, msg = validation[0])
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
