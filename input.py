import json

from flask import Blueprint, request

from app import app
from preprocessor import handle_packet


@app.route('/api', methods=['post'])
def post_data():
    try:
        data: dict = request.json
        ts = data["_local_time"]
    except:
        return json.dumps({'error': True}), 400, {'ContentType': 'application/json'}

    with open(f'{ts}.json', 'w') as writing:
        writing.write(json.dumps(data))

    metrics = handle_packet(data)
    return json.dumps(metrics), 200, {'ContentType': 'application/json'}


bp = Blueprint('input', __name__)