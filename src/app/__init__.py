from flask import Flask

def create_app():

	app = Flask(__name__)

	# Initialise the database connection
	from app.database import connect_db
	connect_db()

	# Register Blueprint
	from app.views import main_bp
	app.register_blueprint(main_bp)


	return app

