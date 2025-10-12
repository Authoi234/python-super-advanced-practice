import base64
from dataclasses import dataclass
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

@dataclass
class Car:
    car_id: str
    name: str
    manufacturer: str
    year: int
    price: int

car_db = dict()
HOST, PORT = "localhost", 8888

class SimpleServer(SimpleHTTPRequestHandler):

    def _send_400(self, msg=''):
        self.send_response(400)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(msg.encode())

    def _send_200(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _send_unauthorized(self, msg=''):
        self.send_response(400)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(msg.encode())

    @classmethod
    def set_api_key(cls, username, password):
        key_str = "{}:{}".format(username, password)
        cls.key = base64.b64encode(key_str.encode()).decode()
    
    def check_authorized(func):
        def check(self):
            api_key = self.key
            if self.headers.get("Authorization") == None:
                return self._send_unauthorized("Missing Auth Header")
            elif self.headers.get("Authorization") != "Basic {}".format(api_key):
                return self._send_unauthorized("Wrong username/password")
            func(self)
        return check
        

    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = parse_qs(parsed_url.query)
        if "id" not in qs or len(qs["id"]) == 0 :
            self._send_400("Id missing")
            return
        
        car_id = qs["id"][0]
        if car_id not in car_db:
            self._send_400("Id not found")
            return
        
        car = car_db[car_id]
        
        self._send_200()
        details = "Car Name: {}<br />Manufacturer: {}<br />Year: {}"
        details += "<br />Price: {}<br />"
        details = details.format(car.name, car.manufacturer, car.year, car.price)

        html_content = f"""
            <html lang="en">

            <head>
                <link rel="shortcut icon"
                    href="https://icons.iconarchive.com/icons/icons-land/vista-hardware-devices/256/Home-Server-icon.png"
                    type="image/x-icon">
                <title>Authoi Server</title>
            </head>

            <body>
                {details}
            </body>
            </html>
        """
        self.wfile.write(html_content.encode())

    @check_authorized
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        req_data = self.rfile.read(content_length)
        
        try:
            c = json.loads(req_data)
            car = Car((c["id"]), c["name"], c["manufacturer"], c["year"], c["price"])
            car_db[car.car_id] = car
        except KeyError:
            self._send_400("Missing required field(s)")
            return
        
        self._send_200()

    @check_authorized
    def do_DELETE(self):
        car_id = self.path.removeprefix('/delete/')
        if car_id not in car_db:
            self._send_400("Id not found")
            return
        
        del car_db[car_id]
        self._send_200()

    @check_authorized
    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        req_data = self.rfile.read(content_length)

        try:
            c = json.loads(req_data)
            if "id" not in c:
                self._send_400("Id missing")
                return
            car = car_db[c["id"]]

            for key in c:
                car.__setattr__(key, c[key])
            car_db[car.car_id] = car
        except KeyError:
            self._send_400("Invalid field(s)")
            return
        
        self._send_200()
        self.wfile.write(b'Car updated')
        return
    
    @check_authorized
    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        req_data = self.rfile.read(content_length)

        try:
            c = json.loads(req_data)
    
            if "id" not in c:
                self._send_400("Id missing")
                return

            car_id = c["id"]

            if car_id not in car_db:
                self._send_400("Id not found")
                return

            try:
                new_car = Car(
                    car_id,
                    c["name"],
                    c["manufacturer"],
                    c["year"],
                    c["price"]
                )
            except KeyError:
                self._send_400("Missing required field(s)")
                return

            car_db[car_id] = new_car

        except json.JSONDecodeError:
            self._send_400("Invalid JSON")
            return

        self._send_200()
        self.wfile.write(b'Car replaced')


if __name__ == "__main__":
    simple_server = HTTPServer((HOST, PORT), SimpleServer)
    SimpleServer.set_api_key("dimik","python")
    print("Starting Server ...\n")
    try:
        simple_server.serve_forever()
    except KeyboardInterrupt:
        pass

    simple_server.server_close()
    print("[SHUTTING DOWN] Server shutting down ...")