from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("Test", "Test author")
        b.create_post("Test Post", "Test content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test content")

    def test_json_no_posts(self):
        b = Blog("Test", "Test author")
        expected = {
            'title': 'Test',
            'author': "Test author",
            "posts": []
                    }

        self.assertDictEqual(expected, b.json())

    def test_blog_json(self):
        b = Blog("Test", "Test author")
        b.create_post("Test Post", "Test content")
        b.create_post("Test Post 2", "Test content 2")
        expected = {
            'title': 'Test',
            'author': "Test author",
                    "posts":
                        [
                            {
                                'title': "Test Post",
                                'content': 'Test content'
                            },
                            {
                                'title': "Test Post 2",
                                'content': 'Test content 2'
                            }
                        ]
                    }

        self.assertEqual(len(b.posts), 2)
        self.assertDictEqual(expected, b.json())

