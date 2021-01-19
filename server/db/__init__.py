from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
	app.logger.info("Initializing MongoDB")
	db.init_app(app)