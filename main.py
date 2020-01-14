from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getIndex():
  return render_template ('layout.html')

@app.route('/home')
def getHome():
  return "<h1 align ='center'> HEOO </h1>"

@app.route('/about')
def getAbout():
  return "<h1 align ='center'> Chaw </h1>"

@app.route('/about.html')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "123")
app.run(host = '0.0.0.0', port = 8020)

if _name_ == '_main_':
  app.run(threaded=True, port=5050, debug = True)