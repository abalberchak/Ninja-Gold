from flask import Flask, render_template, request, redirect, session, Markup
app = Flask(__name__)
app.secret_key = 'SECRET'
import random


	# def initialize():
	# session['target'] = random.randrange(0, 101)
	# #print session['session['target']']
	#  return session['target']


@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'log' in session:
		session['log'] = ''
	# data = {}
	# data['gold'] = session['gold']
	# data['log'] = session['log']

	session['farm'] = random.randrange(10, 21)
	print session['farm']
	session['cave'] = random.randrange(5, 11)
	print session['cave']
	session['house'] = random.randrange(2, 6)
	print session['house']
	session['casino'] = random.randrange(-50, 51)
	print session['casino']


	return render_template("index.html", gold=session['gold'], log=session['log'])
 	

@app.route('/process_money', methods=['POST'])
def SubmitNumber():
	

	if request.form['bldg'] == 'farm':
		session['gold'] += session['farm']
		message = "<div class='won'> You went to the farm and earned " + str(session['farm']) + " gold!</div>"
	elif request.form['bldg'] == 'cave':
		session['gold'] += session['cave']
		message = "<div class='won'> You went to the cave and earned " + str(session['cave']) + " gold!</div>"
	elif request.form['bldg'] == 'house':
		session['gold'] += session['house']
		message = "<div class='won'> You went to the house and earned " + str(session['house']) + " gold!</div>"
	elif request.form['bldg'] == 'casino':
		session['gold'] += session['casino']
		if session['casino'] > 0:
			message = "<div class='won'> You went to the casino and earned " + str(session['casino']) + " gold!</div>"
		else:
			message = "<div class='lost'> You went to the casino and lost " + str(session['casino']) + " gold!</div>"
	

	log = session['log']
	session['log'] = message + log


	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['gold'] = 0
	session['log'] = ''
	return redirect('/')


app.run(debug=True) 