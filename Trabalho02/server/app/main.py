from flask import Flask
app = Flask(__name__)

from flask import  render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

HTTP_ESP_URL = "http://192.168.229.34:80"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    passCode = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

with app.app_context():
    db.create_all()

@app.get('/')
def hello_world():
    return "hello world"


@app.get('/user')
def get_users():
    users = User.query.order_by(User.date_created).all()
    return render_template('index.html', users=users, HTTP_ESP_URL=HTTP_ESP_URL)

@app.post('/user')
def upload_user():
    user_name = request.form['name']
    user_pass_code = request.form['passCode']
    new_user = User(name=user_name, passCode=user_pass_code)

    try:
        db.session.add(new_user)
        db.session.commit()
        return redirect('/user')
    except:
        print('There was an issue adding your user')

@app.route('/user/delete/<int:id>')
def delete(id):
    user_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/user')
    except:
        return 'There was a problem deleting that user'


@app.route('/user/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['name']
        user.passCode = request.form['passCode']

        try:
            db.session.commit()
            return redirect('/user')
        except:
            return 'There was an issue updating your user'

    else:
        return render_template('update.html', user=user)

@app.get('/confirmCode/<string:passCode>')
def get_user_by_passcode(passCode):
    user = db.session.query(User).filter_by(passCode=passCode).first()

    if user:
        return "1"

    return "0"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=80)