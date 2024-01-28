from flask import Flask, request, jsonify
from db import ExecuteUpdate,ExecuteGetQuery
from SqlQuarys import insertSipetransaction,insertHelathcheck,gethealthstatusquary,getSwipetransactionquary
from datetime import datetime, timedelta
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def INDEX():
    try:
        return jsonify({'message': 'Apis'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/SwipeTransactions', methods=['POST'])
def insert_data():
    try:
        data = request.json

        result_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
        quary = insertSipetransaction.format(data['superId'], data['RID'], data['ticketType'], data['BRN'], data['GATE'],
                       data['availableAdultEntryCount'], data['totalAdultEntryCount'], data['bookingDate'],
                       str(result_time), 1,data['GATETYPE'])

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


@app.route('/GetHealthStatus')
def GetHealthStatus():
    try:
        typeid = request.args.get('typeid', default='typeid')
        gate = request.args.get('gate', default='gate')
        GATETYPE = request.args.get('GATETYPE', default='GATETYPE')

        createdon = request.args.get('createdon', default='createdon between createdon and createdon')

        if typeid == '' or typeid == '0':
            typeid = 'typeid'
        if gate == '' or gate == '0':
            gate = 'gate'
        else:
            gate = f"'{gate}'"

        if GATETYPE == '' or GATETYPE == '0':
            GATETYPE = 'GATETYPE'
        else:
            GATETYPE = f"'{GATETYPE}'"


        if createdon == '' or createdon == '0':
            createdon = 'createdon between createdon and createdon'
        else:
            createdon = f"createdon between '{createdon} 00:00:01' and '{createdon} 23:59:59'"

        quary = gethealthstatusquary.format(typeid, gate, createdon,GATETYPE)
        result = ExecuteGetQuery(quary)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/getSwipetransaction')
def getSwipetransaction():
    try:
        bid = request.args.get('bid', default='bid')
        tickettype = request.args.get('tickettype', default='tickettype')
        gate = request.args.get('gate', default='gate')
        GATETYPE = request.args.get('gatetype', default='gatetype')
        bookingdate = request.args.get('bookingdate', default='bookingdate')

        if bid == '' or bid == '0':
            bid = 'bid'
        else :
            bid = f"'{bid}'"

        if gate == '' or gate == '0':
            gate = 'gate'
        else:
            gate = f"'{gate}'"

        if GATETYPE == '' or GATETYPE == '0':
            GATETYPE = 'GATETYPE'
        else:
            GATETYPE = f"'{GATETYPE}'"


        if tickettype == '' or tickettype == '0':
            tickettype = 'tickettype'
        else:
            tickettype = f" '{tickettype}' "

        if bookingdate == '' or bookingdate == '0':
            bookingdate = 'bookingdate'
        else:
            bookingdate = f" '{bookingdate}' "

        quary = getSwipetransactionquary.format(bid, tickettype, gate,GATETYPE,bookingdate)
        result = ExecuteGetQuery(quary)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run()
