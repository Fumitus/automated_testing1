from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Post Test was created by Test author. Test author has 0 posts.')
