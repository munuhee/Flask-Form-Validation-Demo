# Import necessary modules
from flask import Flask, render_template

# Import the MyForm class from the forms module within the app package
from app.forms import MyForm

# Create a Flask application instance
app = Flask(__name__)

# Set the secret key for the application to enable CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key'

# Import routes from the app package
from app import routes
