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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        doctor = request.form['doctor']
       
        query = "SELECT * from doctor WHERE fname LIKE %s OR lname LIKE %s;"
        data = (doctor, doctor)
        result = db.execute_query(db_connection, query, data).fetchall()
        
        
        if len(data) == 0: 
            query = "SELECT * FROM doctor;"
            data = (doctor, doctor)
            result = db.execute_query(db_connection, query, data).fetchall()
            
        return render_template('search.j2', search=result)
    return render_template('search.j2')

@app.route('/browse_doctor')
def doctor():
    db_connection = db.connect_to_database()
    query = "SELECT doctor.id, doctor.fname, doctor.lname, doctor.phoneNumber, doctor.salary, nurse.fname, nurse.lname FROM doctor LEFT JOIN nurse ON doctor.nurseID = nurse.id;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_doctor.j2", doctors=result)

@app.route('/add_new_doctor', methods=['POST','GET'])
def add_new_doctor():
    db_connection = db.connect_to_database()
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

        query = "SELECT doctor.id, doctor.fname, doctor.lname, doctor.phoneNumber, doctor.salary, nurse.fname, nurse.lname FROM doctor LEFT JOIN nurse ON doctor.nurseID = nurse.id;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_doctor.j2", doctors=result, resultText = "Doctor added.")

