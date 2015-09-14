__author__ = 'ym1ng'
import os
import tornado.ioloop
import tornado.web
import ConfigParser
import tornado.autoreload
from model import *

_config = ConfigParser.ConfigParser()
_config.read('config.ini')


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        username = self.get_secure_cookie('username')
        if User.filter(username=username):
            return True
        else:
            return False

    def get_all_input(self):
        data = {}
        for key in self.request.arguments:
            data[key] = self.get_argument(key)
        return data


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('main.html')


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
        username = input.get('username')
        result = Result(username=username, result=input)
        result.save()
        print input

    def post(self):
        self.get()


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        input = self.get_all_input()
        username = input.get('username')
        password = input.get('password')
        user = User.filter(username=username)
        if user:
            ret = user.login(password)
        else:
            ret = None
        if ret:
            self.set_secure_cookie('username', self.get_argument('username'))
            self.redirect('/')
        else:
            self.redirect('/login')




settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret': _config.get('tornado', 'cookie_secret'),
    'login_url': '/login',
    'debug': True
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
