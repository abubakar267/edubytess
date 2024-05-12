import unittest
from main import app
from main import db  # Import your database object
from bson.objectid import ObjectId

class TestPostEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # Initialize your test database or use a testing database
        # Clear the forum collection before each test
        db.forum.delete_many({})

    def test_successful_post(self):
        # Mocking request data
        post_data = {
            "content": "Test content",
            "image": "test_image.jpg",
            "target": "IBA",
            "subject": "Computer Science",
            "tags": ["tag1", "tag2"]
        }
        response = self.app.post('/post', json=post_data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        # Check if the data is inserted into the database
        inserted_id = data['data']
        self.assertIsNotNone(db.forum.find_one({"_id": ObjectId(inserted_id)}))

    # Write other test cases for different scenarios (e.g., invalid JWT token, exceptions, etc.)

if __name__ == '__main__':
    unittest.main()
