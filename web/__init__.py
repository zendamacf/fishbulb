from flask import Flask, jsonify, Response
from web import database

app = Flask(__name__)


@app.route('/ping')
def ping() -> Response:
	return jsonify(ping='pong')


@app.route('/', methods=['GET'])
def home() -> Response:
	resp = database.query(
		"""
		SELECT
			q.category,
			q.content,
			a.name AS author_name
		FROM
			quote q
		LEFT JOIN
			author a ON (a.id = q.authorid)
		ORDER BY RANDOM()
		LIMIT 1
		"""
	)[0]
	return jsonify(**resp)
