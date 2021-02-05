from .. import db
from ..model.base import Base


class Poll(Base):
    """ User Model for storing user related details """
    __tablename__ = "polls"

    title = db.Column(db.String(255), nullable=False)
