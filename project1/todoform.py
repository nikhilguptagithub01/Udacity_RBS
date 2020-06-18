from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class formtable(db.Model):
    __tablename__ = 'formtb' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    dept = db.Column(db.String(), nullable=False)



    def __repr__(self):
        return f'<formtb id: {self.id}, fname: {self.fname}, lname: {self.lname}, dept: {self.dept}>'

db.create_all()

@app.route('/todoform/create', methods=['POST']) #listen to homepage
def create_todo(): #route handler
    value1=request.form.get('id','')
    value2=request.form.get('fname','')
    value3=request.form.get('lname','')
    value4=request.form.get('dept','')

    formtablevariable = formtable(id=value1, fname=value2, lname=value3, dept=value4)
    db.session.add(formtablevariable)
    db.session.commit()

    return redirect(url_for('indexform'))

@app.route('/') #listen to homepage
def indexform(): #route handler
    list=formtable.query.all()
    print("formtable:", list)
    return render_template('indexform.html', data = list)