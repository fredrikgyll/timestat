from app import app, manager, db
from app.models import Hour
from flask import jsonify, json,  make_response


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/hour/increment/<int:hour_id>', methods=['PUT'])
def increment_hour(hour_id):
    hour = Hour.query.get(hour_id)
    hour.frequency = hour.frequency + 1
    db.session.commit()
    return jsonify(hour.serialize)


manager.create_api(Hour, methods=['GET', 'POST', 'PUT'])
