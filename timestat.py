#from app import app, db
#from app.models import Hour


#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'Hour': Hour}
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restless import APIManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models

migrate = Migrate(app, db)
manager = APIManager(app, flask_sqlalchemy_db=db)
from app import routes
