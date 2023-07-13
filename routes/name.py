from flask import Blueprint, jsonify
from models.data_model import load_data

name_bp = Blueprint('name_bp', __name__)

@name_bp.route('/api/name/<string:name>', methods=['GET'])
def get_data_by_name(name):
    data = load_data()
    matching_records = [item for item in data if item['name'].lower() == name.lower()]
    return jsonify(matching_records)
