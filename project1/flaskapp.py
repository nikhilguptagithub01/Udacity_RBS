from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/udacity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class person(db.Model):
    __tablename__ = 'person' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    dept = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<person id: {self.id}, name: {self.fname}>'

db.create_all()

@app.route('/')
def index():
    result = person.query.first()
    return 'Hello '+ result.fname + '...!!'