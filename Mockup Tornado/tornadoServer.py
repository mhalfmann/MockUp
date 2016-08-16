import tornado.ioloop
import tornado.web

import os.path

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('indexVis.htm'
		)
		
settings = dict(
		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		debug=True
)

application = tornado.web.Application([
	(r"/",MainHandler)
],**settings)

if __name__== "__main__":
	print("Server Running ...")
	print("Press ctrl + c to close")
	application.listen(8889)
	tornado.ioloop.IOLoop.instance().start()