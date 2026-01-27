

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

# 1. Ein Mini-Webserver für Render
def run_server(): # pragma: no cover
    port = int(os.environ.get("PORT", 10000))# pragma: no cover
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)# pragma: no cover
    server.serve_forever()# pragma: no cover

threading.Thread(target=run_server, daemon=True).start()# pragma: no cover

# 2. Dein Bot-Logik
print("Bot startet...")# pragma: no cover



if __name__ == "__main__": # pragma: no cover
    print("Hello World") # pragma: no cover