from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticsearch import Elasticsearch
import logging
#logging
toto_logger = logging.getLogger("toto")
toto_logger.setLevel(logging.DEBUG);
console_handler = logging.StreamHandler()
toto_logger.addHandler(console_handler)
#init objects
db = SQLAlchemy()
migrate = Migrate()

#create instance of app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
if app.config['ELASTICSEARCH_URL'] else None

from app import views, models