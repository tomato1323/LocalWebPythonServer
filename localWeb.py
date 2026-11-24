import http.server
import socketserver

import webbrowser
import threading
import time

PORT = 8000
URL = f"http://localhost:{PORT}"

def open_brower():
    time.sleep(1)
    webbrowser.open(URL)

if __name__ == "__main__":
    print("サーバー起動")
    threading.Thread(target=open_brower, daemon=True).start()
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("受信ポート: ", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n Server stop")