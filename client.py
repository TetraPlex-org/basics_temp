import requests
import time as t
session = requests.session()
ipaddress = input("enter server ip: ")
for i in range(10):
  t.sleep(1)
  response = session.get("http://0.0.0.0:8000")
  print(response)
