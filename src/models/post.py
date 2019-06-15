import uuid
from src.common.database import Database
import datetime

class Post(object):

    def __init__(self, blog_id,  title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        if _id is None:
            self._id = uuid.uuid4().hex
            # uuid.uuid4() generates a random uid. hex generates a 32 chars hexadecimal string
        else:
            self._id = _id

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            '_id' : self._id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        # return a specific post from a query of post id
        post_data = Database.find_one('posts', {'_id' : id})
        return cls(**post_data)
        # return cls(blog_id=post_data["blog_id"],
        #            author=post_data["author"],
        #            content=post_data["content"],
        #            title=post_data["title"],
        #            created_date=post_data["created_date"],
        #            _id=post_data['_id'])


    @staticmethod
    def from_blog(id):
        #Return a list of posts from a query of blog id
        return [post for post in Database.find('posts', {'blog_id' : id})]