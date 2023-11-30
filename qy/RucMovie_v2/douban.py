from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text as query_text
from sqlalchemy.sql import func
from helpers.echarts import hbar_option
import pandas as pd
import numpy as np
import os


# Create a Blueprint instance
blueprint_douban = Blueprint('douban', __name__)

# Define routes using the Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'douban.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.app_context().push()
db = SQLAlchemy(app)

movies = pd.read_sql('douban_movies', db.engine)
persons = pd.read_sql('persons', db.engine)
associations = pd.read_sql('movie_actor_association', db.engine)

movies['link'] = movies.apply(lambda x: f"""<a href="{x['douban_url']}">{x['douban_rate']}</a>""", axis=1)
movies['release_year'] = movies.release_year.fillna(0).astype(np.int64)
movies['short'] = movies.description.str.replace(r'\n| |\u3000', '', regex=True)
movies['short'] = movies['short'].apply(lambda x: x if len(x)<155 else x[:155]+'...')
movies['country'] = movies.country.str.split('/', expand=True)[0]

movie_actor = {}

for movie_id in associations.movie_id.unique():
    movie_actor[movie_id] = associations.loc[associations.movie_id==movie_id, 'person_id'].values.tolist()[:3]
movie_actor = pd.DataFrame.from_dict(movie_actor, orient='index').stack().droplevel(-1).reset_index()
movie_actor.columns = ['movie_id', 'person_id']

movie_name = movies.set_index('movie_id')['movie_name'].to_dict()
movie_rate = movies.set_index('movie_id')['douban_rate'].to_dict()
rate_count = movies.set_index('movie_id')['rating_count'].to_dict()
person_group = movie_actor.groupby('person_id')['movie_id']
actors = pd.concat([
    person_group.apply(lambda x: [mid for mid in x]),
    person_group.apply(lambda x: [movie_name[mid] for mid in x]),
    person_group.apply(lambda x: [movie_rate[mid] for mid in x]),
    person_group.apply(lambda x: [rate_count[mid] for mid in x]),
    person_group.apply(lambda x: '; '.join([f"{movie_name[mid]}（{movie_rate[mid]})" for mid in x])),
], keys =['movie_id', 'movie_name', 'movie_rate', 'rate_count', 'movies'], 
axis=1).join(persons.set_index('person_id'))
actors['max_rate'] = actors.movie_rate.apply(max)
actors['top_count'] = actors.movie_rate.apply(len)
actors = actors.sort_values(['max_rate', 'top_count'], ascending=False)


@blueprint_douban.route('/')
@blueprint_douban.route('/index')
@blueprint_douban.route('/movies')
def movie_table():
    movies.loc[movies.release_year==0, 'release_year'] = ''
    cols = ['movie_id', 'movie_name', 'release_year', 'movie_type',  'country', 'link', 'short', 'poster']
    vars = dict(data = movies[cols].values.tolist(), ensure_ascii=True)
    return render_template('douban/movie_list.html', vars=vars)

@blueprint_douban.route('/movie_top10')
def movie_top10():
    vars = {}
    data = movies.loc[
        movies.country.str.contains('大陆'), ['movie_name', 'douban_rate']
    ].sort_values('douban_rate', ascending=False)[:10].set_index('movie_name')
    vars['echart_mainland'] = hbar_option("大陆电影高分榜", data.index.tolist(), data['douban_rate'].tolist())
    data = movies.loc[
        movies.country.str.contains('香港|台湾'), ['movie_name', 'douban_rate']
    ].sort_values('douban_rate', ascending=False)[:10].set_index('movie_name')
    vars['echart_hk'] = hbar_option("港台电影高分榜", data.index.tolist(), data['douban_rate'].tolist())

    data = movies.loc[
        ~movies.country.str.contains('大陆|香港|台湾'), ['movie_name', 'douban_rate']
    ].sort_values('douban_rate', ascending=False)[:10].set_index('movie_name')
    vars['echart_oversea'] = hbar_option("国外电影高分榜", data.index.tolist(), data['douban_rate'].tolist())

    return render_template('douban/movie_top10.html', vars=vars)

@blueprint_douban.route('/actors')
def actor_table():
    cols = ['person_name', 'gender', 'birth_date', 'birth_place',  'max_rate', 'top_count', 'movies']
    vars = dict(data = actors[cols].values.tolist(), ensure_ascii=True)
    return render_template('douban/actor_list.html', vars=vars)






