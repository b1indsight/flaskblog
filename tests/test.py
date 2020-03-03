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
        self.client.post('/login', data=dict(
            username='123', 
            password='123'), follow.redirects=TRUE)
        data = respose.get_data(as_text=True)
        self.assertIN('success', data)

    def test_logout():
        respose = self.client.get('/logout')
        data = respose.get_data(as_text=True)
        self.assertIN('index.html',data)

    def test_404():
        respose = self.client.get('/nothing')
        data = respose.get_data(as_text=True)
        self.assertIN('get 404',data)
        self.assertIN('Page not found',data)
