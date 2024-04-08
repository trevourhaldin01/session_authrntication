from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_cors import CORS
from config import ApplicationConfig
from models import db, User

app = Flask(__name__)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

app.config.from_object(ApplicationConfig)
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    #gets email and password input
    email  =request.json['email']
    password  = request.json['password']

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error":"user already exists"}), 409
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    session['user_id']=new_user.id
    return jsonify ({
        "id": new_user.id,
        "email": new_user.email
    })

@app.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error":"unauthorized"}), 401
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error":"unauthorized"})
    
    session['user_id']=user.id
    return jsonify ({
        "id": user.id,
        "email": user.email
    })

@app.route('/logout', methods=['POST'])
def logout_user():
    session.pop("user_id")
    return "200"

#get user data if logged in

@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    }) 








server_session = Session(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
