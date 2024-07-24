'''
3. Basic Web Server

Create a simple web server that can serve HTML files.

Task:

    Accept incoming HTTP requests.
    Respond with the contents of an HTML file.
    Handle basic GET requests.

Hint: Use the http.server module.
'''

import http.server
import socketserver

'''
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_file_path = "index.html"

        try:
            with open(html_file_path, 'r') as file:
                html_content= file.read()
                self.wfile.write(html_content.encode())
        except FileNotFoundError:
            self.send_response(400)
            self.wfile.write(b"File Not Found")


def run(server_class=http.server.HTTPServer, handler_class= MyRequestHandler, port=8080):
    server_address= ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'[*] Starting the Server on port {port}...')
    httpd.serve_forever()

if __name__=="__main__":
    run()

'''

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

port = 8000

with socketserver.TCPServer(("",port),MyRequestHandler) as httpd:
    print(f"[*] Serving HTTP on port {port}...")
    httpd.serve_forever()
