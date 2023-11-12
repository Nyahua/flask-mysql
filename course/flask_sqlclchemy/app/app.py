from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.app_context().push()

db = SQLAlchemy(app)



class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)

def select_to_dataframe(query):
    with db.engine.connect() as connection:
        result = connection.execute(query)
    return pd.DataFrame(result)


# Delete tables if exsits
with db.engine.connect() as conn:
    query = text("""
    DROP TABLE IF EXISTS movies;
    """)
    conn.execute(query)
with app.app_context():
    db.create_all()
    
if __name__ == "__main__":

    # add movie data to database
    import pandas as pd
    import json

    with open('datasets/top-rated-movies.json', 'r') as file:
        movie_data = json.load(file)
        
    df_movie = pd.DataFrame(movie_data)
    df_movie.loc[df_movie.originalTitle=='', 'originalTitle'] = df_movie.title
        
    for idx, row in df_movie.iterrows():
        movie = Movie(title=row['originalTitle'], year=row['year'])
        db.session.add(movie)
        
    db.session.commit()

    query = text("SELECT COUNT(*) FROM movies;")
    print(f'{select_to_dataframe(query)} rows added.')

