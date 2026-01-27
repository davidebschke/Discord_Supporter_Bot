

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

# 1. Ein Mini-Webserver für Render
def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# 2. Dein Bot-Logik
print("Bot startet...")



if __name__ == "__main__": # pragma: no cover
    print("Hello World") # pragma: no cover