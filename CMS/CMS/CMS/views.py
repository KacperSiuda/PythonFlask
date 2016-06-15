"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CMS import app

@app.route('/')
def home():
  return render_template('Index.html')
