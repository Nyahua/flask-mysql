from flask import Flask, render_template
from markupsafe import escape

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://nyahua:123456@nyahua.com:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.app_context().push()

db = SQLAlchemy(app)

# many to many relation
movie_actor_association = db.Table(
    'movie_actor_association',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie_info.movie_id')),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor_info.actor_id')),
)

class Movie(db.Model):
    __tablename__ = 'movie_info'

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(db.String(20))
    release_date = db.Column(db.String(15))
    country = db.Column(db.String(20))
    movie_type = db.Column(db.String(10))
    release_year = db.Column(db.Integer)
    
    moviebox = db.relationship('MovieBox', back_populates='movies', uselist=False)
    actors = db.relationship('Actor', secondary=movie_actor_association, back_populates='movies')
    
    def __repr__(self):
        return f'<Movie {self.movie_name}>'
    
class Actor(db.Model):
    __tablename__ = 'actor_info'

    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actor_name = db.Column(db.String(20))
    gender = db.Column(db.String(2))
    country = db.Column(db.String(20))
    
    movies = db.relationship('Movie', secondary=movie_actor_association, back_populates='actors')
    
    def __repr__(self):
        return f'<Actor {self.actor_name}>'    
    
# one to one relation
class MovieBox(db.Model):
    __tablename__ = 'movie_box'
    movie_id = db.Column(db.String(10), db.ForeignKey('movie_info.movie_id'), unique=True, nullable=False, primary_key=True)
    movie_box = db.Column(db.Float)
    movies = db.relationship('Movie', back_populates='moviebox')

# move mysql database to local variables 
movies = []
for instance in Movie.query.all():
    movie = dict(title=instance.movie_name, year=instance.release_year)
    movie['actors'] = [actor.actor_name for actor in instance.actors]
    movies += [movie]

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('tpl_index.html', movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return dict(User=escape(name))