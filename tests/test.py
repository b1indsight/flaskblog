import unittest
from flask import current_app
from ..app import create_app, db

class BlogTestCase(unittest.TestCase):

    def setUp():
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown():
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertIsNone(app)

    def test_login():
        respose = self.client.get('/login')
        data = respose.get_data(as_text=True)
        self.assertIN('', data)

