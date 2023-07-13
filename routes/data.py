from flask import Blueprint, jsonify
from models.data_model import load_data

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/api/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data)
