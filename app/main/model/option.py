from ..model.base import Base
from .. import db


class Option(Base):
    """ User Model for storing user related details """
    __tablename__ = "option"

    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
    name = db.Column(db.String(255), nullable=False)
