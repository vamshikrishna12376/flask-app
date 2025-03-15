import unittest
from app import create_app

class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test client before tests."""
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_home_route(self):
        """Test the home route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, CI/CD!")

    def test_not_found_route(self):
        """Test a non-existent route (should return 404)."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
