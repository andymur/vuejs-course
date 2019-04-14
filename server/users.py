# -*- coding: utf-8 -*-
import json
from flask import request, Response
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
#to avoid CORS
CORS(app, resources={r"*": {"origins": "*"}})


matt = {'id': 2, 'firstName': 'Matthew', 'secondName': 'Kinsky', 'patronymic': 'James', 'avatarLink': None}
lena = {'id': 3, 'firstName': 'Lena', 'secondName': 'Kovacs', 'patronymic': 'Maria', 'avatarLink': None}
roger = {'id': 4, 'firstName': 'Roger', 'secondName': 'Trump', 'patronymic': 'Edward', 'avatarLink': None}
andy = {'id': 5, 'firstName': 'Andy', 'secondName': 'Mur', 'patronymic': 'Alex', 'avatarLink': 'https://pp.userapi.com/c630324/v630324139/28f44/O2t_HP_TVks.jpg?ava=1'}
donald = {'id': 1, 'firstName': 'Donald', 'secondName': 'McDonald', 'patronymic': 'O\' Hara', 'avatarLink': None}

users = [donald, matt, lena, roger, andy]

@app.route('/users/')
def users_list():
    content = users 
    response = Response(response=json.dumps(content), status=200, mimetype='application/json')
    return response

@app.route('/user/<userId>')
def user_data(userId):
    content = donald
    response = Response(response=json.dumps(content), status=200, mimetype='application/json')
    return response

