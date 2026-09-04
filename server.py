"""
ZoneMemo AI - Local Development Server
Run: python server.py
Then open http://localhost:8000 in your web browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[ZoneMemo Server] {self.address_string()} - {format % args}")

def main():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("🚀 ZoneMemo AI Web Platform is running locally!")
        print(f"👉 Local URL: http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        print("=" * 60)
        try:
            # Auto-open browser
            webbrowser.open(f"http://localhost:{PORT}")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down ZoneMemo server. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
