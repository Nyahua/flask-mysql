from flask import Flask, render_template
from markupsafe import escape

# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]

from .model import Movie, db
movies = []
for instance in Movie.query.all():
    movie = dict(
        id=instance.movie_id,
        title=instance.movie_name, 
        year=instance.release_year
        )
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

@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = Movie.query.filter_by(movie_id=movie_id)
    print(movie)
    movie = Movie.query.get_or_404(movie_id)

    # if request.method == 'POST':  # 处理编辑表单的提交请求
    #     title = request.form['title']
    #     year = request.form['year']

    #     if not title or not year or len(year) != 4 or len(title) > 60:
    #         flash('Invalid input.')
    #         return redirect(url_for('edit', movie_id=movie_id))  # 重定向回对应的编辑页面

    #     movie.title = title  # 更新标题
    #     movie.year = year  # 更新年份
    #     db.session.commit()  # 提交数据库会话
    #     flash('Item updated.')
    #     return redirect(url_for('index'))  # 重定向回主页

    return render_template('tpl_edit_movie.html', movie=movie)  # 传入被编辑的电影记录