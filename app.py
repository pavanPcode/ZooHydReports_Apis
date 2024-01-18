from flask import Flask, request, jsonify
from db import ExecuteUpdate
from SqlQuarys import insertSipetransaction,insertHelathcheck
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/SwipeTransactions', methods=['POST'])
def insert_data():
    try:
        data = request.json

        result_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
        quary = insertSipetransaction.format(data['superId'], data['RID'], data['ticketType'], data['BRN'], data['GATE'],
                       data['availableAdultEntryCount'], data['totalAdultEntryCount'], data['bookingDate'],
                       str(result_time), 1)

        connection = ExecuteUpdate(quary)
        return jsonify({'message': 'Data inserted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/HealthStatus', methods=['POST'])
def HealthStatus():
    try:
        data = request.json
        quary = insertHelathcheck.format(data['typeid'],data['message'],data['gate'],data['ErrorMessage'],data['superid'],data['GateType'])
        connection = ExecuteUpdate(quary)
        return jsonify({'message': 'Data inserted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def INDEX():
    try:
        return jsonify({'message': 'Apis'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
