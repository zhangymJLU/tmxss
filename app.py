__author__ = 'ym1ng'
import os
import tornado.ioloop
import tornado.web
import ConfigParser


config = ConfigParser.ConfigParser()


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write('test')



class ResultListHandler(BaseHandler):
    def get(self):
        self.write()


class ResultDetailHandler(BaseHandler):
    def get(self):
        pass


class LoginHandler(BaseHandler):
    def get(self):
        self.write('login')

    def post(self):
        self.set_secure_cookie('user', self.get_argument('username'))


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    'cookie_secret': config.get('tornado', ''),
    'login_url': '/login'

}


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/login', LoginHandler),
],**settings)


if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()