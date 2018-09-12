from flask import Flask

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import routes, models

"""
Сценарий создает объект приложения как экземпляр класса Flask, импортированного из пакета flask.
Переменная __name__, переданная в класс Flask, является предопределенной переменной Python, которая задается именем модуля, в котором она используется.
Flask использует расположение модуля, переданного здесь как отправную точку, когда ему необходимо загрузить связанные ресурсы, такие как файлы шаблонов.
"""
