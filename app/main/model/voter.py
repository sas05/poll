from .. import db
from ..model.base import Base


class Voter(Base):
    """ User Model for storing user related details """
    __tablename__ = "voter"

    email = db.Column(db.String(255), unique=True, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
