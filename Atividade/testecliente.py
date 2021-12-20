import requests
from interface import *

#r1 = requests.get("http://127.0.0.1:8080")
#print(r1.text)
while True:
   try:
      r = requests.post("http://127.0.0.1:8080", data=(input('\033[32mENVIAR MENSAGEM VIA CLIENTE> \033[m')))
   except ValueError:
      continue
   msg = r.text
   cabecalho(f"\033[34mMENSAGEM RECEBIDA (SERVIDOR)\033[m" + f"\033[34m> {msg}\033[m")
   linha(len('MENSAGEM RECEBIDA (SERVIDOR)') + len(msg))







