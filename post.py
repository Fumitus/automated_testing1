class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        j_post = {
            "title": self.title,
            "content": self.content,
        }
        return j_post
