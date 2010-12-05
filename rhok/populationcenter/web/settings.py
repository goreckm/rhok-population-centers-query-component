import os

port = os.environ['SERVER_PORT']
if port and port != '80':
    HOST_NAME = '%s:%s' % (os.environ['SERVER_NAME'], port)
else:
    HOST_NAME = os.environ['SERVER_NAME']

FT_URL = 'http://www.google.com/fusiontables'
FT_API_PATH = '/api/query'