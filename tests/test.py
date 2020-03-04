import unittest
from flask import current_app
from app import create_app, db

class BlogTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(self.app is None)

    def test_login(self):
        respose = self.client.post('/login', data=dict(
            username='123', 
            password='123'
            ), follow_redirects=True)
        data = respose.get_data(as_text=True)
        self.assertIn('logout', data)

        

    def test_logout(self):
        respose = self.client.get('/logout', follow_redirects=True)
        data = respose.get_data(as_text=True)
        self.assertIn('login',data)

    def test_404(self):
        respose = self.client.get('/nothing')
        data = respose.get_data(as_text=True)
        self.assertIn('get 404',data)
        self.assertIn('Page not found',data)

if __name__=="__main__":
    unittest.main()