from app.factory import db
from app.config import Base
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.sql.expression import text

class Rank(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}rank"

    rank_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    threshold = db.Column(INTEGER(10, unsigned=True), nullable=False)

class Role(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}role"

    role_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class Subscription(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}subscription"

    subscription_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class User(db.Model):
    __tablename__ = f"{Base.DATABASE_TABLE_PREFIX}user"

    user_id = db.Column(INTEGER(10, unsigned=True), primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)    
    email = db.Column(db.String(255), unique=True, nullable=False)
    website = db.Column(db.String(255), nullable=True)
    timezone = db.Column(db.String(50), nullable=True)
    lastlogin = db.Column(db.TIMESTAMP, nullable=True)
    lastloginattempt = db.Column(db.TIMESTAMP, nullable=True)
    failedloginattempts = db.Column(INTEGER(11), nullable=False, server_default=text("0"))
    remembertoken = db.Column(db.String(100), nullable=True)
    voided = db.Column(TINYINT(1), nullable=False, server_default=text("0"))


