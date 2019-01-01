from app.factory import db
from app.config import Base
from sqlalchemy.dialects.mysql import INTEGER

class Entry(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}entry"

    entry_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    media = db.Column(INTEGER(10, unsigned=True), nullable=False)