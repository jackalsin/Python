
import pymysql.cursors

data = ["1001, 'Learning Python, 5th Edition', 'Mark Lutz', 40.89, 31",
        "1002, 'Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython', 'Wes McKinney', 25.24, 10",
        "1003, 'Python Cookbook', 'David Beazley, Brian K. Jones', 31.80, 100"]

def main():

    connection = pymysql.connect(host='128.2.76.186',
                                 user='12746',
                                 password='12746_CMU',
                                 db='12746',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            print "-" * 20 + " part a " + "-" * 20
            insertOriginalData(connection, cursor)
            print "-" * 20 + " part b " + "-" * 20
            selectTask(connection, cursor)
            print "-" * 20 + " part c " + "-" * 20
            updateTask(connection, cursor)
            print "-" * 20 + " part d " + "-" * 20
            deleteTask(connection, cursor)
    finally:
        connection.close()

def insertOriginalData(connection, cursor):
    sql = "INSERT INTO 12746_zxin VALUES (%s)"
    for dataChild in data:
        print sql % dataChild
        cursor.execute(sql % dataChild)
        connection.commit()

def selectTask(connection, cursor):
    sql = "SELECT Title, Quantity, Author FROM 12746_zxin WHERE Price<50 ORDER BY Price"
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    print result


def updateTask(connection, cursor):
    sql = "UPDATE 12746_zxin SET Quantity=9 WHERE Price<50"
    cursor.execute(sql)
    connection.commit()

def deleteTask(connection, cursor):
    sql = "DELETE FROM 12746_zxin WHERE Price<50"
    cursor.execute(sql)
    connection.commit()


if __name__ == '__main__':
    main()