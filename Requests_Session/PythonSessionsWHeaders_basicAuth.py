
	
import requests
#
session = requests.Session()
session.auth = ('<username>', '<password>')
headers ={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36'}

session.headers=headers
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
session.proxies.update(proxies)
 

"""
To use params in the request like : /url?<param1>=<value1>&<param2>=<Value2>
"""
params = {
    "page": 20,
    "page_size": 25,
    "type": "image"
}
session.params = params

response = session.get('URL', verify=False)
print(response.text)