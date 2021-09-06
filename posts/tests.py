from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Posts

# Create your tests here.
class PostssTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='9919')
        testuser1.save()
        test_post = Posts.objects.create(author=testuser1, title='hello', description='greeting' )
        test_post.save()

    def test_blog_content(self):
        post = Posts.objects.get(id =1)
        expected_author = f'{post.author}'
        expected_Poststitle = f'{post.title}'
        expected_description = f'{post.description}'
        self.assertEqual(expected_author,'testuser1')
        self.assertEqual(expected_Poststitle,'hello')
        self.assertEqual(expected_description,'greeting')