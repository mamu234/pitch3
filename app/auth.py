from crypt import methods
from unicodedata import category
from xmlrpc.client import boolean
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('passwaord1')
        password2 = request.form.get('passwaord2')

        if len(email) < 4:
          flash('Email needs to have more than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('passwords dont\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must eb at least 7 characters', category='error') 
        else:
          flash('account created', category='success')




    return render_template("sign_up.html")