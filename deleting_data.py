from adding_data_to_BD import db, User

user = User.query.get(2)
db.session.delete(user)
db.session.commit()

user = User.query.get(2)
print(user is None)

"""
Запросы на удаление по условию
"""
db.session.query(User).filter(User.name == 'Max').delete()
db.session.commit()

user = User.query.filter(User.name == 'Max').all()
print(user)
