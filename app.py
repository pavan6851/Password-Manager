from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Password model
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Password('{self.website}', '{self.username}')"

# Home route: display all passwords
@app.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

# Add route: add a new password
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        website = request.form['website']
        username = request.form['username']
        password = request.form['password']
        
        new_password = Password(website=website, username=username, password=password)
        db.session.add(new_password)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit route: edit an existing password
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    password = Password.query.get_or_404(id)
    if request.method == 'POST':
        password.website = request.form['website']
        password.username = request.form['username']
        password.password = request.form['password']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', password=password)

# Delete route: delete a password
@app.route('/delete/<int:id>')
def delete(id):
    password = Password.query.get_or_404(id)
    db.session.delete(password)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
