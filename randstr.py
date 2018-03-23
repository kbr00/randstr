from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def main():
	str = ''
	i = 0
	while i <= 2048:
		c = chr (random.randint(33,126))
		if c.isalpha():
			str += c
			i += 1
	return str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
