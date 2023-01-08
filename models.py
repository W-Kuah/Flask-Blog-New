# This file creates the a SQLAlchemy class definition for the data in the person datbase

from datetime import datetime
from marshmallow_sqlalchemy import fields

from config import db, ma


class Note(db.Model):
    __table_name__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    ## This and the Person.notes attribute are how SQLAlchemy knows what to do when interacting with Person and Note objects.
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    ## The nullable=False parameter indicates that new notes must contain content.
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        ## Set include_fk to True. 
        ## Otherwise Marshmallow wouldn’t recognize person_id during the serialization process
        include_fk = True

##  Inheriting from db.Model gives Person the SQLAlchemy features to connect to the database and access its tables.
class Person(db.Model):
    ## Connects the class definition to the person database table
    __tablename__ = "person"
    ## Declares the id column containing an integer acting as the primary key for the table.
    id = db.Column(db.Integer, primary_key=True)
    ## Defines the last name field with a string value. 
    ## This field must be unique because the lname is being used as the identifier for a person in a REST API URL.
    lname = db.Column(db.String(32), unique=True)
    ## Defines the first name field with a string value.
    fname = db.Column(db.String(32))
    ## define a timestamp field with a datetime value
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    ## create a new attribute called notes and set it equal to an instance of an object.
    ## This object creates the relationship.
    notes = db.relationship(
        ## This parameter defines the SQLAlchemy class that the Person class will be related to
        Note,
        ## This parameter creates a backward reference,
        ## each instance of Note will contain an attribute called .person.
        ## The .person attribute references the parent object that a particular Note instance is associated with.
        backref="person",
        ## This parameter determines how to treat Note instances when changes are made to the parent Person instance.
        ## https://docs.sqlalchemy.org/en/20/orm/cascades.html#delete
        cascade="all, delete, delete-orphan",
        ## Prevent a Note without a parent Person object to exist
        single_parent=True,
        order_by="desc(Note.timestamp)"
    )

## The PersonSchema class defines how the attributes of a class will be converted into JSON-friendly formats.
## Marshmallow makes sure that all attributes are present and contain the expected data type 
class PersonSchema(ma.SQLAlchemyAutoSchema):
    ## To find a SQLAlchemy model and a SQLALchemy session, 
    ## SQLAlchemyAutoSchema looks for and then uses this internal Meta class.
    class Meta:
        ## For PersonSchema, the model is Person, 
        ## and sqla_session is db.session.
        model = Person
        ## load_instance deserializes JSON data and loads Person model instances from it
        load_instance = True
        sqla_session = db.session
        ## Marshmallow now adds any related objects to the person schema
        include_relationships = True
    
    ## Marshmallow doesn’t receive all the information it needs to work with the Notes data,
    ## therefore the notes field in PersonSchema have to be explicitly created.
    notes = fields.Nested(NoteSchema, many=True)

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
note_schema = NoteSchema()