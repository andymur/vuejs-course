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

users_hash = {1: donald, 2: matt, 3: lena, 4: roger, 5: andy}

google = {'id': 1, 'url': 'http://google.com', 'tags': ['search']}
jsru = {'id': 2, 'url': 'http://javascript.ru', 'category': 'Applied', 'tags': ['js']}

links = [google, jsru]
links_hash = {1: google, 2: jsru}

@app.route('/link/<int:linkId>')
def link_data(linkId):
    link = links_hash.get(linkId)
    if link is None:
        raise Exception('Link not found!')
    response = Response(response=json.dumps(link), status=200, mimetype='application/json')
    return response
 
@app.route('/links/')
def links_list():
    content = links  
    response = Response(response=json.dumps(content), status=200, mimetype='application/json')
    return response

@app.route('/users/')
def users_list():
    content =  users  
    response = Response(response=json.dumps(content), status=200, mimetype='application/json')
    return response

@app.route('/user/<int:userId>')
def user_data(userId):
    user = users_hash.get(userId)
    if user is None:
        raise Exception('User not found!')
    response = Response(response=json.dumps(user), status=200, mimetype='application/json')
    return response

@app.route('/useredit/<int:userId>', methods=['PATCH'])
def user_edit(userId):
    user = users_hash.get(userId)
    newUser = request.json

    if user is None:
        userId = max(users_hash.keys()) + 1

    newUser['id'] = userId

    users_hash[userId] = newUser
    response = Response(response=json.dumps(newUser), status=200, mimetype='application/json')
    return response
