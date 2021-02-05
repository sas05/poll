from ..model.base import Base
from .. import db


class Voter(Base):
    """ User Model for storing user related details """
    __tablename__ = "result"

    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'))
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'))
