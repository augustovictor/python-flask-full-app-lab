from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# To generate the secret:
# Go to terminal then type python
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY']= '5672e054298dfbb66457ad5ce64819f8'

posts = [
    {
        'author': 'Victor August',
        'title': 'The first blog post',
        'content': 'This is the content of the first blog post',
        'date_posted': 'June, 03, 2018'
    },
    {
        'author': 'Kikita Costa',
        'title': 'The second blog post',
        'content': 'This is the content of the second blog post',
        'date_posted': 'June, 05, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Homepage', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign up', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(port=3000, debug=True)