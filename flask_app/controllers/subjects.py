from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.subject import Subject

@app.route('/')
def index():
    return redirect('/subjects/')

@app.route('/subjects/')
def subjects():
    # knowing that I am going to display a table of all the subjects created on the html I call it subjects plural to remind myself multiple entries returned
    print("all subjects from controller file: ", Subject.getAll())
    return render_template('subjects.html', subjects=Subject.getAll())
