import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from class3 import Controller, Database, MyConsoleClass, MockEmailClient

class IntegrationTest(unittest.TestCase):
    def test_execute_operation(self):
        db = Database("login", "password", "result", "error")
        console = MyConsoleClass()
        email_client = MockEmailClient()
        controller = Controller()
        mock_input = "John"
        expected_output = "Result: Result"
        # Set up the mock email client
        email_client.add_received_email("Новое сообщение: Привет от example@example.com")
        # Patch the input and output methods
        with patch("builtins.input", return_value=mock_input), \
             patch("sys.stdout", new=StringIO()) as mock_stdout:
            # Execute the operation
            result = controller.execute_operation()
            # Assert the result and output
            self.assertEqual(result, "Result")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
            # Assert the email client
            self.assertEqual(email_client.received_emails, ["Новое сообщение: Привет от example@example.com"])

    def test_execute_operation_existing_result(self):
        db = Database("login", "password", "existing_result", "error")
        console = MyConsoleClass()
        email_client = MockEmailClient()
        controller = Controller()
        mock_input = "John"
        expected_output = "Result: existing_result"
        # Set up the mock email client
        email_client.add_received_email("Новое сообщение: Привет от example@example.com")
        # Patch the input and output methods
        with patch("builtins.input", return_value=mock_input), \
             patch("sys.stdout", new=StringIO()) as mock_stdout:
            # Execute the operation
            result = controller.execute_operation()
            # Assert the result and output
            self.assertEqual(result, "existing_result")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
            # Assert the email client
            self.assertEqual(email_client.received_emails, ["Новое сообщение: Привет от example@example.com"])

    def test_execute_operation_no_result(self):
        db = Database("login", "password", "", "error")
        console = MyConsoleClass()
        email_client = MockEmailClient()
        controller = Controller()
        mock_input = "John"
        expected_output = "Result: Result"
        # Set up the mock email client
        email_client.add_received_email("Новое сообщение: Привет от example@example.com")
        # Patch the input and output methods
        with patch("builtins.input", return_value=mock_input), \
             patch("sys.stdout", new=StringIO()) as mock_stdout:
            # Execute the operation
            result = controller.execute_operation()
            # Assert the result and output
            self.assertEqual(result, "Result")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
            # Assert the email client
            self.assertEqual(email_client.received_emails, ["Новое сообщение: Привет от example@example.com"])

class TestController(unittest.TestCase):
    def test_execute_operation_new_result(self):
        db = MagicMock()
        db.result = ""
        console = MagicMock()
        console.get_input.return_value = "John"
        email_client = MagicMock()
        controller = Controller(db, console, email_client)

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            result = controller.execute_operation()

            self.assertEqual(result, "result")
            self.assertEqual(mock_stdout.getvalue().strip(), "Result: result")
            db.addToDatabase.assert_called_once()
            email_client.send_email.assert_called_once_with("example@example.com", "Result", "result")

    def test_execute_operation_existing_result(self):
        db = MagicMock()
        db.result = "existing_result"
        console = MagicMock()
        console.get_input.return_value = "John"
        email_client = MagicMock()
        controller = Controller(db, console, email_client)

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            result = controller.execute_operation()

            self.assertEqual(result, "existing_result")
            self.assertEqual(mock_stdout.getvalue().strip(), "Result: existing_result")
            db.addToDatabase.assert_not_called()
            email_client.send_email.assert_called_once_with("example@example.com", "Result", "existing_result")

if __name__ == '__main__':
    unittest.main()