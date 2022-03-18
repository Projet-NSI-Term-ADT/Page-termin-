#!/export/home/mermet/anaconda3/bin/python
# -*- coding: utf-8 -*-
# à mettre dans chacun des scripts :
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
import http.server
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler

PORT = 8888
server_address = ("", PORT)

handler.cgi_directories = ["/"]

print("Serveur actif sur le port :", PORT)
print("Starting server. Ctrl+C to quit.")
print("http://localhost:8888/index_login.py")

httpd = server(server_address, handler)
httpd.serve_forever()

