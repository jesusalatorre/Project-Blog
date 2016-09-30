from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required
from werkzeug.security import generate_password_hash, check_password_hash

class loginform(Form):
	username=StringField('username', validators=[Required()])
	password=PasswordField('password', validators=[Required()])
	submit=SubmitField('login')
		

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I need a better example'

@app.route('/')
def index():
	return render_template('login.html', form=loginform())

@app.route('/dash')
def dash():
	return render_template('dashboard.html')

@app.route('/register')
def register():
	return render_template('register.html')



if __name__=='__main__':
	app.run(debug=True)