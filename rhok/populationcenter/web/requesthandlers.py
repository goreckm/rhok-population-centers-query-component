from google.appengine.ext import webapp
from google.appengine.api import users
from rhok.populationcenter.web import utilities
from rhok.populationcenter.web import settings
import urllib
import urllib2
import csv
from django.utils import simplejson as json
from google.appengine.api import urlfetch
import atom.url
import gdata.service
import gdata.alt.appengine
import logging

class FusionTableQuery(webapp.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            query = self.request.get('query')
            path = settings.FT_URL + settings.FT_API_PATH + '?' + urllib.urlencode({'sql': query})
            headers = {
            }
            
            logging.error('Error retrieving: ' + path)
            
            result = urlfetch.fetch(url=path,
                                    payload='',
                                    method=urlfetch.GET,
                                    headers=headers)

            if result.status_code == 200:
                logging.error(result.content)
                fileReader = csv.reader(result.content.split("\n"))
#                fileReader.next()
                jsonArray = [];
                for row in fileReader:

                    if len(row) == 0:
                        continue
                    
                    (city, population, latitude, longitude) = row
                    
                    # fix data
                    if len(longitude) == 0:
                        (latitude, longitude) = latitude.split(' ')
                    
                    logging.error("City:" + city + "\n")
                    logging.error("population:" + population + "\n")
                    logging.error("latitude:" + latitude + "\n")
                    logging.error("longitude:" + longitude + "\n")

                    jsonArray.append({ 'city': city, 
                                      'population': population, 
                                      'latitude': latitude, 
                                      'longitude': longitude});
                
                self.response.out.write(json.dumps(jsonArray))

            else:
                logging.error('Error retrieving: ' + path + "\nReturn Code: " + str(result.status_code))

class HomeHandler(webapp.RequestHandler):
    
    def get(self):
        user = users.get_current_user()
        if user:
            next_url = atom.url.Url('http', settings.HOST_NAME, path='/')
            template = utilities.render_template('home.html', { 'signoutUrl': users.create_logout_url(str(next_url)) });
            self.response.out.write(template)
        
        else:
            self.redirect(users.create_login_url(self.request.uri))
