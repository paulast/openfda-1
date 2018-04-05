import http.server
import socketserver

PORT = 8000


class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        mensaje += "<p>" + "Información medicamento" + "</p>"
        for a in nombre:
            mensaje += a + "<br>"
        mensaje += "<ul>"
        mensaje += "<li>Recurso solicitado: {}</li>".format(self.path)
        mensaje += "</ul>"
        mensaje += "</body>"
        mensaje += "</html>"

        
        self.wfile.write(bytes(mensaje, "utf8"))
        return

Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("Sirviendo en puerto: {}".format(PORT))


try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Servidor detenido")
    httpd.server_close()

