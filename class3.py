from abc import ABC, abstractmethod
import sqlite3

class ConsoleInterface(ABC):

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def display_output(self, output):
        pass


class MyConsoleClass(ConsoleInterface):

    def get_input(self):
        user_input = input("Введите Ваше имя: ")
        return user_input

    def display_output(self, output):
        print("Result:", output)

console_obj = MyConsoleClass()
user_input = console_obj.get_input()
console_obj.display_output("Привет " + user_input + ")")




class EmailClient(ABC):

    @abstractmethod
    def send_email(self, recipient, subject, message):
        pass

    @abstractmethod
    def receive_email(self):
        pass

class MockEmailClient(EmailClient):

    def __init__(self):
        self.received_emails = []

    def send_email(self, recipient, subject, message):
        print(f"Отправка email на {recipient} с темой '{subject}' и сообщением '{message}'")

    def receive_email(self):
        print("Получение всех новых email")
        return self.received_emails

    def add_received_email(self, email):
        self.received_emails.append(email)



email_client = MockEmailClient()
email_client.send_email("example@example.com", "Привет", "Привет, как дела?")
email_client.add_received_email("Новое сообщение: Привет от example@example.com")
received_emails = email_client.receive_email()
print(received_emails)
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


class Controller:
    def __init__(self):
        self.db = Database("login", "password", "result", "error")
        self.console = MyConsoleClass()
        self.email_client = MockEmailClient()

    def execute_operation(self):
        user_input = self.console.get_input()
        self.db.login = user_input
        self.db.readFromDatabase()
        result = self.db.result

        if not result:
            self.calculate_result()
            self.db.addToDatabase()
        else:
            self.result = self.db.result

        self.send_result_to_external_dependency()

        return self.result

    def calculate_result(self):
        self.result = "Result"

    def send_result_to_external_dependency(self):
        self.email_client.send_email("example@example.com", "Result", self.result)

