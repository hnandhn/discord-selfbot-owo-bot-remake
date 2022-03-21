import time
import json
import os
from sys import exit
def menu():
 if os.name == 'nt':
    pass
 if os.name == 'linux':
    import simplejson as json
 else:
    try:
        import json
    except:
        import simplejson as json
 file = open("settings.json", "r")
 data = json.load(file)
 file.close()
 print('================================')
 print(f'| [0] Exit And Save           |')
 print(f'| [1] Change All Settings     |')
 print(f'| [2] Change Token            |')
 print(f'| [3] Change Channel          |')
 print(f'| [4] Change Pray Mode        |')
 print(f'| [5] Change Gems Mode        |')
 print(f'| [6] Change Exp Mode         |')
 print(f'| [7] Change Quest Mode       |')
 print(f'| [8] Change Sleep Mode       |')
 print(f'| [9] Change Webhook Settings |')
 print(f'| [10] Change Selfbot Commands|')
 print(f'| [11] Change Daily Mode      |')
 print(f'| [12] Change Stop Time       |')
 print(f'| [13] Change Switch Channel  |')
 print('================================')
 choice = input("Enter Your Choice: ")
 if choice == "0":
  raise SystemExit
 if choice == "1":
  t(data,"True")
  c(data,"True")
  pm(data,"True")
  gm(data,"True")
  em(data,"True")
  qm(data,"True")
  sm(data,"True")
  webhook(data,"True")
  daily(data,"True")
  stop(data,"True")
  switch_channel(data,"True")
 if choice == "2":
  t(data,"False")
 if choice == "3":
  c(data,"False")
 if choice == "4":
  pm(data,"False")
 if choice == "5":
  gm(data,"False")
 if choice == "6":
  em(data,"False")
 if choice == "7":
  qm(data,"False")
 if choice == "8":
  sm(data,"False")
 if choice == "9":
  webhook(data,"False")
 if choice == "10":
  oc(data,"False")
 if choice == "11":
  daily(data,"False")
 if choice == "12":
  stop(data,"False")
 if choice == "13":
  switch_channel(data,"False")
def t(data,all):
 data['token'] = input("Please Enter Your Account Token: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def c(data,all):
 data['channel'] = input("Please Enter Your Channel ID: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def pm(data,all):
 data['pm'] = input("Toggle Automatically Send Pray (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def gm(data,all):
 data['gm'] = input("Toggle Automatically Use Gems Mode (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def em(data,all):
 data['em'] = input("Toggle Automatically Send Random Text To Level Up (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def qm(data,all):
 data['alt'] = input("Toggle Automatically Do Quests (YES/NO): ")
 if data['alt'] == "YES":
  data['alt'] = input("Enter Your Alternative Account Token To Do Some Specified Quests: ")
 else:
  data['alt'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def sm(data,all):
 data['sm'] = input("Toggle Sleep Mode (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def webhook(data,all):
 data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def oc(data,all):
 data['prefix'] = input("Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): ")
 if data['prefix'] == "YES":
  data['prefix'] = input("Enter Your Selfbot Prefix: ")
  data['allowedid'] = input("Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": ")
  print("Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")
  time.sleep(1)
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def daily(data,all):
 data['daily'] = input("Toggle Automatically Claim Daily (YES/NO): ")
 if data['daily'] == "NO":
  data['daily'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def switch_channel(data,all):
 data['change'] = input("Toggle Switch Default Channel To Random One After 10 Mins (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def stop(data,all):
 data['stop'] = input("Toggle Stop After A Specifice Time (YES/NO): ")
 if data['stop'] == "YES":
  data['stop'] = input("Enter Stop Time (Seconds): ")
 else:
  data['stop'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
menu()
