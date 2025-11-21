from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="practice1"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("students.html", students=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return redirect('/students')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)
