from flask import Flask, render_template, request, redirect

import mysql.connector as ms

app = Flask(__name__)

# Simulated user database (Replace with an actual database in a real application)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/nadhome')
def nadhome():
    return render_template('nadhome.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    db = ms.connect(host='localhost', user='root', passwd='dpsbn', database='cars')
    cursor = db.cursor()
    cursor.execute('select * from pswd')
    a = cursor.fetchall()
    
    for i in a:
        if username == i[1] and password == i[2]:
            if username == 'admin' and password == 'admin':
                return 'Admin Login Successful'
            else:
                return redirect('/nadhome')
    
    return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
