from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class employee(db.Model):
    __tablename__ = 'emp' #if this is not given then by default class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    dept = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<employee id: {self.id}, fname: {self.fname}, lname: {self.lname}, dept: {self.dept} >'

db.create_all()

@app.route('/') #listen to homepage
def indexquery(): #route handler
    list = employee.query.all()
    print("employee list: ", list)
    return render_template('indexquery.html', data = list)
