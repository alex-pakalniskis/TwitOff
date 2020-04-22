from flask import Flask
from web_app.models import db, migrate
from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.tweet_routes import tweet_routes

DATABASE_URI = "sqlite:///TwitOff.db" # TODO: read from env var
SECRET_KEY = "super secret" # TODO: read from env var

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    # configure the database:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # suppress warning messages
    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(admin_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

