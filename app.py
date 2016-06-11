#coding: utf-8
import os
from flask import Flask, render_template
templates_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'dydymvc/views'))
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'dydymvc/static'))


app = Flask(__name__, static_folder=static_path, template_folder=templates_path)

@app.route("/")
def hello():
	lista = [{"nome":"Bruno", "idade": 30},
			 {"nome": "Clara Luna", "idade": 10},
			 {"nome": "Antonia", "idade": 2}]

	return render_template("index.html", listagem=lista)

if __name__ == "__main__":
	app.run(debug=True)