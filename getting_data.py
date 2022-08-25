"""
Чтобы получить данные из бд, вызываем методы у объекта класса:
    rsult = User.query.<method>()
    User.query.all() - возвращает результат запроса (объект Query) в виде списка
    User.query.count() - возвращает общее количество записей в запросе
    User.query.first() - возвращает первый результат из запроса или None, если записей нет
    User.query.get(pk) - возвращает объект по первичному ключу (pk) или None, если объект не был найден

Фильтрация выборки данных:
    User.query.filter(*criterion) - возвращает экземпляр Query после применения оператора WHERE
    User.query.limit(limit) - возвращает экземпляр Query после применения оператора LIMIT
    User.query.offset(offset) - возвращает экземпляр Query после применения оператора OFFSET
    User.query.order_by(*criterion) - возвращает экземпляр Query после применения оператора ORDER BY
    User.query.group_by(*criterion) - возвращает экземпляр Query после применения оператора GROUP BY
    User.query.join(*props) - возвращает экземпляр Query после применения оператора SQL INNER JOIN
"""
from adding_data_to_BD import app, db, User, Group
from sqlalchemy import or_, desc, func

"""
Пример с WHERE
SQL -> WHERE name = 'Max'
query = User.query.filter(User.name == 'Max')
"""
query_1 = db.session.query(User).filter(User.name == 'Max1')
"""сформирует SQL запрос в виде объекта класса flask_sqlalchemy.BaseQuery с преподготовленным аргументом условия"""

# print(query_1)
# print(query_1.one())

"""
SQL -> WHERE passport_number IS NULL
"""
query_12 = db.session.query(User).filter(User.passport_number == None)
# print(query_12)
# print(query_12.all())

"""
SQL -> WHERE ... IN
"""
query_13 = db.session.query(User).filter(User.id.in_([1, 2]))
# print(query_13)
# print(query_13.all())

"""
SQL -> WHERE ... NOT IN
"""
query_14 = db.session.query(User).filter(User.id.notin_([1, 2]))
# print(query_14)
# print(query_14.all())

"""
SQL -> WHERE ... BETWEEN
"""
query_15 = db.session.query(User).filter(User.id.between(4, 7))
# print(query_15)
# print(query_15.all())

"""
Пример с WHERE ... AND
"""
query_2 = db.session.query(User).filter(User.id <= 5, User.age > 20)
# print(query_2)
# print(query_2.all())

"""
Пример с WHERE ... OR
"""
query_3 = db.session.query(User).filter(or_(User.id <= 5, User.age > 20))
# print(query_3)
# print(query_3.all())

"""
Пример с LIKE
"""
query_4 = db.session.query(User).filter(User.name.like('L%'))
# print(query_4)
# print(query_4.first().name)

"""
Пример с LIMIT
"""
query_5 = db.session.query(User).limit(2)
# print(query_5)
# print(query_5.all())

"""
Пример с LIMIT OFFSET
"""
query_6 = db.session.query(User).limit(2).offset(2)
# print(query_6)
# print(query_6.all())

"""
Пример с ORDER BY
"""
query_7 = db.session.query(User).order_by(User.age)
query_71 = db.session.query(User).order_by(desc(User.age))
# print(query_71)
# print(query_71.all())

"""
Пример с JOIN
"""
query_8 = db.session.query(User.name, Group.name).join(Group)
# print(query_8)
# print(query_8.all())

"""
SQL -> GROUP BY (scalar)
func -> count(user.id)
"""
query_9 = db.session.query(func.count(User.id)).join(Group).filter(Group.id == 1).group_by(Group.id)
print(query_9)
print(query_9.scalar())
