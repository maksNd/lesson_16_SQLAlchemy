from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

"""relationship - позволяет погружать связь в виде объектов"""

from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

"""

Валидная модель ОRМ:
    1. Нужно наследоваться от базового класса db.Model
    2. Нужно объявить имя таблицы с помощью атрибута __tablename__
    3. Должна быть как минимум одна колонка, которая является частью первичного ключа

Чтобы добавить данные в бд:
    * создать объект пользователя
    * добавить его в сессию
    * выполнить комит (commit - применяет изменения, которые были сделаны с помощью объекта db)
"""


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    passport_number = Column(String, unique=True)  # это значение должно быть уникально
    name = Column(String(100), nullable=False)  # это поле должно быть заполнено
    age = Column(Integer, CheckConstraint('age > 18'))  # ограничение по условию
    group_id = Column(Integer, ForeignKey('group.id'))
    """Строчка ниже делает тоже самое что и строчка выше, только важен порядок создания классов таблиц"""
    # group_id = Column(Integer, ForeignKey(Group.id))

    group = relationship('Group')


class Group(db.Model):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    users = relationship('User')


db.drop_all()  # удаляет все данные из БД
db.create_all()

group_01 = Group(id=1, name='Group #1')
group_02 = Group(id=2, name='Group #2')

user_01 = User(id=1, name='John', age=25, group=group_01)  # * создать объект пользователя
user_02 = User(id=2, name='Kate', age=20, group=group_02)
user_03 = User(id=3, name='Artur', age=23, group=group_01)
user_04 = User(id=4, name='Max', age=33, group=group_01)
user_05 = User(id=5, name='Lily', age=19, group=group_02)
user_06 = User(id=6, name='Mary', age=26, group=group_02)
users = [user_06, user_05, user_04, user_03, user_02, user_01]

with db.session.begin():  # мы не добаляем группы, т.к. алхимия добавит их автоматически с помощью relationship
    db.session.add_all(users)
    # db.session.add_all([group_02, group_01])

# print(User.query.all())
"""
Сессия - активное соединение между программой и базой данных
Может быть большое количество паралельных сессий от разных пользователей
"""
# if __name__ == '__main__':
#     app.run()
