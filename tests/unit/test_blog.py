from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("First blog message", "Andrius")

        self.assertEqual("First blog message", b.title)
        self.assertEqual("Andrius", b.author)
        self.assertListEqual([], b.post)
