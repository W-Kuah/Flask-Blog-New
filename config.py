# Configuration of...
## Flask, 
## Connexion, 
## SQLAlchemy (https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/), 
## and Marshmallow

import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
# Create the connexion app instance and give it the path to the directory that contains your specification file.
connex_app = connexion.App(__name__, specification_dir=basedir)

# Creates a variable, 
# which is the Flask instance initialized by Connexion.
app = connex_app.app
# Set SQLite as the database and a file named people.db in the current directory as the database file for SQLAlchemy.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Pass the app configuration information to SQLAlchemy and assign it to a variable
db = SQLAlchemy(app)
# Initializes Marshmallow and allows it to work with the SQLAlchemy components attached to the app.
ma = Marshmallow(app)



