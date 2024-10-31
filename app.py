from flask import Flask, jsonify
import unittest

# Create the Flask app
app = Flask(__name__)

# Define the route
@app.route('/')
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")

# Define the unit test class
class TestMyApp(unittest.TestCase):
  
 # Set up a test client
    def setUp(self):
        self.app = app.test_client()

  # Test the home route
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Hello level 400 FET, Quality Assurance!'})

    if __name__ == '__main__':
        app.run(debug=True)
        unittest.main()