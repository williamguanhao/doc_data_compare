import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
import os
from data_loader import get_data_by_id, extract_fields_from_pdf

PORT = 8000
STATIC_DIR = "static"
PDF_DIR = "pdfs"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == "/get_pdf":
            query = parse_qs(parsed_path.query)
            doc_id = query.get("doc_id", [""])[0]
            file_path = os.path.join(PDF_DIR, f"{doc_id}.pdf")
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header("Content-type", "application/pdf")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "PDF not found")
        elif parsed_path.path == "/get_data":
            query = parse_qs(parsed_path.query)
            data_id = query.get("data_id", [""])[0]
            data = get_data_by_id(data_id)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif parsed_path.path == "/extract_fields":
            query = parse_qs(parsed_path.query)
            doc_id = query.get("doc_id", [""])[0]
            df = extract_fields_from_pdf(doc_id)
            result = df.to_dict(orient="records")  # Convert DataFrame to list of dicts
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
