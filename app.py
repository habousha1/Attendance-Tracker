import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prenom TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                status TEXT NOT NULL,
                date DATE NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        ''')
        db.commit()

init_db()

@app.route('/')
def index():
    db = get_db()
    
    # Get all students
    students = db.execute('SELECT * FROM students').fetchall()
    
    # Get today's attendance for these students
    today = datetime.now().strftime('%Y-%m-%d')
    attendance_records = db.execute(
        'SELECT student_id, status FROM attendance WHERE date = ?', (today,)
    ).fetchall()
    
    # Map student_id to today's status
    student_status = {record['student_id']: record['status'] for record in attendance_records}
    
    # Calculate global stats
    total_presents = db.execute('SELECT COUNT(*) FROM attendance WHERE status = "present"').fetchone()[0]
    total_absences = db.execute('SELECT COUNT(*) FROM attendance WHERE status = "absent"').fetchone()[0]

    return render_template('index.html', students=students, student_status=student_status, 
                           total_presents=total_presents, total_absences=total_absences, today=today)

@app.route('/add', methods=('GET', 'POST'))
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        prenom = request.form['prenom']

        if name and prenom:
            db = get_db()
            db.execute('INSERT INTO students (name, prenom) VALUES (?, ?)', (name, prenom))
            db.commit()
            return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/attendance/<int:student_id>', methods=('POST',))
def mark_attendance(student_id):
    status = request.form['status']
    date = datetime.now().strftime('%Y-%m-%d')
    
    if status in ['present', 'absent']:
        db = get_db()
        # Check if already marked for today
        existing = db.execute(
            'SELECT id FROM attendance WHERE student_id = ? AND date = ?', (student_id, date)
        ).fetchone()
        
        if existing:
            # Update
            db.execute(
                'UPDATE attendance SET status = ? WHERE id = ?', (status, existing['id'])
            )
        else:
            # Insert
            db.execute(
                'INSERT INTO attendance (student_id, status, date) VALUES (?, ?, ?)',
                (student_id, status, date)
            )
        db.commit()
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