@app.route('/update_doctor/<int:id>', methods=['POST','GET'])
def update_doctor(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        doctor_query = 'SELECT id, fname, lname, phoneNumber, salary, nurseID FROM doctor WHERE id = %s' % (id)
        doctor_result = db.execute_query(db_connection, doctor_query).fetchone()
        if doctor_result == None:
            return "No such doctor found!"
        nurses_query = 'SELECT id, fname, lname FROM nurse'
        nurses_results = db.execute_query(db_connection, nurses_query).fetchall()
        return render_template('doctor_update.j2', nurses = nurses_results, doctor = doctor_result)
    elif request.method == 'POST':
        doctor_id = request.form['doctor_id']
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']
        nurseID = request.form['nurseID']

        query = "UPDATE doctor SET fname = %s, lname = %s, phoneNumber = %s, salary = %s, nurseID = %s WHERE id = %s"
        data = (fname, lname, phoneNumber, salary, nurseID, doctor_id)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")
        return redirect('/browse_doctor')

@app.route('/delete_doctor/<int:id>')
def delete_doctor(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM doctor WHERE id = %s"
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    print(str(result.rowcount) + " row(s) updated")
    return redirect('/browse_doctor')

@app.route('/browse_nurse')
def nurse():
    db_connection = db.connect_to_database()
    query = "SELECT id, fname, lname, phoneNumber, salary FROM nurse;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_nurse.j2", nurses=result)

@app.route('/add_new_nurse', methods=['POST','GET'])
def add_new_nurse():
    db_connection = db.connect_to_database()
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

@app.route('/update_nurse/<int:id>', methods=['POST','GET'])
def update_nurse(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        nurse_query = 'SELECT id, fname, lname, phoneNumber, salary FROM nurse WHERE id = %s' % (id)
        nurse_result = db.execute_query(db_connection, nurse_query).fetchone()
        if nurse_result == None:
            return "No such nurse found!"
        return render_template('nurse_update.j2', nurse = nurse_result)
    elif request.method == 'POST':
        nurse_id = request.form['nurse_id']
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']

        query = "UPDATE nurse SET fname = %s, lname = %s, phoneNumber = %s, salary = %s WHERE id = %s"
        data = (fname, lname, phoneNumber, salary, nurse_id)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_nurse')
        
@app.route('/delete_nurse/<int:id>')
def delete_nurse(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM nurse WHERE id = %s"
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    print(str(result.rowcount) + " row(s) updated")
    return redirect('/browse_nurse')

@app.route('/browse_office')
def office():
    db_connection = db.connect_to_database()
    query = "SELECT office.id, office.name, office.phoneNumber, office.street, office.city, office.state, office.zip, manager.fname, manager.lname FROM office LEFT JOIN manager ON office.managerID = manager.id;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_office.j2", offices=result)

@app.route('/add_new_office', methods=['POST','GET'])
def add_new_office():
    db_connection = db.connect_to_database()
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

        query = "SELECT office.id, office.name, office.phoneNumber, office.street, office.city, office.state, office.zip, manager.fname, manager.lname FROM office LEFT JOIN manager ON office.managerID = manager.id;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_office.j2", offices=result, resultText="Office added.")

@app.route('/update_office/<int:id>', methods=['POST','GET'])
def update_office(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        office_query = 'SELECT id, name, phoneNumber, street, city, state, zip, managerID FROM office WHERE id = %s' % (id)
        office_result = db.execute_query(db_connection, office_query).fetchone()
        if office_result == None:
            return "No such office found!"
        manager_query = 'SELECT id, fname, lname FROM manager'
        manager_results = db.execute_query(db_connection, manager_query).fetchall()
        return render_template('office_update.j2', managers = manager_results, office = office_result)
    elif request.method == 'POST':
        office_id = request.form['office_id']
        name = request.form['name']
        phoneNumber = request.form['phoneNumber']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipco = request.form['zip']
        managerID = request.form['managerID']

        query = "UPDATE office SET name = %s, phoneNumber = %s, street = %s, city = %s, state = %s, zip = %s, managerID = %s WHERE id = %s"
        data = (name, phoneNumber, street, city, state, zipco, managerID, office_id)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")
        return redirect('/browse_office')

@app.route('/delete_office/<int:id>')
def delete_office(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM office WHERE id = %s"
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    print(str(result.rowcount) + " row(s) updated")
    return redirect('/browse_office')

@app.route('/browse_patient')
def patient():
    db_connection = db.connect_to_database()
    query = "SELECT patient.id, patient.fname, patient.lname, patient.phoneNumber, patient.street, patient.city, patient.state, patient.zip, patient.dob, patient.weight, doctor.fname, doctor.lname FROM patient LEFT JOIN doctor ON patient.doctorID = doctor.id;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_patient.j2", patients=result)

@app.route('/add_new_patient', methods=['POST','GET'])
def add_new_patient():
    db_connection = db.connect_to_database()
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

        query = "SELECT patient.id, patient.fname, patient.lname, patient.phoneNumber, patient.street, patient.city, patient.state, patient.zip, patient.dob, patient.weight, doctor.fname, doctor.lname FROM patient LEFT JOIN doctor ON patient.doctorID = doctor.id;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template("browse_patient.j2", patients=result, resultText="Patient added")

@app.route('/update_patient/<int:id>', methods=['POST','GET'])
def update_patient(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        patient_query = 'SELECT id, fname, lname, phoneNumber, street, city, state, zip, dob, weight, doctorID FROM patient WHERE id = %s' % (id)
        patient_result = db.execute_query(db_connection, patient_query).fetchone()
        if patient_result == None:
            return "No such patient found!"
        doctor_query = 'SELECT id, fname, lname FROM doctor'
        doctor_results = db.execute_query(db_connection, doctor_query).fetchall()
        return render_template('patient_update.j2', doctors = doctor_results, patient = patient_result)
    elif request.method == 'POST':
        patient_id = request.form['patient_id']
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipco = request.form['zip']
        dob = request.form['dob']
        weight = request.form['weight']
        doctorID = request.form['doctorID']

        query = "UPDATE patient SET fname = %s, lname = %s, phoneNumber = %s, street = %s, city = %s, state = %s, zip = %s, dob = %s, weight = %s, doctorID = %s WHERE id = %s"
        data = (fname, lname, phoneNumber, street, city, state, zipco, dob, weight, doctorID, patient_id)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")
        return redirect('/browse_patient')

@app.route('/delete_patient/<int:id>')
def delete_patient(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM patient WHERE id = %s"
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    print(str(result.rowcount) + " row(s) updated")
    return redirect('/browse_patient')

@app.route('/browse_manager')
def manager():
    db_connection = db.connect_to_database()
    query = "SELECT id, fname, lname, phoneNumber, salary FROM manager;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template("browse_manager.j2", managers=result)

@app.route('/add_new_manager', methods=['POST','GET'])
def add_new_manager():
    db_connection = db.connect_to_database()
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

@app.route('/update_manager/<int:id>', methods=['POST','GET'])
def update_manager(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        manager_query = 'SELECT id, fname, lname, phoneNumber, salary FROM manager WHERE id = %s' % (id)
        manager_result = db.execute_query(db_connection, manager_query).fetchone()
        if manager_result == None:
            return "No such manager found!"
        return render_template('manager_update.j2', manager = manager_result)
    elif request.method == 'POST':
        manager_id = request.form['manager_id']
        fname = request.form['fname']
        lname = request.form['lname']
        phoneNumber = request.form['phoneNumber']
        salary = request.form['salary']

        query = "UPDATE manager SET fname = %s, lname = %s, phoneNumber = %s, salary = %s WHERE id = %s"
        data = (fname, lname, phoneNumber, salary, manager_id)
        result = db.execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated")

        return redirect('/browse_manager')
        
@app.route('/delete_manager/<int:id>')
def delete_manager(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM manager WHERE id = %s"
    data = (id,)
    result = db.execute_query(db_connection, query, data)
    print(str(result.rowcount) + " row(s) updated")
    return redirect('/browse_manager')

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 
