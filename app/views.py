from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = dict(nickname='Cycu')
    street = dict(name='Cwiartki', number='3/4')
    posts = [
        dict(author=dict(nickname='Arnold Boczek'), body='Wakacje z podrobami'),
        dict(author=dict(nickname='Jolaska'), body='100 twarzy Jolaski')
    ]
    return render_template('index.html', user=user, street=street, posts=posts)
    # return "Co jest kurde, noc jest kurde!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID=%s, remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', form=form)
