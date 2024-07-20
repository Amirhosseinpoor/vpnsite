import base64
import json
from urllib.parse import urlparse, parse_qs


class Extractor:
    def __init__(self, link):
        self.link = link
        if self.link.startswith('vmess://'):
            self.output = self.vmessextractor(self.detector(self.link))

        elif self.link.startswith('vless://'):
            self.output = self.vlessextractor(self.detector(self.link))

        else:
            self.output = "invalid"

    def detector(self, link):
        if link.startswith('vmess://'):
            return link[8:]
        elif link.startswith('vless://'):
            return link[8:]
        else:
            return "invalid"

    def vmessextractor(self, vmesslink):
        if vmesslink == "invalid":
            return "invalid"
        else:
            try:
                decoded_data = base64.b64decode(vmesslink).decode('utf-8')
                vmess_info = json.loads(decoded_data)
                return vmess_info
            except:
                return "invalid"

    def vlessextractor(self, vlesslink):

        parsed_url = urlparse(vlesslink)
        user_info = parsed_url.username
        server_address = parsed_url.hostname
        server_port = parsed_url.port
        query_params = parse_qs(parsed_url.query)
        fragment = parsed_url.fragment

        query_params = {k: v[0] for k, v in query_params.items()}

        vless_info = {
            "user_info": user_info,
            "server_address": server_address,
            "server_port": server_port,
            "fragment": fragment,
            **query_params
        }

        return vless_info

    def final_output(self):
        if self.link.startswith("vmess://"):
            return self.output, self.output['ps']
        elif self.link.startswith("vless://"):
            return self.output, self.output['fragment']


example = Extractor(
    "vmess://eyJhZGQiOiJuczIzNy5ub29yYWhvc3QuY29tIiwiYWlkIjoiMCIsImhvc3QiOiIiLCJpZCI6ImE4MzEzODFjLTYzMjAtNGQ1My1hZDRmLThkZGE0MGIzMDgxMSIsIm5ldCI6IndzIiwicGF0aCI6Ii9ncmFwaHFsP2tleT04MDdkZGI4Yzk3NjRjMDg0MzAyNjEyY2NiOTg4ODBiMiIsInBvcnQiOiI0NDMiLCJwcyI6IlZNZXNzICM4NzE0NSIsInNjeSI6Im5vbmUiLCJzbmkiOiIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ==")
print(example.final_output()[1])

example2 = Extractor(
    "vless://6dd184d2-19b8-e570-8f29-19ad999abc8a@q.ownlink.pro:27768?security=none&encryption=none&headerType=http&type=tcp#31720")
print(example2.final_output()[1])
