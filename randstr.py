from flask import Flask, request
import random

app = Flask(__name__)

def genStr (n):
	str = ''
	i = 0
	while i < n:
		c = chr (random.randint(33,126))
		if c.isalpha():
			str += c
			i += 1
	return str

@app.route("/")
def main_get():
	return genStr(2048)

@app.route("/",methods=['POST'])
def main_post():
	try:
		n = int(request.form['n'])
		return genStr(n)
	except Exception:
		return "ERROR"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
