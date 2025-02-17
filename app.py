from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", employees=None)

@app.route("/add_employee", methods=["POST"])
def add_employee():
    employee_id = request.form.get("employee_id")
    name = request.form.get("name")
    department = request.form.get("department")
    new_employee = Employee(employee_id=employee_id, name=name, department=department)
    db.session.add(new_employee)
    db.session.commit()
    flash("Employee added successfully!")
    return redirect(url_for("index"))

@app.route("/display_employees", methods=["GET"])
def display_employees():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

if _name_ == "_main_":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)