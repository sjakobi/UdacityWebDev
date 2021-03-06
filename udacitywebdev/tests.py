import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from udacitywebdev.views import hello_udacity
        request = testing.DummyRequest()
        response = hello_udacity(request)
        self.assertEqual(response["title"], "Hello, Udacity!")


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from udacitywebdev import main
        settings = {}
        app = main(settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get("/", status=200)
        self.assertIn(b"Hello, Udacity!", res.body)
