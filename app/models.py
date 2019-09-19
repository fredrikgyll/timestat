from timestat import db
from enum import IntEnum


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    short_name = db.Column(db.String(2), unique=True, nullable=False, default='XX')

    def __repr__(self):
        return f'<Location {self.name}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Hour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f'<Hour {self.start:%H:%M}-{self.end:%H:%M}>'


class WorkDays(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4


class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Enum(WorkDays))
    hour = db.Column(db.Integer, db.ForeignKey('hour.id'), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    number_of_workers = db.Column(db.Integer)

    def __repr__(self):
        return f'<Shift:{self.id} {self.day.name}>'


class ShiftPreference(IntEnum):
    REFUSE = 0
    NEUTRAL = 1
    PREFER = 2


class ShiftWorker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shift = db.Column(db.Integer,
                      db.ForeignKey('shift.id'),
                      nullable=False)
    user = db.Column(db.Integer,
                     db.ForeignKey('user.id'),
                     nullable=False)
    preference = db.Column(db.Enum(ShiftPreference))

    def __repr__(self):
        return f'<ShiftWorker:{self.id}>'
