from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "my_secret_key"
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('Inregistrare.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            return "Toate câmpurile trebuie completate."

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        existing_user = cursor.fetchone()
        conn.close()

        if existing_user:
            return "Utilizatorul cu această adresă de email există deja."

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        conn.commit()
        conn.close()

        return redirect(url_for('signin'))

    return render_template('Inregistrare.html')

@app.route('/signin')
def signin():
    return render_template('Conectare.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user_id'] = user[0]
        return redirect(url_for('game'))
    else:
        return "Autentificare eșuată. Utilizatorul nu există sau parola este greșită."

@app.route('/retete')
def game():
    if 'user_id' not in session:
        return redirect(url_for('signin'))

    return render_template('Retete.html')

if __name__ == '__main__':
    app.run(debug=True)