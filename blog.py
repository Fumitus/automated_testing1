class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.post = []

    def __repr__(self):
        pass

    def create_post(self, title, content):
        pass

    def json(self):
        j_blog = {
            "title": self.title,
            "content": self.content,
        }
