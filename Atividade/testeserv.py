from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

hostName = "127.0.0.1"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        
    def do_GET(self):     
        self._set_response()
        self.wfile.write("fr".format(self.path).encode('utf-8'))
        self.wfile.write(input('R=').format(self.path).encode('utf-8'))
            

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        print(str(self.rfile.read(length), "utf-8"))

        response = bytes(input('R: '), "utf-8") #create response
        
        self._set_response()

        self.wfile.write(response) #send response

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
