from django.test import TestCase

class TestYourViews(TestCase):
    def test_index_view(self):
        response = self.client.get('/', follow=True)
        # Check the final status code after following the redirect
        self.assertEqual(response.status_code, 200)
