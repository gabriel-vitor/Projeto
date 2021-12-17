import requests
URL = 'http://127.0.0.1:8080/'

while True:
    r = requests.get(URL)
    print(r.text)

