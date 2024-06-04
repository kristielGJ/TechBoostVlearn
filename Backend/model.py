from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db

enrollment = db.Table('enrollment',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('enrolled_course_id', db.Integer, db.ForeignKey('enrolled_courses.id'), primary_key=True),
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    interests = db.Column(db.Text, default='')
    jobs = db.Column(db.Text, default='')
    total_score = db.Column(db.Integer,default=0)
    user_role = db.relationship('UserRole', back_populates='user', uselist=False, cascade="all, delete, delete-orphan")
    enrolled_courses = db.relationship('EnrolledCourse', back_populates='user', cascade="all, delete-orphan")
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'total_score': self.total_score,
            'jobs': self.jobs,
            'interests': self.interests,
        }

class Skill(db.Model):
    __tablename__ = 'skills'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    skill_name = db.Column(db.String(80), primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'skill_name': self.skill_name,
            'rating': self.rating
        }
 
class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user = db.relationship('User', back_populates='user_role')
    role = db.relationship('Role', back_populates='user_roles')
 
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255), unique=True)
    permissions = db.Column(db.Text)
    user_roles = db.relationship('UserRole', back_populates='role')

class EnrolledCourse(db.Model):
    __tablename__ = 'enrolled_courses'
    id = db.Column(db.String(255), primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    completion = db.Column(db.Float, nullable=False, default=0)
    user = db.relationship('User', back_populates='enrolled_courses')

    def serialize(self):
        return {
            'id': self.id,
            'completion': self.completion
        }
 