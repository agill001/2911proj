from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(200))
    drivers_license = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    booking_confirmation_number = db.Column(db.String(50))
    dob = db.Column(db.Date)
    email = db.Column(db.String(120), unique=True)

    items = db.relationship('Item', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    lost_location = db.Column(db.String(50))
    lost_time = db.Column(db.DateTime)
    finder = db.Column(db.String(50))
    status = db.Column(db.String(50))  # like found and stuff
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'))  # association with user

    notifications = db.relationship('Notification', backref='item', lazy=True)


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'))  # association with user
    item_id = db.Column(db.Integer, db.ForeignKey(
        'items.id'))  # association with item
