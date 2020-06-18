from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class ajaxtable(db.Model):
    __tablename__ = 'ajaxtb' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    dept = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<ajaxtb id: {self.id}, fname: {self.fname}, lname: {self.lname}, dept: {self.dept}>'

#db.create_all()

@app.route('/todoajax/create', methods=['POST']) #listen to homepage
def create_todo(): #route handler
    error = False
    body = {}
    try:
        value1=request.get_json()['id']
        value2=request.get_json()['fname']
        value3=request.get_json()['lname']
        value4=request.get_json()['dept']

        ajaxtablevariable = ajaxtable(id=value1, fname=value2, lname=value3, dept=value4)
        db.session.add(ajaxtablevariable)
        db.session.commit()
        body['id']= ajaxtablevariable.id
        body['fname']= ajaxtablevariable.fname
        body['lname']= ajaxtablevariable.lname
        body['dept']= ajaxtablevariable.dept
    except:
        error=True
        db.session.rollback()
        print(sys.exec_info())
    
    finally:
        db.session.close()
    
    if not error:
        return jsonify(body)


@app.route('/') #listen to homepage
def indexajax(): #route handler
    list=ajaxtable.query.all()
    print("formtable:", list)
    return render_template('indexajax.html', data = list)