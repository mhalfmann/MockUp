import Settings
import tornado.web
import tornado.httpserver


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
        }
        application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "indexD3.htm"})
])


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("indexD3.htm")


def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(8889)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()