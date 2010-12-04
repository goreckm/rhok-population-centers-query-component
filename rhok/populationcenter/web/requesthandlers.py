from google.appengine.ext import webapp
from rhok.populationcenter.web import utilities

class HomeHandler(webapp.RequestHandler):
    
    def get(self):
        template = utilities.render_template('home.html');
        self.response.out.write(template)
        