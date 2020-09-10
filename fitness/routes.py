from flask import render_template, url_for, flash, redirect
from fitness import app
from fitness.forms import RegistrationForm, LoginForm
from fitness.models import User, Post

posts = [
    {
        'author': 'Kevin',
        'title': 'workout',
        'content': 'exercise',
        'date_posted': 'today'
    },
    {
        'author': 'Kevin',
        'title': 'workout2',
        'content': 'exercise3',
        'date_posted': 'today'
    }
]


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', posts=posts)

@app.route('/build')
def build():
    return render_template('build.html', title = 'Build')

@app.route('/premade')
def premade():
    return render_template('premade.html', title = 'Premade Workouts')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)

