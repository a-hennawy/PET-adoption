
from models import db, Pet
from app import app

db.drop_all()
db.create_all()

default_cat_pic = "https://www.freeiconspng.com/uploads/3d-cat-animal-png-3.png"
default_dog_pic = "https://www.freeiconspng.com/uploads/dog-3d-animal-png-12.png"


luca = Pet(pet_name='Luca', pet_species='cat',
           pet_age=3, pet_pic=default_cat_pic)

jouly = Pet(pet_name='Jouly', pet_species='dog',
            pet_age=7, pet_pic=default_dog_pic)

db.session.add_all([luca, jouly])
db.session.commit()
