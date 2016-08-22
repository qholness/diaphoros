from flask import Flask
# from app import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

bootstrap = Bootstrap(app)

# app.config.from_object(config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['NO_BACKSLASH_ESCAPES'] = True

# db = SQLAlchemy(app, 
# 	session_options={
# 		'expire_on_commit' : False,
# 	})

# db.create_all()

from app import views