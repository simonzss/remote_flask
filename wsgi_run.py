
# encoding = 'utf-8'
#
# def application(environ,start_response):
#    status = "200 Ok"
#    output = b"Hello wsgi"
#    response_headers=[('Content-type','text/plain'),('Content-Length',str(len(output)))]
#    start_response(status,response_headers)
#    return [output]

import sys

flaskPath = 'D:\\PycharmProjects\\flask_first'


if flaskPath not in sys.path:
    sys.path.insert(0, 'D:\\PycharmProjects\\flask_first')


from manage import app


application = app