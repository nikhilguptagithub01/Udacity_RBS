from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:default123@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class news(db.Model):
    __tablename__ = 'news' #if this is not given then by ddefault class name (in lowercase) will be used for naming table
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)


    def __repr__(self):
        return f'<news id: {self.id}, description: {self.description} >'

db.create_all()

@app.route('/') #listen to homepage
def indexquery(): #route handler
    return render_template('index.html', data = news.query.all())
