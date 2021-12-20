import requests

r1 = requests.get("http://127.0.0.1:8080")
#print(r1.encoding)
while True:
   try:
      r = requests.post("http://127.0.0.1:8080", data=(input('POST client = ')))
   except ValueError:
      continue
   print(f"Mensagem servidor: {r.text}")







