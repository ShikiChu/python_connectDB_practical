from mysql.connector import MySQLConnection, Error
from mySqlDbConfig import readDbConfig


def queryFetchone():
    try:
        dbconfig = readDbConfig()
        # return a dictionary of db configuration
        # dbconfig: {'host': 'localhost', 'database': 'world', 'user': 'root', 'password': '*********'}

        conn = MySQLConnection(**dbconfig)
        # use this dictionary info to create a new connection object "conn"
        # conn: <mysql.connector.connection.MySQLConnection object at 0x10262f8b0>

        cursor = conn.cursor()
        # create a new constructor "cursor()" in the object

        cursor.execute("SELECT * FROM city LIMIT 10")
        # send the query to this cursor
        # return all the records in the memory
        # {tuple:5} ('ID','Name','CountryCode','District','Population')

        row = cursor.fetchone()
        # fetch the first result in that memory
        # row: (1, 'Kabul', 'AFG', 'Kabol', 1780000)

        print("<table>")
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0], row[1], row[2], row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    queryFetchone()

