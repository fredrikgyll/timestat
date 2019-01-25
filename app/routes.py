from app import app, manager, db
from app.models import Hour, Location, LocationHour
from flask import jsonify,  make_response


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/locationhour/increment/<int:lochour_id>', methods=['PUT'])
def increment_hour(hour_id):
    lhour = LocationHour.query.get(hour_id)
    lhour.frequency = lhour.frequency + 1
    db.session.commit()
    return make_response(jsonify({
        'id': lhour.id,
        'frequency': lhour.frequency
    }), 200)


manager.create_api(Hour, methods=['GET'])
manager.create_api(Location, methods=['GET'])
manager.create_api(LocationHour, methods=['GET'])
