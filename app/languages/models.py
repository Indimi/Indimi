from app.factory import db
from app.config import Base
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, CHAR


class Language(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}language"

    language_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    code = db.Column(CHAR(2), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)    
    localname = db.Column(db.String(50), nullable=False)    
    queryurl = db.Column(db.String(255), nullable=True) 
    hastranslation = db.Column(TINYINT(1), nullable=False)
    haslexical = db.Column(TINYINT(1), nullable=False)