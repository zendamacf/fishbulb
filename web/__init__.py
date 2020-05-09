# Third party imports
from flask import Flask, jsonify, Response, got_request_exception, request
import rollbar
import rollbar.contrib.flask

# Local imports
from web import config, database

app = Flask(__name__)


@app.before_first_request
def init_rollbar():
	if not hasattr(config, 'TESTMODE'):
		env = 'production'
		if request.remote_addr == '127.0.0.1':
			env = 'development'
		rollbar.init(
			config.ROLLBAR_TOKEN,
			environment=env
		)

		# send exceptions from `app` to rollbar, using flask's signal system.
		got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


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
