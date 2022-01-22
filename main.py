import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database= 'sql_transaction'
)
#
#

try:

    db.autocommit = False
    cur = db.cursor(dictionary=True)

    # Operation 1. Increase the salary of Seniors Developers by 20%
    query = "UPDATE data SET salary = salary * 1.2 where seniority = 'Senior'"
    cur.execute(query)

    # Operation 2. Increase the salary of Juniors Developers by 10%
    query2 = "UPDATE data SET salary = salary * 1.1 where seniority = 'Junior'"
    cur.execute(query2)

    print("Salries Increased Successfully")
    db.commit()
except mysql.connector.Error as error:
    print("Transaction Failed")
    db.rollback()
finally:
    if db.is_connected():
        db.close()
        print("Connection closed")

