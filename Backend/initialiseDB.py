'''Authors: Ajay Dayalani
'''
from model import User, Skill
def create_users_and_skills(app, db):
    with app.app_context():
        users_data = [
            {"username": "john_doe", "email": "john.doe@vodafone.com", "password": "password1"},
            {"username": "jane_smith", "email": "jane.smith@vodafone.com", "password": "password2"},
            {"username": "alice_wonderland", "email": "alice.wonderland@vodafone.com", "password": "password3"},
            {"username": "bob_carpenter", "email": "bob.carpenter@vodafone.com", "password": "password4"},
            {"username": "emma_jones", "email": "emma.jones@vodafone.com", "password": "password5"},
            {"username": "michael_scott", "email": "michael.scott@vodafone.com", "password": "password6"},
            {"username": "pam_beesly", "email": "pam.beesly@vodafone.com", "password": "password7"},
            {"username": "dwight_schrute", "email": "dwight.schrute@vodafone.com", "password": "password8"},
            {"username": "stanley_hudson", "email": "stanley.hudson@vodafone.com", "password": "password9"},
            {"username": "kevin_malone", "email": "kevin.malone@vodafone.com", "password": "password10"}
        ]

        for user_data in users_data:
            user = User(**user_data)
            db.session.add(user)

        db.session.commit()

        skills_data = [
            {"user_id": 1, "skill_name": "Python", "rating": 4},
            {"user_id": 1, "skill_name": "Flask", "rating": 3},
            {"user_id": 2, "skill_name": "JavaScript", "rating": 2},
            {"user_id": 2, "skill_name": "React", "rating": 2},
            {"user_id": 3, "skill_name": "SQL", "rating": 1},
            {"user_id": 3, "skill_name": "Database Design", "rating": 2},
            {"user_id": 4, "skill_name": "Java", "rating": 4},
            {"user_id": 4, "skill_name": "Spring", "rating": 4},
            {"user_id": 4, "skill_name": "HTML", "rating": 2},
            {"user_id": 5, "skill_name": "CSS", "rating": 2},
            {"user_id": 6, "skill_name": "Leadership", "rating": 2},
            {"user_id": 6, "skill_name": "Management", "rating": 5},
            {"user_id": 7, "skill_name": "Microsoft Excel", "rating": 1},
            {"user_id": 7, "skill_name": "Microsoft Word", "rating": 1},
            {"user_id": 7, "skill_name": "Sales", "rating": 3},
            {"user_id": 8, "skill_name": "Customer Service", "rating": 3},
            {"user_id": 9, "skill_name": "Problem Solving", "rating": 1},
            {"user_id": 9, "skill_name": "Decision Making", "rating": 3},
            {"user_id": 10, "skill_name": "Accounting", "rating": 2},
            {"user_id": 10, "skill_name": "Finance", "rating": 3}
        ]

        for skill_data in skills_data:
            skill = Skill(**skill_data)
            db.session.add(skill)

        db.session.commit()

        print("Users and skills created successfully.")
