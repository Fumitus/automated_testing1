from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("First blog message", "Andrius")

        self.assertEqual("First blog message", b.title)
        self.assertEqual("Andrius", b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog("Test title", "Test author")

        self.assertEqual(b.__repr__(), "Post Test title was created by Test author. Test author has 0 posts.")

    def test_repr_multi_posts(self):
        b = Blog("Test title 1", "Test author 1")
        b.posts = ["test1"]
        b2 = Blog("Test title 2", "Test author 2")
        b2.posts = ["test1", "one more"]

        self.assertEqual(b.__repr__(), "Post Test title 1 was created by Test author 1. Test author 1 has 1 post.")
        self.assertEqual(b2.__repr__(), "Post Test title 2 was created by Test author 2. Test author 2 has 2 posts.")
