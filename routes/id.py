from flask import Blueprint, jsonify
from models.data_model import load_data

id_bp = Blueprint('id_bp', __name__)

@id_bp.route('/api/id/<int:id>', methods=['GET'])
def get_data_by_id(id):
    data = load_data()
    record = next((item for item in data if item['id'] == id), None)
    if record:
        return jsonify(record)
    else:
        return jsonify({'error': 'Record not found'}), 404
