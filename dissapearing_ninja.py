
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	print 'index.html rendered go ninja'
	return render_template('index.html')

@app.route('/ninja')
def tmnt_all():
	print 'page with all ninjas'
	return render_template('tmnt_all.html')

@app.route('/ninja/<fav_color>')
def fav_color(fav_color):
	print 'fav_color'
	if fav_color == 'blue':
		return render_template('leo.html')
	elif fav_color == 'orange':
		return render_template('mike.html')
	elif fav_color == 'red':
		return render_template('raph.html')
	elif fav_color == 'purple':
		return render_template('don.html')
	else:
		return render_template('april.html')


app.run(debug=True) 