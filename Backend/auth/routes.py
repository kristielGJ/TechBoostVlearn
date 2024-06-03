from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from model import User, EnrolledCourse
from database import db

auth = Blueprint('auth', __name__)

@auth.route("/auth/test", methods=["GET"])
def test():
    return "Hello, World!"

@auth.route("/auth/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
        
    user = User.query.filter_by(email=email).first()
    
    
    if user and (password == user.password):
        access_token = create_access_token(identity=email)
        return jsonify({'message': 'Login Success',
                        'id': user.id,
                        'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Login Failed'}), 401