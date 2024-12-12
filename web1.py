from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return "<h1>Welcome to My Website</h1><p>This is the homepage.</p>"

# Define the about page route
@app.route('/about')
def about():
    return "<h1>About Me</h1><p>This page contains information about me.</p>"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
