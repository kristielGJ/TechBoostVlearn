from flask import Blueprint, jsonify, request
from model import User
from database import db


users = Blueprint('users', __name__)

@users.route("/users")
def user_list():
    users = db.session.query(User).order_by(User.username).all()
    # Convert user objects to dictionaries
    user_data = [user.serialize() for user in users]
    return jsonify(user_data)
 
@users.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        # Return user data as JSON
        return jsonify(user.serialize())
 
    return jsonify({"message": "User created"})  # Optional message for GET

@users.route('/users/update/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'})
    if request.method == 'PUT':
        user.username = request.form.get('username', user.username)
        user.email = request.form.get('email', user.email)
        user.password = request.form.get('password', user.password)
        db.session.commit()
        return jsonify({'success': 'User updated'})
    return jsonify({'message': 'Invalid request method'})

@users.route('/users/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'})
 
    db.session.delete(user)
    db.session.commit()

    return jsonify({'success': 'User and associated user role deleted'})