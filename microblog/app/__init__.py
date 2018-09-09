from flask import Flask

app = Flask(__name__)

from app import routes

"""
Сценарий создает объект приложения как экземпляр класса Flask, импортированного из пакета flask.
Переменная __name__, переданная в класс Flask, является предопределенной переменной Python, которая задается именем модуля, в котором она используется.
Flask использует расположение модуля, переданного здесь как отправную точку, когда ему необходимо загрузить связанные ресурсы, такие как файлы шаблонов.
"""
