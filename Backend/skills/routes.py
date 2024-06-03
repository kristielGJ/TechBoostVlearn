from flask import Blueprint, jsonify, request
from model import User, Skill
from database import db


skills = Blueprint('skills', __name__)

#Add skill to user
@skills.route("/users/<int:user_id>/skills", methods=["POST"])
def add_skill(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    skill_name = request.form.get("skill_name")
    rating = request.form.get("rating")

    if not skill_name or rating is None:
        return jsonify({"message": "Missing skill name or rating"}), 400

    skill = Skill(user_id=user_id, skill_name=skill_name, rating=int(rating))
    db.session.add(skill)
    db.session.commit()

    return jsonify(skill.serialize()), 201

# Get skills for a user
@skills.route("/users/<int:user_id>/skills", methods=["GET"])
def get_skills(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    skills = Skill.query.filter_by(user_id=user_id).all()
    return jsonify([{"skill_name": skill.skill_name, "rating": skill.rating} for skill in skills]), 200


# Update an existing skill for a user
@skills.route("/users/<int:user_id>/skills/<string:skill_name>", methods=["PUT"])
def update_skill(user_id, skill_name):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    skill = Skill.query.filter_by(user_id=user_id, skill_name=skill_name).first()
    if not skill:
        return jsonify({"message": "Skill not found"}), 404

    rating = request.form.get("rating")
    if rating is None:
        return jsonify({"message": "Missing rating"}), 400

    skill.rating = int(rating)
    db.session.commit()

    return jsonify(skill.serialize()), 200

# Delete a skill for a user
@skills.route("/users/<int:user_id>/skills/<string:skill_name>", methods=["DELETE"])
def delete_skill(user_id, skill_name):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    skill = Skill.query.filter_by(user_id=user_id, skill_name=skill_name).first()
    if not skill:
        return jsonify({"message": "Skill not found"}), 404

    db.session.delete(skill)
    db.session.commit()

    return jsonify({"message": "Skill deleted"}), 200
