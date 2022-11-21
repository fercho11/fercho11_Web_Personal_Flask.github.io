####from crypt import methods
from flask import Flask, render_template, request

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
    projects= [
        {
            'name':'Primer Proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image':'img/home-bg.jpg',
            'url':'http://google.com'
        },
        {
            'name':'Segundo Proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image':'img/about-bg.jpg',
            'url':'http://xataka.com'
        }
    ]
    return render_template('public/portfolio.html', projects=projects)

####### Rutas #########
@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    email = request.form['mail']
    password = request.form['password']
    access = {'email':email, 'password': password}

    return render_template('admin/index.html', user_access=access )

@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)