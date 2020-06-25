import web_server
# Module for Test Coverage for Application
import unittest

# Smallest Unit of Testing to check for specific response to input
class TestHelloWorld(unittest.TestCase):
    # Runs immediately
    def setUp(self):
        self.app = web_server.app.test_client()
        self.app.testing = True

    # Checks for successful get request
    def test_status_code(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    # Checks that message by app by test is the same
    def test_message(self):
        response = self.app.get("/")
        message = web_server.wrap_html("Hello Docker Peeps")
        # Convert Byte Data to String to fix Line Breaks
        self.assertEqual(response.data.decode("utf-8"), message)

if __name__ == "__main__":
    unittest.main()