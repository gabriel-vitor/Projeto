import requests

r1 = requests.get("http://127.0.0.1:8080")
print(r1.text)
while True:
   try:
      r = requests.post("http://127.0.0.1:8080", data=(input('R= ')))
   except ValueError:
      continue
   print(r.text)







