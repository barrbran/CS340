from flask import Flask, render_template, json
from flask import request, redirect
import os
import database.db_connector as db

db_connection = db.connect_to_database()


# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/browse_doctor')
def doctor():
    query = "SELECT id, fname, lname, phoneNumber, salary, nurseID FROM doctor;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_doctor.j2", doctors=result)

@app.route('/add_new_doctor', methods=['POST','GET'])
def add_new_doctor():
    if request.method == 'GET':
        query = 'SELECT id, fname, lname FROM nurse;'
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('doctor_add_new.j2', nurses=result)
    elif request.method == 'POST':
        print("Add new doctor")
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']
        nurseID = request.form['nurseID']

        query = 'INSERT INTO doctor (fname, lname, phoneNumber, salary, nurseID) VALUES (%s,%s,%s,%s,%s);'
        data = (fname, lname, phoneNumber, salary, nurseID)
        db.execute_query(db_connection, query, data)

        query = "SELECT id, fname, lname, phoneNumber, salary, nurseID FROM doctor;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_doctor.j2", doctors=result, resultText = "Doctor added.")

@app.route('/browse_nurse')
def nurse():
    query = "SELECT id, fname, lname, phoneNumber, salary FROM nurse;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_nurse.j2", nurses=result)

@app.route('/add_new_nurse', methods=['POST','GET'])
def add_new_nurse():
    if request.method == 'GET':
        return render_template('nurse_add_new.j2')
    elif request.method == 'POST':
        print("Add new nurse")
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']

        query = 'INSERT INTO nurse (fname, lname, phoneNumber, salary) VALUES (%s,%s,%s,%s);'
        data = (fname, lname, phoneNumber, salary)
        db.execute_query(db_connection, query, data)

        query = "SELECT id, fname, lname, phoneNumber, salary FROM nurse;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_nurse.j2", nurses=result, resultText = "Nurse added.")

@app.route('/browse_office')
def office():
    query = "SELECT id, name, phoneNumber, street, city, state, zip, managerID FROM office;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_office.j2", offices=result)

@app.route('/add_new_office', methods=['POST','GET'])
def add_new_office():
    if request.method == 'GET':
        query = 'SELECT id, fname, lname FROM manager;'
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('office_add_new.j2', managers=result)
    elif request.method == 'POST':
        print("Add new office")
        name = request.form['name']
        phoneNumber = request.form['phoneNumber']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zip']
        managerID = request.form['managerID']
        query = 'INSERT INTO office (name, phoneNumber, street, city, state, zip, managerID) VALUES (%s,%s,%s,%s,%s,%s,%s);'
        data = (name, phoneNumber, street, city, state, zipcode, managerID)
        db.execute_query(db_connection, query, data)

        query = "SELECT id, name, phoneNumber, street, city, state, zip, managerID FROM office;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_office.j2", offices=result, resultText="Office added.")

@app.route('/browse_patient')
def patient():
    query = "SELECT id, fname, lname, phoneNumber, street, city, state, zip, dob, weight, doctorID FROM patient;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_patient.j2", patients=result)

@app.route('/add_new_patient', methods=['POST','GET'])
def add_new_patient():
    if request.method == 'GET':
        query = 'SELECT id, fname, lname FROM doctor;'
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('patient_add_new.j2', doctors=result)
    elif request.method == 'POST':
        print("Add new patient")
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zip']
        dob = request.form['dob']
        weight = request.form['weight']
        doctorID = request.form['doctorID']
        query = 'INSERT INTO patient (fname, lname, phoneNumber, street, city, state, zip, dob, weight, doctorID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        data = (fname, lname, phoneNumber, street, city, state, zipcode, dob, weight, doctorID)
        db.execute_query(db_connection, query, data)

        query = "SELECT id, fname, lname, phoneNumber, street, city, state, zip, dob, weight, doctorID FROM patient;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_patient.j2", patients=result, resultText="Patient added")

@app.route('/browse_manager')
def manager():
    query = "SELECT id, fname, lname, phoneNumber, salary FROM manager;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_manager.j2", managers=result)

@app.route('/add_new_manager', methods=['POST','GET'])
def add_new_manager():
    if request.method == 'GET':
        return render_template('manager_add_new.j2')
    elif request.method == 'POST':
        print("Add new manager")
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']

        query = 'INSERT INTO manager (fname, lname, phoneNumber, salary) VALUES (%s,%s,%s,%s);'
        data = (fname, lname, phoneNumber, salary)
        db.execute_query(db_connection, query, data)

        query = "SELECT id, fname, lname, phoneNumber, salary FROM manager;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_manager.j2", managers=result, resultText = "Manager added.")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 