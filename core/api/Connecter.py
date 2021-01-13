import json
import urllib.request

class Connecter():
    """description of class"""
    def Request(self, url):
        key = {'private_key': '5966da3db81c45808f21087729e6cb88e0ada6648cd247f8803cfdea76f8694b'}
        jData = urllib.parse.urlencode(key).encode("utf-8")
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        request = urllib.request.Request(url)
        request.add_header('User-Agent', '&lt;User-Agent&gt;')

        data = json.loads(urllib.request.urlopen(request,data=jData).read())
        return data


