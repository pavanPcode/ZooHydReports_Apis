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

