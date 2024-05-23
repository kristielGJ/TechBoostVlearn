from flask import Blueprint, jsonify, request
from model import User
from database import db


users = Blueprint('users', __name__)

@users.route("/users")
def user_list_get():
    try:
        users = db.session.query(User).order_by(User.username).all()
        # Convert user objects to dictionaries
        user_data = [user.serialize() for user in users]
        return jsonify(user_data), 200
    except:
        return jsonify({"message": "Cannot get all users"}), 500

 
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
        return jsonify(user.serialize()), 201
 
    return jsonify({"message": "User created"})  # Optional message for GET


@users.route('/users/<int:user_id>', methods=['GET'])
def user_get(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.serialize()), 200
    except:
        return jsonify({'error': 'Cannot get user'}), 500

@users.route('/users/update/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        if request.method == 'PUT':
            user.username = request.form.get('username', user.username)
            user.email = request.form.get('email', user.email)
            user.password = request.form.get('password', user.password)
            db.session.commit()
            return jsonify({'success': 'User updated'}), 200
        return jsonify({'message': 'Invalid request method'}), 405
    except:
        return jsonify({'error': 'Cannot update user'}), 500

@users.route('/users/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):

    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'success': 'User and associated user role deleted'}), 200
    except:
        return jsonify({'error': 'Cannot delete user'}), 500
