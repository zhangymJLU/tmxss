__author__ = 'ym1ng'
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write('test')


class LoginHandler(BaseHandler):
    def get(self):
        self.write('login')

    def post(self):
        self.set_secure_cookie('user',self.get_argument('name'))

settings = {
    'cookie_secret': '123456789',
    'login_url': '/login'

}
application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/login', LoginHandler),
],**settings)


if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()