from flask import Flask
from markupsafe import escape
from flask import render_template
from base64 import b64encode
import pandas as pd
from matplotlib import pyplot as plt
from flask_sqlalchemy import SQLAlchemy

from bot import *


bot = Bot(path="./bot/credentials.txt")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"

db = SQLAlchemy(app)

class Stock(db.Model):
	ticker = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)


@app.route('/')
def overview():
	data = bot.get_overview()
	return render_template('overview.html', data=data)

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')


@app.route('/transactions')
def transactions():
	return render_template('transactions.html')


@app.route('/orders')
def orders():
	return render_template('orders.html')


@app.route('/settings')
def settings():
	return render_template('settings.html')


@app.route('/positions')
def positions():
	positions = bot.get_positions()
	return render_template('positions.html')


@app.route('/graph')
def graph():
	positions = bot.get_positions()
	return render_template('graph.html')



@app.route('/plot/<ticker>')
def plot(ticker):

	"""
	encoded = b64encode(img_data)
	mime = "image/jpeg"
	uri = "data:%s;base64,%s" % (mime, encoded)
	"""
	values = bot.get_barset(ticker)[ticker]["open"].tolist()
	return render_template('plot.html',
		values=values,
		ticker=ticker
		)

if __name__ == "__main__":
	app.run(debug=True)