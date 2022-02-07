import imp
from m2m import app,db
from m2m.models import Class, Student
from flask import render_template, flash, redirect, request, url_for

@app.route("/")
def index():
    return render_template("index.html",title ="Home Page")
@app.route("/student")
def student():
    students = Student.query.all()
    return render_template("student.html", title = "Student Page", students = students)

@app.route("/add_student", methods = ["POST", "GET"])
def add_student():
    if request.method == "POST":
        std_name = request.form["name"]
        s = Student(name=std_name)
        db.session.add(s)
        db.session.commit()
        
    return redirect(url_for("student"))
@app.route("/edit_student<int:id>", methods=["POST", "GET"])
def edit_student(id):
    students = Student.query.all()
    student = Student.query.filter_by(id = id).first()
    if request.method == "POST":
        student.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("student"))
        
    return render_template("student.html", title="Edit Student", students = students,student = student)


@app.route("/detail_student: <int:id>")
def detail_student(id):
    student = Student.query.filter_by(id= id).first()
    classe = student.classes.all()
    print(classe)
    return render_template("detail_student.html", title="Detail Student", student = student, classe = classe)



@app.route("/class")
def classes():
    classes = Class.query.all()
    
    return render_template("class.html", title = "Class Page", classes = classes)

@app.route("/add_class", methods=["POST", "GET"])
def add_class():
    if request.method == "POST":
        class_name = request.form["name"]
        classes = Class(name=class_name)
        db.session.add(classes)
        db.session.commit()        
    return redirect(url_for("classes"))

@app.route("/edit_class:<int:id>", methods=["POST", "GET"])
def edit_class(id):
    
    classes = Class.query.all()
    classe = Class.query.filter_by(id = id).first()
    if request.method == "POST":
        classe.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("classes"))
        
    return render_template("class.html", title="Edit Class", classes = classes,classe = classe)

@app.route("/rigistration", methods=["POST", "GET"])
def rigistration():
    students = Student.query.all()
    classess = Class.query.all()
    if request.method == "POST":
        std_name= request.form["std_name"]
        class_name = request.form["class_name"]
        std = Student.query.filter_by(name=std_name).first()
        c = Class.query.filter_by(name=class_name).first()
        print(std_name)
        print(class_name)

        std.classes.append(c)
        db.session.add(std)
        db.session.commit()
        return redirect(url_for("rigistration"))
    
    return render_template("rigistration.html", title="Rigistration", students = students, classes = classess)   
@app.route("/detail_class: <int:id>")
def detail_class(id):
    classe = Class.query.filter_by(id= id).first()
    print(classe)
    student = classe.students.all()
   
    return render_template("detail_class.html", title="Detail Student", classe = classe, students = student)

