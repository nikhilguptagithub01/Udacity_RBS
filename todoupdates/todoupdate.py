from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class todoupd(db.Model):
    __tablename__ = 'todouptb' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    dept = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default = False)

    def __repr__(self):
        return f'<todouptb id: {self.id}, fname: {self.fname}, lname: {self.lname}, dept: {self.dept}>'

#db.create_all()

@app.route('/todoupdate/create', methods=['POST']) #listen to homepage
def create_todo(): #route handler
    error = False
    body = {}
    try:
        value1=request.get_json()['id']
        value2=request.get_json()['fname']
        value3=request.get_json()['lname']
        value4=request.get_json()['dept']

        todoupdtbvar = todoupd(id=value1, fname=value2, lname=value3, dept=value4)
        db.session.add(todoupdtbvar)
        db.session.commit()
        body['id']= todoupdtbvar.id
        body['fname']= todoupdtbvar.fname
        body['lname']= todoupdtbvar.lname
        body['dept']= todoupdtbvar.dept
    except:
        error=True
        db.session.rollback()
        print(sys.exec_info())
    
    finally:
        db.session.close()
    
    if not error:
        return jsonify(body)

@app.route('/todoupdate/<todo_id>/set-completed', methods=['POST']) #listen to homepage
def set_completed_todo(todo_id): #route handler
    error = False
    body = {}
    try:
        value1=request.get_json()['completed']
        
        todoupdtbvar = todoupd.query.get(todo_id)
        todoupdtbvar.completed=value1
        #db.session.add(todoupdtbvar)
        db.session.commit()
        
    except:
        error=True
        db.session.rollback()
        print(sys.exec_info())
    
    finally:
        db.session.close()
    
    return redirect(url_for('indexupdate'))
    
    #if not error:
    #    return jsonify(body)


@app.route('/') #listen to homepage
def indexupdate(): #route handler
    list=todoupd.query.order_by('id').all()
    print("formtable:", list)
    return render_template('indexupdate.html', data = list)

