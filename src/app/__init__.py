from flask import Flask
from app.views import main_bp
from app.database import init_db


def create_app():

	app = Flask(__name__)
	# Register Blueprint
	app.register_blueprint(main_bp)

	# Initialise the database
	init_db()

	return app

