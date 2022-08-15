from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")# Ask user for author name
        self.user_blog = None
        if self._user_has_account():
            print("Welcome Back {}!".format(self.user))# Check if they've already got an account
        else:
            self._prompt_user_for_account()
        # If not, prompt them to create one
        pass

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author' : self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read(R) or write (W) blogs? ")# User read of write blogs
        if read_or_write == 'R':# If read:
            self._list_blogs() # list blogs in database
            self._view_blog() # allow user to pick one and then display posts
            pass
        elif read_or_write == 'W': # If write:
            self.user_blog.new_post() # Prompt to write a post
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                                query= {})
        for blog in blogs:
                print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = ("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {},\n\n{}".format(post['created_date'], post['title'], post['content']))

