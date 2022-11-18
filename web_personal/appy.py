from flask import Flask, render_template

app = Flask(__name__)


####### Rutas Public ######
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('public/portfolio.html')

####### Rutas #########
@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

if __name__ == '__main__':
    app.run(debug=True)