from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.dp'
dp = SQLAlchemy(app)


class Article(dp.Model):
    id = dp.Column(dp.Integer, primary_key=True)
    title = dp.Column(dp.String(100), nullable=False)
    intro = dp.Column(dp.String(300), nullable=False)
    text = dp.Column(dp.Text, nullable=False)
    date = dp.Column(dp.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article> %r' % self.id

class Data(dp.Model):
    id = dp.Column(dp.Integer, primary_key=True)
    name = dp.Column(dp.String(100), nullable=False)
    email = dp.Column(dp.String(100), nullable=False)
    phone = dp.Column(dp.String(20), nullable=False)
    age = dp.Column(dp.Integer, nullable=False)
    happiness_level = dp.Column(dp.Float, nullable=False)
    has_car = dp.Column(dp.Boolean, nullable=False)


    def __repr__(self):
        return '<Data> %r' % self.id

@app.route('/')
def coomingsoon3():
    return render_template('comingsoon.html')


@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/forus')
def rrk():
    return render_template("base.html")


@app.route('/contact')
def kkt():
    return render_template("contact.html")


@app.route('/blog/<string:news>/<int:id>')
def user(news, id):
    return 'User page' + news + ' - ' + str(id)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            dp.session.add(article)
            dp.session.commit()
            return redirect('/home')
        except:
            return 'error'

    else:
        return render_template('create-article.html')


@app.route('/commit', methods=['POST', 'GET'])
def create_commit():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        happiness_level = request.form['happiness_level']
        has_car = request.form['has_car']
        intro = request.form['intro']
        text = request.form['text']
        date = request.form['date']

        article = Data(name=name, email=email, phone=phone, age=age, happiness_level=happiness_level,
                           has_car=has_car, intro=intro, text=text, date=date)

        try:
            dp.session.add(article)
            dp.session.commit()
            return redirect('/home')
        except:
            return 'error'

    else:
        return render_template('someInfo.html')


@app.route('/create-article2', methods=['POST', 'GET'])
def create_article2():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            dp.session.add(article)
            dp.session.commit()
            return redirect('/home')
        except:
            return 'error'

    else:
        return render_template('Create-article2.html')

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post_detail.html', article=article)


@app.route('/posts/<int:id>/delete')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        dp.session.delete(article)
        dp.session.commit()
        return redirect('/posts')
    except:
        return 'error'


@app.route('/posts/<int:id>/del')
def post_confirm_delete(id):
    article = Article.query.get(id)
    return render_template('confirm.html', article=article)


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def create_article3(id):
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            dp.session.add(article)
            dp.session.commit()
            return redirect('/posts')
        except:
            return 'error'

    else:
        article = Article.query.get(id)
        return render_template('post_update.html', article=article)


@app.route('/tasks')
def task():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('tasks.html', articles=articles)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
