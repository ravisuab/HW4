from numbers import Number
import sqlite3
import os
from tkinter.tix import INTEGER
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
secret_key = os.urandom(24).hex()
app.config['SECRET_KEY'] = secret_key

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_employee(id: Number):
    conn = get_db()
    employee = conn.execute('SELECT * FROM EMPLOYEE WHERE id = ?', (id,)).fetchone()
    conn.commit()
    conn.close()
    return employee


@app.get('/nav/display')
def nav_to_display_employees():
    return redirect(url_for('render_employees'))

@app.get('/nav/create')
def nav_to_create_employee():
    return redirect(url_for('render_create_employee'))

@app.get('/nav/edit/<int:id>/')
def nav_to_edit_employee(id: Number):
    return redirect(url_for('render_edit_employee', id=id))

@app.get('/display/')
def render_employees():
    conn = get_db()
    employees = conn.execute('SELECT * FROM EMPLOYEE').fetchall()
    conn.close()
    return render_template('display.html', employees=employees)

@app.get('/search')
def render_filtered_employees():
    args = request.args
    conn = get_db()
    employees = conn.execute('SELECT * FROM EMPLOYEE WHERE mobile = ?',(args.get("mobile"),)).fetchall()
    conn.close()
    return render_template('display.html', employees=employees)

@app.post('/create/')
def create_employee():
    name = request.form['name']
    company_name = request.form['company_name']
    email = request.form['email']
    mobile = request.form['mobile']
    address = request.form['address']

    if not name or not company_name or not email or not mobile or not address:
        flash('Please fill all fields')
        return render_template('create.html', error='Please fill all fields')
    else:
        conn = get_db()
        conn.execute('INSERT INTO employee (name, company_name, email, mobile, address) VALUES (?, ?, ?, ?, ? )',
            (name, company_name, email, mobile, address))
        conn.commit()
        conn.close()
        return redirect(url_for('render_employees'))

@app.get('/create/')
def render_create_employee():
    return render_template('create.html')

@app.get('/edit/<int:id>/')
def render_edit_employee(id):
    employee = get_employee(id)
    return render_template('edit.html', employee=employee)

@app.post('/edit/<int:id>/')
def edit_employee(id):
    name = request.form['name']
    company_name = request.form['company_name']
    email = request.form['email']
    mobile = request.form['mobile']
    address = request.form['address']

    if not name or not company_name or not email or not mobile or not address:
        flash('Please fill all fields')
    else:
        conn = get_db()
        conn.execute('UPDATE employee SET name = ?, company_name = ?, email = ?, mobile = ?,'
                    ' address = ? WHERE id = ?',
            (name, company_name, email, mobile, address, id))
        conn.commit()
        conn.close()
        return redirect(url_for('render_employees'))

@app.post('/delete/<int:id>/')
def delete_employee(id):
    conn = get_db()
    conn.execute('DELETE FROM employee WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Selected record deleted successfully')
    return redirect(url_for('render_employees'))