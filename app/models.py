from app import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location_hours = db.relationship('LocationHour', 
                                     backref='location', 
                                     lazy=True)

    def __repr__(self):
        return f'<Location {self.name}>'


class Hour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)
    location_hours = db.relationship('LocationHour', backref='hour', lazy=True)

    def __repr__(self):
        return f'<Hour {self.id}>'


class LocationHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    frequency = db.Column(db.Integer)
    hour_id = db.Column(db.Integer, db.ForeignKey('hour.id'), nullable=False)
    location_id = db.Column(db.Integer, 
                            db.ForeignKey('location.id'), 
                            nullable=False)

    def __repr__(self):
        return (f'<LocHour {self.date} - '
                f'h:{self.hour_id} - l:{self.location_id}>')
