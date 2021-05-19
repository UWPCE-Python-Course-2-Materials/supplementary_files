from datetime import date
import os
from peewee import *

os.remove("people.db")

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


def create_tables(database):
    database.create_tables([Person, Pet])


def add_data():
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save()  # bob is now stored in the database

    # alt
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    grandma.save()
    herb.save()
    return uncle_bob, grandma, herb


def update_data(grandma):
    grandma.name = 'Grandma L.'
    grandma.save()  # Update grandma's name in the database.


def set_pet_owners():
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(
        owner=herb, name='Mittens Jr', animal_type='cat')
    return bob_kitty, herb_fido, herb_mittens, herb_mittens_jr


def delete_pet(herb_mittens):

    herb_mittens.delete_instance()


def show_someones_pets():
    # 1
    Person.get(Person.name == 'Grandma L.')

    for person in Person.select():
        print(person.name)

    # 2
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))

    for pet in query:
        print(pet.name, pet.owner.name)

    # 3
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
        print(pet.name)


if __name__ == "__main__":
    db.connect()
    create_tables(db)
    uncle_bob, grandma, herb = add_data()
    update_data(grandma)
    bob_kitty, herb_fido, herb_mittens, herb_mittens_jr = set_pet_owners()
    delete_pet(herb_mittens)
    show_someones_pets()
    db.close()
