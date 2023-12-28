"""Pet adoption agency application"""

from flask import Flask, redirect, render_template, request, flash
from models import connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mac@localhost:5432/adoption_pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'


db = connect_db(app)
db.create_all()

# View functions


@app.route('/')
def pet_list():
    pets = Pet.query.all()
    return render_template("pet-list.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """renders a form to add a pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        # raise
        pet_name = form.pet_name.data
        pet_species = form.pet_species.data
        pet_pic = form.pet_pic.data
        pet_age = form.pet_age.data
        more_info = form.more_info.data
        availablity = form.availability.data

        new_pet = Pet(pet_name=pet_name, pet_species=pet_species, pet_pic=pet_pic, 
                      pet_age=pet_age, more_info=more_info, availablity=availablity)
        db.session.add(new_pet)
        db.session.commit()
     
        return redirect('/')
    else:
        return render_template("add-pet.html", form = form)

@app.route("/<int:pet_id>")
def pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet-info.html", pet=pet)


@app.route("/<int:pet_id>/edit", methods=["GET","POST"])
def info_edit(pet_id):
    """edits the pet information"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        
        pet.pet_name = form.pet_name.data
        pet.pet_species = form.pet_species.data
        pet.pet_pic = form.pet_pic.data
        pet.pet_age = form.pet_age.data
        pet.more_info = form.more_info.data
        pet.availablity = form.is_available.data
        # db.session.add(pet)
        db.session.commit()
        # raise
        return redirect(f"/{pet.pet_id}")
        
    else:
        
        return render_template("edit-pet-info.html", form=form)