from http.server import BaseHTTPRequestHandler, HTTPServer
from interface import *
import logging

hostName = "127.0.0.1"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        return self.end_headers()


    def do_GET(self):
        self._set_response()
        self.wfile.write("fr".format(self.path).encode('utf-8'))
        #self.wfile.write(input('ENVIA do serv =').format(self.path).encode('utf-8'))

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        msg = str(self.rfile.read(length), 'utf-8')
        cabecalho("\033[32mMENSAGEM RECEBIDA (CLIENTE)> \033[m" + f'\033[32m{msg}\033[m')
        #print()
        linha(len('MENSAGEM RECEBIDA (CLIENTE)> ') + len(msg))

        response = bytes(input('\033[34mENVIAR MENSAGEM VIA SERVIDOR> \033[m'), "utf-8")  # create response

        self._set_response()
        self.wfile.write(response)# send response


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    #print("Server started http://%s:%s" % (hostName, serverPort))
    #print(f"Serv Started http:// {hostName}: {serverPort}")
    linha(20)
    cabecalho(f"\033[35m SERVIDOR INICIADO\n  {hostName}:{serverPort}\033[m")
    linha(20)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
