from app import db, Data, Car
3

@app.before_first_request
def create_tables():
    db.create_all()

person1 = Data(name='Waqas Arqum' email='waqy_arqum@hotmail.co.uk')
db.session.add(person1)
db.session.commit()

car1 = Car(reg="12345", databr_id=person1)
db.session.add(car1)
db.session.commit()
car2 = Car(reg="123456", databr_id=person1)
db.session.add(car2)
db.session.commit()

print(person1.car)

print(car1.databr.name + ', ' + car1.databr.email)