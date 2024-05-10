from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        # Set headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # HTML content to be served
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Sample Page</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTTP server example.</p>
        </body>
        </html>
        """
        
        # Send the HTML response
        self.wfile.write(html_content.encode('utf-8'))

# Define the main function to start the HTTP server
def run():
    # Server address (localhost) and port
    server_address = ('127.0.0.1', 8000)
    # Create an HTTP server with our custom handler
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running at http://{server_address[0]}:{server_address[1]}/")
    # Start the HTTP server
    httpd.serve_forever()

# Run the main function if the script is executed directly
if __name__ == '__main__':
    run()
