import http.server
import socketserver
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port",required=True, type=int, help="Run the server on a specific port")
args = parser.parse_args()
PORT = int(args.port)

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Python HTTP Handler!</h1>")
        self.wfile.write(f"<p>You requested: {self.path}</p>".encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.path
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>POST Received!</h1>")
        self.wfile.write(b"<p>Data received:</p>")
        self.wfile.write(f"<p>Requested path: {self.path}</p>".encode())
        self.wfile.write(f"<pre>{post_data.decode()}</pre>".encode())



Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()