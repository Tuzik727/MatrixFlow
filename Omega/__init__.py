import requests

from flask import Flask

from Omega.src.Backend.DAO.Users import UserDAO

app = Flask(__name__)
app.secret_key = '5tmw6m9672'
app.config['SESSION_TYPE'] = 'filesystem'
s = requests.Session()
user = UserDAO()

import Omega.views
import Omega.views2
