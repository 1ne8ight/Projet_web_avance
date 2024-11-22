from flask import Flask

from flask_mysqldb import MySQL
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

from application import routes
 