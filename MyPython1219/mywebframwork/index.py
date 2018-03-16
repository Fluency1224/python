#/usr/bin/env python
#coding:utf-8

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):



    
    start_response('200 OK', [('Content-Type', 'texst/html')])
    return '<h1>From Python3 Web by Fleuncy!</h1>'


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print('Server HTTP on port 8000...')
    httpd.serve_forever()