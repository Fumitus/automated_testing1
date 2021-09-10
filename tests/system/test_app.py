from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {'Test': blog}

    def test_menu_print_blogs(self):
        expected = '- Post Test was created by Test author. Test author has 0 posts.'
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch('builtins.print') as mocked_print:
                app.menu()

                mocked_print.assert_called_with(expected)

    def test_menu_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test', 'Test author', 'q')
            app.menu()

            self.assertIsNotNone(app.blogs['Test'])

    def test_menu_ask_read_blog(self):
        blog = app.blogs['Test']
        blog.create_post('Test menu post', 'Test menu content')
        expected = "Title ---Test menu post---" \
                   "" \
                   "Content Test menu content"\
                   ""
        with patch('builtins.input') as mocked_inputs:
            mocked_inputs.side_effect = ('r', 'Test', 'q')
            with patch('builtins.print') as mocked_print:
                app.menu()

                mocked_print.assert_called_with(expected)

    def test_menu_ask_create_post(self):
        with patch('builtins.input') as mocked_inputs:
            mocked_inputs.side_effect = ('p', 'Test', 'Test post', 'Test content', 'q')
            app.menu()

            self.assertEqual('Test post', app.blogs['Test'].posts[0].title)
            self.assertEqual('Test content', app.blogs['Test'].posts[0].content)


    def test_menu_exit(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_once_with(app.MENU_PROMPT)


    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_print_blogs_prompt(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()


    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Post Test was created by Test author. Test author has 0 posts.')


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))


    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test', 'Test content')
        with patch('app.print_post') as moked_print_posts:
            app.print_posts(blog)

            moked_print_posts.assert_called_with(blog.posts[0])

    def test_print_post(self):
        expected = "Title ---Test title---" \
                   "" \
                   "Content Test content"\
                   ""
        post = Post('Test title', 'Test content')
        with patch('builtins.print') as mocked_print_post:
            app.print_post(post)

            mocked_print_post.assert_called_with(expected)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_inputs:
            mocked_inputs.side_effect = ('Test', 'First post', 'First post content')

            app.ask_create_post()

            self.assertEqual('First post', app.blogs['Test'].posts[0].title)
            self.assertEqual('First post content', app.blogs['Test'].posts[0].content)
