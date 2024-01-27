import mysql.connector



db_config = {
        'host': 'MYSQL5048.site4now.net',
        'user': 'a50d85_payroll',
        'password': 'p3r3nnial',
        'database': 'db_a50d85_payroll',
    }


def ExecuteUpdate(quary):
    connection = mysql.connector.connect(**db_config)
    if connection:
        cursor = connection.cursor()
        cursor.execute(quary)
        connection.commit()
        cursor.close()
        connection.close()

import mysql.connector

def ExecuteGetQuery(Quary):
    ResultModel = {'Status': False, 'Message': None, 'ResultData': []}
    total_data_to_list = []

    try:
        try:
            # Update connection details for MySQL
            db_connection  = mysql.connector.connect(**db_config)
            cursor = db_connection.cursor()

            # Execute the query
            cursor.execute(Quary)

        except mysql.connector.Error as e:
            ResultModel['Message'] = str(e)
            ResultModel['Status'] = False
            ResultModel['ResultData'] = []
            return ResultModel

        if cursor.with_rows:
            try:
                total_data = cursor.fetchall()

                if len(total_data) == 0:
                    ResultModel['Message'] = 'No Records Found.'
                    ResultModel['Status'] = False
                    ResultModel['ResultData'] = total_data_to_list

                    cursor.close()
                    db_connection.close()
                    return ResultModel

                for j in range(len(total_data)):
                    count = 0
                    dict_data = {}

                    for i in cursor.description:
                        dict_data[str(i[0]).lower()] = total_data[j][count]
                        count += 1
                    total_data_to_list.append(dict_data)

                ResultModel['Status'] = True
                ResultModel['Message'] = None
                ResultModel['ResultData'] = total_data_to_list

                cursor.close()
                db_connection.close()
                return ResultModel

            except mysql.connector.Error as e:
                ResultModel['Status'] = False
                ResultModel['Message'] = str(e)
                ResultModel['ResultData'] = []
                cursor.close()
                db_connection.close()
                return ResultModel

        else:
            # Handle the case where the cursor doesn't have rows (e.g., for non-SELECT queries)
            ResultModel['Status'] = True
            ResultModel['Message'] = "Query executed successfully."
            ResultModel['ResultData'] = []

            cursor.close()
            db_connection.close()
            return ResultModel

    except mysql.connector.Error as e:
        ResultModel['Status'] = False
        ResultModel['Message'] = str(e)
        ResultModel['ResultData'] = []
        return ResultModel
