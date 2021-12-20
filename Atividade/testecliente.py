import requests
from interface import *

#r1 = requests.get("http://127.0.0.1:8080")
#print(r1.text)
while True:
   try:
      r = requests.post("http://127.0.0.1:8080", data=(input('ENVIAR MENSAGEM VIA CLIENTE = ')))
   except ValueError:
      continue
   msg = r.text
   cabecalho(f"MENSAGEM RECEBIDA (SERVIDOR)" + f"> {msg}")
   linha(len('MENSAGEM RECEBIDA (SERVIDOR)') + len(msg))







