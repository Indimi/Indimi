from datetime import datetime
from app.factory import db
from app.config import Base
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.sql.expression import text

class SearchRecord(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}searchrecord"

    search_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    query = db.Column(db.String(100), nullable=False)
    suggest = db.Column(db.String(100), nullable=True)
    iterations = db.Column(INTEGER(11), nullable=False)
    results = db.Column(INTEGER(11), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    timetaken =  db.Column(INTEGER(11), nullable=False)
    remoteaddr = db.Column(db.String(50), nullable=True)
    source = db.Column(db.String(10), nullable=True)