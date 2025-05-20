from flask import render_template, redirect, request, url_for, flash
# from flask_login import login_required, login_user, logout_user, current_user
# from app import db

from . import auth
# from .models import User
# from .forms import LoginForm
# from .email import send_email

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
		# ~ user = User.query.filter_by(email=email).first()
		# ~ if user:
			# ~ return render_template('auth/email.html')
        # print(request.form.get('email'), file=sys.stderr)
        # print(request.form.get('username'), file=sys.stderr)
        email = request.form.get('email')
        # if User.query.filter_by(email=email).first():
        #     flash('Email adresa je već registrirana.')
        # password = request.form.get('password')
        # remember_me = request.form.get('username')
        # user = User(username=request.form.get('username'),
        #             email=request.form.get('email'))
        # db.session.add(user)
        # db.session.commit()
        # token = user.generate_confirmation_token()
        # send_email(request.form.get('email'),
        #            'Potvrdi svoj korisnički račun',
        #            'auth/email/confirm', user=request.form.get('username'), token=token)
        # flash('Poslana je elektronička pošta za potvrdu elektroničke pošte(email).')
        return redirect(url_for('general.home'))
    return render_template('auth/register.html')

@auth.route('/register/confirm/<token>')
def register_confirm(token):
    # if current_user.confirmed:
    #     return redirect(url_for('general.home'))
    # if current_user.confirm(token):
    #     db.session.commit()
    #     flash('Potvrdili ste svoj korisnički račun. Hvala!')
    # else:
    #     flash('Poveznica za potvrdu je nevažeća ili je prošao rok valjanosti.')
    return redirect(url_for('general.home'))

