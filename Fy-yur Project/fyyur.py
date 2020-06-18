from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, flash
from flask_sqlalchemy import SQLAlchemy
import sys

from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/fyyur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class venueclass(db.Model):
    __tablename__ = 'venuetable' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    address = db.Column(db.String, nullable=False)
    phn_num=db.Column(db.String, nullable=False)
    genres=db.Column(db.String, nullable=False)
    fblink=db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<venueclass id: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}>'

#db.create_all()
@app.route('/postvenue') #listen to homepage
def get_venue():
    return render_template('postvenue.html')

@app.route('/postvenue', methods=['POST']) #listen to homepage
def post_venue(): #route handler
    error = False
    #body = {}
    try:
        #value1=request.get_json()['id']
        value2=request.get_json()['name']
        value3=request.get_json()['city']
        value4=request.get_json()['state']
        value5=request.get_json()['address']
        value6=request.get_json()['phn_num']
        value7=request.get_json()['genres']
        value8=request.get_json()['fblink']
        

        todovar = venueclass(name=value2, city=value3, state=value4, 
               address=value5, phn_num=value6, genres=value7, fblink=value8)
        db.session.add(todovar)
        db.session.commit()

        #body['id']= todovar.id
        #body['name']= todovar.name
        #body['city']= todovar.city
        #body['state']= todovar.state
        #body['address']= todovar.address
        #body['phn_num']= todovar.phn_num
        #body['genres']= todovar.genres
        #body['fblink']= todovar.fblink
    except:
        error=True
        db.session.rollback()
        print(sys.exec_info())
    
    finally:
       db.session.close()
    
    if not error:
        #form=form
        #return render_template('postvenue.hrml')
        #return jsonify(body)
        flash('Venue ' + request.get_json()['name'] + ' was successfully listed!')
     #   return render_template('indexfyyur.html')
        return redirect(url_for(index))

@app.route('/') #listen to homepage
def index(): #route handler
    #list=venueclass.query.order_by('id').all()
    #print("formtable:", list)
    return render_template('indexfyyur.html')

