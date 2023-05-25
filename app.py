from flask import Flask,request,redirect,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/acerca')
def acerca():
    return render_template('about.html')

@app.route('/libros')
def libros():
    return render_template('books.html')

@app.route('/tienda')
def store():
    return render_template('store.html')

@app.route('/redes-y-contactos')
def socials_and_contact():
    return render_template('contact.html')
