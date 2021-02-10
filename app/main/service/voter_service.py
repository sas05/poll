import uuid
import datetime

from app.main import db
from app.main.model.voter import Voter


def get_all_voters():
    return Voter.query.all()


def save_new_voter(data):
    voter = Voter.query.filter_by(email=data['email']).first()
    if not voter:
        new_voter = Voter(
            public_id=str(uuid.uuid4()),
            email=data['email']
        )
        save_changes(new_voter)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()
