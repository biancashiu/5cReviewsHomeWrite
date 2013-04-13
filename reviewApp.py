from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for
)
import urllib
import requests
import json
from mongokit import Connection, Document, ObjectId
import datetime

app = Flask(__name__)

connection = Connection('localhost', 27017)
class Entry(Document):
    structure = {
        'course_name': basestring,
        'prof_name': basestring,
        'overall': bool,
        'time_spent': basestring
    }

    use_dot_notation = True

connection.register([Entry])
collection = connection['reviews'].entries

@app.route('/')
def index():
    entries = list(collection.Entry.find())
    return render_template('index.html', entries = entries)

@app.route('/write')
def write():
    return render_template('enterReviews.html')

@app.route('/save', methods=['POST'])
def save():
    new_entry = collection.Entry()
    new_entry.course_name = request.form['course_name']
    new_entry.prof_name = request.form['prof_name']
    new_entry.time_spent = request.form['time_spent']
    new_entry.overall = request.form['overall']
    new_entry.q1 = request.form['q1']
    new_entry.q2 = request.form['q2']
    new_entry.q3 = request.form['q3']
    new_entry.q4 = request.form['q4']
    new_entry.q5 = request.form['q5']
    new_entry.q6 = request.form['q6']
    new_entry.comments = request.form['comments']

    new_entry.save()
   
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
