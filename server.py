# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
serverPort = 8080

ok_response = bytes( json.dumps( [
    { 'verdict': 'Accepted', 'time': 0, 'memory': 250 }
] * 20 ), "utf-8" )

class MyServer( BaseHTTPRequestHandler ):
    def do_GET( self ):
        self.send_response( 200 )
        self.send_header( "Content-type", "text/json" )
        self.end_headers()
        self.wfile.write( ok_response )

if __name__ == "__main__":        
    webServer = HTTPServer( (hostName, serverPort), MyServer )
    print( f"Server started http://{hostName}:{serverPort}" )

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print( "Server stopped." )

