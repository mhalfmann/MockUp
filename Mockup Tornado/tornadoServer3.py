import os
import tornado.ioloop
import tornado.web

root = os.path.join(os.path.dirname(__file__),"static")
port = 8889

application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "indexD3.htm"})
])

if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()