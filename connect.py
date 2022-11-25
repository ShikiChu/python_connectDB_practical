import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='world',
                                       user='root',
                                       password='59*******')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    connect()
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# 它是样板代码（boilerplate code），可防止用户在无意中意外调用脚本。
# 当执行connect.py这个模块时（作为主程序）, 特殊变量__name__ is initiated to '__main__' , in which case this statement is true, so execute connect()
# 当import connect.py时， it will assign the name "connect" from the import statement to the __name__ variable,
# i.e. __name__ = "connect", 它就不再是'__main__', so NOT execute connect(), nothing will happen
