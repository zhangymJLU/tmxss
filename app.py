__author__ = 'ym1ng'
import os
import tornado.ioloop
import tornado.web
import ConfigParser
from model import *

config = ConfigParser.ConfigParser()


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')

    def get_all_input(self):
        data = {}
        for key in self.request.arguments:
            data[key] = self.get_argument(key)
        return data


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render()


class ResultListHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write()


class ResultDetailHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pass


class ReceiveRequestHandler(BaseHandler):
    def get(self):
        input = self.get_all_input()

    def post(self):
        self.get()


class LoginHandler(BaseHandler):
    def get(self):
        self.write('login')

    def post(self):
        input = self.get_all_input()
        username = input.get('username')
        password = input.get('password')
        user = User.filter(username=username)
        ret = user.login(password)
        if ret:
            self.set_secure_cookie('user', self.get_argument('username'))
            self.redirect('/')
        else:
            self.redirect('/login')




settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret': config.get('tornado', 'cookie_secret'),
    'login_url': '/login'

}


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    (r'/resultlist', ResultListHandler),
    (r'/resultdetail', ResultDetailHandler),
    (r'/recive', ReceiveRequestHandler),
], **settings)


if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
