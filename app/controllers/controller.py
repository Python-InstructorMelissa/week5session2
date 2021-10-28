from app import app
from flask import Flask, render_template, redirect, session, request
from app.models.course import Course

# ----------- Main landing page
@app.route('/')
def index():
    return render_template('index.html', allCourses = Course.getAll())

# -------- Add Course Landing Page
@app.route('/addCourse')

# ---------- Hidden create course route (only used to just process a function)
@app.route('/createCourse', methods=['POST'])
def createCourse():
    data = {
        "courseName": request.form['courseName'],
        "courseDesc": request.form['courseDesc']
    }
    print(request.form)
    Course.save(data)
    return redirect('/')

# --------- Single course Landing page for updating
@app.route('/course/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template("updateCourse.html", course=Course.getOne(data))

# --------- Hidden update course route
@app.route('/course/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id,
        "courseName": request.form['courseName'],
        "courseDesc": request.form['courseDesc']
    }
    Course.update(data)
    return redirect('/')

# ------------ Hidden delete route (only used to just process a function)
@app.route('/course/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Course.delete(data)
    return redirect('/')
