from flask import Flask, render_template

web2 = Flask(__name__)

web2.static_folder = 'static'

@web2.route('/')
def home():
    return render_template('home.html')

@web2.route('/about')
def about():
    return render_template('about.html')

@web2.route('/player')
def player():
    return render_template('index.html')


if __name__ == '__main__':
    web2.run(debug=True)