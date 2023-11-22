import sqlite3

class Database:
    def __init__(self,login:str, password:str, result:str, error:str) -> None:
        self.login = login
        self.password = password
        self.result = result
        self.error = error

    def addToDatabase(self):
        try:
            sqlite_connection = sqlite3.connect('laba.db')
            cursor = sqlite_connection.cursor()


            sqlite_insert_with_param = """INSERT INTO userinfo
                             (login,password,passrepeat,authorizationresult,erroormessage)
                             VALUES ( ?, ?,? ,?, ?);"""

            data_tuple = (str(self.login),str(self.password),str(self.password),(self.result),(self.error))
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqlite_connection.commit()


            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")



    def removeFromDatabase(self):
        try:
            sqlite_connection = sqlite3.connect('laba.db')
            cursor = sqlite_connection.cursor()


            sqlite_remove_query = """DELETE FROM userinfo WHERE login = ?;"""

            data_tuple = (self.login,)
            cursor.execute(sqlite_remove_query, data_tuple)
            sqlite_connection.commit()


            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")



    def readFromDatabase(self):
        try:
            sqlite_connection = sqlite3.connect('laba.db')
            cursor = sqlite_connection.cursor()


            sqlite_select_query = """select * from userinfo where login = ?;"""

            data_tuple = (self.login,)
            cursor.execute(sqlite_select_query, data_tuple)
            result = cursor.fetchall()
            sqlite_connection.commit()
            print(result)


            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")



test =Database("123","123","ok","nth")
test.addToDatabase()
test.readFromDatabase()


