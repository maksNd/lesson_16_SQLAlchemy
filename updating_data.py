from adding_data_to_BD import db, User

user = User.query.get(2)
print(user.name)

user.name = 'New name'
db.session.add(user)
db.session.commit()

user = User.query.get(2)
print(user.name)