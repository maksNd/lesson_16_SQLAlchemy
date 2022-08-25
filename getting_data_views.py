"""
Чтобы получить данные из бд, вызываем методы у объекта класса:
    rsult = User.query.<method>()
    User.query.all() - возвращает результат запроса (объект Query) в виде списка
    User.query.count() - возвращает общее количество записей в запросе
    User.query.first() - возвращает первый результат из запроса или None, если записей нет
    User.query.get(pk) - возвращает объект по первичному ключу (pk) или None, если объект не был найден
"""

import json
from adding_data_to_BD import User, app


@app.route('/users')
def get_all():
    all_users = User.query.all()
    users_response = []

    for user in all_users:
        users_response.append({'user_id': user.id, 'user_name': user.name, 'user_age': user.age})
    return json.dumps(users_response)


@app.route('/users/count')
def get_users_count():
    users_count = User.query.count()
    return json.dumps(users_count)


@app.route('/users/first')
def get_first_user():
    user = User.query.first()
    return json.dumps({'id': user.id, 'name': user.name, 'age': user.age})


@app.route('/users/<int:pk>')
def get_user_by_pk(pk):
    user_by_pk = User.query.get(pk)
    if user_by_pk is None:
        return 'user not found'

    user = {'id': user_by_pk.id, 'name': user_by_pk.name, 'age': user_by_pk.age}
    return json.dumps(user)


app.run()
