import requests
from sys import exit
import time
def key():
 preorno = input("Premium Or Normal? (P/N): ")
 if preorno.lower() == "n":
  username = input("Enter Your Username: ")
  token = input("Enter Authorize Token: ")
  at = input("Secret Token: ")
  r = requests.get('https://crackkeypremiumowo.codegabap.tk/user/?token={}'.format(at))
  if r.status_code == 404:
   print("Invalid Secret Token")
   time.sleep(3)
   raise SystemExit
  try:
    if token == r.json()[username]:
      print("Successfuly Logged In !")
      return "Non-Premium"
    else:
      print("Invalid Authorize Token")
      time.sleep(3)
      raise SystemExit
  except KeyError:
    print("Invalid Username")
    time.sleep(3)
    raise SystemExit
 else:
  username = input("Enter Username: ")
  token = input("Enter Token: ")
  r = requests.get('https://crackkeypremiumowo.codegabap.tk/premium/?token={}&user={}'.format(token,username))
  if r.status_code == 200:
   print("Successfuly Logged In !")
   return "Premium"
  if r.status_code == 400:
   print("Invalid Username!")
   raise SystemExit
  if r.status_code == 404:
   print("Invalid Token!")
   raise SystemExit
if __name__ == "__main__":
 key()
