from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)
    app.app_context().push()
    return db

# Model class Pet


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer, autoincrement=True,
                       primary_key=True)

    pet_name = db.Column(db.Text, nullable=False)

    pet_species = db.Column(db.Text, nullable=False)

    pet_pic = db.Column(db.String, nullable=True)

    pet_age = db.Column(db.Integer, nullable=True)

    more_info = db.Column(db.Text, nullable=True)

    is_available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return (f"< Pet obj {self.pet_id}: {self.pet_name} the {self.pet_species}>")
