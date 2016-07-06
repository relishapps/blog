from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('a', 'a@a.com', 'a')

    def test_string_representation(self):
        post = Post(author=self.user,
                    title='My first post',
                    slug='my-first-post',
                    body='Humpty Dumpty sat on a wall. Humpty Dumpty had a great fall. All of the King\'s horses, and all of the King\'s men, could\'nt put Humpty together again!')
        self.assertEqual(str(post), post.title)
