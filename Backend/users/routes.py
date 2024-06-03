from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from model import User, EnrolledCourse
from database import db
import os.path


users = Blueprint('users', __name__)

@users.route("/users")
def user_list_get():
    try:
        users = db.session.query(User).order_by(User.id).all()
        # Convert user objects to dictionaries
        user_data = [user.serialize() for user in users]
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"message":str(e)}), 500

 
@users.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        username=request.form["username"]
        email=request.form["email"]
        password = request.form["password"]
        if not username or not email or not password:
            return jsonify({"message": "Missing username, email, or password"}), 400
        if User.query.filter_by(username=username).first():
            return jsonify({"message": "Username already exists"}), 400
        if User.query.filter_by(email=email).first():
            return jsonify({"message": "Email already exists"}), 400
        
        user = User(username=username, 
                    email=email, 
                    password=password            
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
            total_score = request.form.get('total_score')
            if total_score is not None:
                user.total_score = total_score
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

@users.route('/users/<int:user_id>/courses', methods=['GET'])
def user_courses_get(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        courses = user.enrolled_courses
        course_data = [course.serialize() for course in courses]
        return jsonify(course_data), 200
    except:
        return jsonify({'error': 'Cannot get user courses'}), 500

@users.route('/users/<int:user_id>/courses', methods=['POST'])
def user_courses_add(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        course_id = request.form.get('course_name').lower()

        quiz_filename = os.path.join("quizzes", f'{course_id.replace(" ", "_")}_quiz.json')

        if not os.path.exists(quiz_filename):
            return jsonify({'error': 'Course not found'}), 404
        else:
            enrolled_course = EnrolledCourse(
            user_id=user_id,
            id=course_id)
            db.session.add(enrolled_course)
            db.session.commit()
        
            return jsonify({'success': 'Course added to user'}), 201
        
    except:
        return jsonify({'error': 'Cannot add course to user'}), 500

@users.route('/users/<int:user_id>/courses', methods=['PUT'])
def user_course_update(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        course_name = request.form.get('course_name').lower()
        enrolled_course = EnrolledCourse.query.filter_by(user_id=user_id, id=course_name).first()
        if not enrolled_course:
            return jsonify({'error': 'Course not found for user'}), 404

        completion_status = request.form.get('completion')
        if not completion_status:
            return jsonify({'error': 'Completion status not provided'}), 400
        if not 0 <= float(completion_status) <= 1:
            return jsonify({'error': 'Completion status must be between 0 and 1'}), 400
        enrolled_course.completion = completion_status
        db.session.commit()

        return jsonify({'success': 'Course completion updated'}), 200
    
    except:
        return jsonify({'error': 'Cannot update course completion'}), 500
    
@users.route('/users/<int:user_id>/courses', methods=['DELETE'])
def user_course_delete(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        course_name = request.form.get('course_name')
        if not course_name:
            return jsonify({'error': 'Course name not provided'}), 400

        enrolled_course = EnrolledCourse.query.filter_by(user_id=user_id, id=course_name).first()
        if not enrolled_course:
            return jsonify({'error': 'Course not found for user'}), 404

        db.session.delete(enrolled_course)
        db.session.commit()

        return jsonify({'success': 'Course deleted from user'}), 200

    except:
        return jsonify({'error': 'Cannot delete course from user'}), 500
    

@users.route('/users/leaderboard', methods=['GET'])
def user_leaderboard():
    try:
        users = db.session.query(User).order_by(User.total_score.desc()).limit(10).all()
        leaderboard_data = [user.serialize() for user in users]
        return jsonify(leaderboard_data), 200
    except:
        return jsonify({'error': 'Cannot get leaderboard'}), 500
