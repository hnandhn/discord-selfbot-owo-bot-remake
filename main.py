#from api import key
pain = "Non-Premium"
from colorama import init
import os
from sys import exit


from sys import *
import logging
import sys
import time

def error(exctype, value, tb):
    f = open('logs.txt','w')
    f.write('Lastest Error Information: \n')
    f.write('Type: {} \n'.format(exctype))
    f.write('Value: {} \n'.format(value))
    f.write('Traceback: {} \n'.format(tb))
    print(f'[ERROR] Stopped Due To Unexpected Error...')
    time.sleep(2)
    raise SystemExit
sys.excepthook = error
import requests
import atexit
from multiprocessing import Process
from multiprocessing import Pool
import random
import re
try:
 from inputimeout import inputimeout,TimeoutOccurred
except:
 from setup import install
 install()
finally:
 from inputimeout import inputimeout,TimeoutOccurred
if os.name == 'nt':
  import json
else:
  import simplejson as json
try:
  from discum import *
except:
  from setup import install
  install()
finally:
  from discum import *
try:
 from discord_webhook import DiscordWebhook
except:
 from setup import install
 install()
finally:
 from discord_webhook import DiscordWebhook
init()
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: 1.0.5**""")

wbm=[13,16]
time.sleep(0.5)
class client:
  commands=[
    "owo hunt",
    "owo battle",
    ]
  darkcommands=[
    "pls beg",
    "pls hunt",
    "pls fish"
    ]
  fishcommands=[
    "%fish",
    ]
  gamecommands=[
    "t", "h"
    ]
  totalcmd = 0
  totaltext = 0
  stopped = False
  recentversion = "1.0.5"
  wait_time_daily = 60
  channel2 = []
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        gm = data["gm"]
        sm = data["sm"]
        pm = data["pm"]
        em = data["em"]
        prefix = data["prefix"]
        allowedid = data["allowedid"]
        webhook = data["webhook"]
        webhookping = data["webhookping"]
        alt = data["alt"]
        daily = data["daily"]
        change = data["change"]
        stop = data["stop"]
        owo = data["owo"]
        fish = data["fish"]
        dank = data["dank"]

        channelxp = channel
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   from newdata import menu
   menu()
   os.execl(executable, executable, *argv)
  head = {'Authorization': str(token)}
  response = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
  if response.status_code == 200:
    pass
  elif response.status_code == 429:
    print(f"{color.fail}[ERROR]{color.reset} Too Many Requests! Try Again Later.")
    time.sleep(2)
    raise SystemExit
  else:
    print(f"{color.fail}[ERROR]{color.reset} Invalid Token")
    time.sleep(2)
    raise SystemExit

  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Info              {color.reset}|')
  print('=========================')
  time.sleep(0.5)
choice = None
try:
 print("Automatically Pick Option [1] In 10 Seconds.")
 choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
except TimeoutOccurred:
 choice = "1"
if (choice == "1"):
      pass
elif (choice == "2"):
 from newdata import menu
 menu()
elif (choice == "3"):
      print(f"{client.color.purple} =========Support========== {client.color.reset}")
      print(f"{client.color.purple}https://discord.gg/3kTrhbBVQm{client.color.reset}")
      print(" ")
      print(f"{client.color.purple} =========Disclaimer========={client.color.reset}")
      print(f"{client.color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
      print(" ")
      print(f'{client.color.purple} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} Sudo-Nizel')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(" ")
      print(f'{client.color.purple} =========Selfbot Commands=========={client.color.reset}')
      print("{Prefix}send {Message} [Send Your Provied Message}")
      print("{Prefix}restart [Restart The Selfbot]")
      print("{Prefix}exit [Stop The Selfbot]")
      print("{Prefix}sm {on/off} [Turn On Or Off Sleep Mode]")
      print("{Prefix}em {on/off} [Turn On Or Off Exp Mode]")
      print("{Prefix}pm {on/off} [Turn On Or Off Pray Mode]")
      print("{Prefix}gm {on/off} [Turn On Or Off Gems Mode]")
      print(" ")
      print("{Prefix} == Your Prefix")
      time.sleep(15)
      raise SystemExit
else:
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(1)
 os.execl(executable, executable, *argv)
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)

@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: 
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def security(resp):
 if client.webhook != 'None':
  if issuechecker(resp) == "captcha":
    client.stopped = True
    user = bot.gateway.session.user
    if client.webhookping != 'None':
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> I Found A Captcha In Channel: <#{}>'.format(client.webhookping,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
      
    else:
     sentwebhook = DiscordWebhook(url=client.webhook, content='<@{}> <@{}> I Found A Captcha In Channel: <#{}>'.format(user['id'],client.allowedid,client.channel))
     response = sentwebhook.execute()
     bot.gateway.close()
 if client.webhook == 'None':
  if issuechecker(resp) == "captcha":
   client.stopped = True
   bot.gateway.close()
@bot.gateway.command
def issuechecker(resp):
 global pain
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and client.stopped != True:
    if m['author']['id'] == '677789907388989469' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
     if '(2/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
       return "captcha"
     if '(3/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
       return "captcha"
     if '(4/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
       return "captcha"
     if '(5/5)' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
       return "captcha"
     if 'banned' in m['content'].lower():
       print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
       return "captcha"
     if 'complete your captcha to verify that you are human!'  in m['content']:
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
     if 'DM' in m['content'].lower():
       print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
       return "captcha"
     if pain == "Premium" and client.change == "YES":
        c = bot.gateway.session.guild(m['guild_id']).channels
        a = c.keys()
        b = random.choice(list(a))
        if c[b]['type'] == "guild_text":
         client.channel2 = []
         client.channel2.append(b)
         client.channel2.append(c[b]['name'])
def runner():
  if client.owo == "YES":
    if client.stopped != True:
        
        command=random.choice(client.commands)
        command2=random.choice(client.commands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd += 1
        if not command2==command and client.stopped != True:
          bot.typingAction(str(client.channel))
          time.sleep(13)
          bot.sendMessage(str(client.channel), command2)    
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd += 1
        time.sleep(random.randint(wbm[0],wbm[1]))
  if client.owo == "NO":
    pass
  if client.dank == "YES":
    if client.stopped != True:
        
        command=random.choice(client.darkcommands)
        command2=random.choice(client.darkcommands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd += 1
        if not command2==command and client.stopped != True:
          bot.typingAction(str(client.channel))
          time.sleep(10)
          bot.sendMessage(str(client.channel), command2)    
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd += 1
        time.sleep(random.randint(50,60))
  if client.dank == "NO":
    pass
  if client.fish == "YES":
    if client.stopped != True:
        
        command=random.choice(client.fishcommands)
        command2=random.choice(client.fishcommands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd += 1
        if not command2==command and client.stopped != True:
          bot.typingAction(str(client.channel))
          time.sleep(1)
          bot.sendMessage(str(client.channel), command2)    
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd += 1
        time.sleep(random.randint(4,5))
  if client.fish == "NO":
    pass
def owoexp():
 if client.stopped != True:
  if client.em == "YES":
        
        try:
         response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random?count=5")
         if response.status_code == 200:
           json_data = response.json()
           data = json_data['data']
           bot.sendMessage(str(client.channelxp), "1 "+ data[0]['quoteText'])
           print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} mess 1")
           time.sleep(3)
           bot.sendMessage(str(client.channelxp), "2 "+ data[1]['quoteText'])
           print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} mess 2")
           time.sleep(3)
           bot.sendMessage(str(client.channelxp), "3 "+ data[2]['quoteText'])
           print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} mess 3")
           time.sleep(3)
           bot.sendMessage(str(client.channelxp), "4 "+ data[3]['quoteText'])
           print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} mess 4")
           time.sleep(3)
           bot.sendMessage(str(client.channelxp), "5 "+ data[4]['quoteText'])
           print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} mess 5")
           time.sleep(3)
           client.totaltext = client.totaltext + 1
           time.sleep(random.randint(1,2))
         else:
           pass
        except:
           pass
 if client.em == "NO":
        pass
def owopray():
 if client.stopped != True:
  if client.pm == "YES":
    bot.sendMessage(str(client.channel), "owo pray")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo pray")
    client.totalcmd += 1
    time.sleep(13)
 if client.pm == "NO":
   pass
@bot.gateway.command
def gems2(resp):
  gems_list_1 = ["cgem1","ugem1","rgem1","egem1","mgem1","lgem1","fgem1"]
  gems_list_3 = ["cgem3","ugem3","rgem3","egem3","mgem3","lgem3","fgem3"]
  gems_list_4 = ["cgem4","ugem4","rgem4","egem4","mgem4","lgem4","fgem4"]
  check1 = None
  check3 = None
  check4 = None
  if client.stopped != True:
   if client.gm == "YES":
    if resp.event.message:
      m = resp.parsed.auto()
      if m['channel_id'] == client.channel and client.stopped != True:
       if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
        if m['embeds'] == [] and "hunt" and "You found" and "gained" in m['content']:
         if not "empowered" in m['content']:
           gems1(random.randint(0,2))
         else:
          check1 = any(gems1 in m['content'] for gems1 in gems_list_1)
          check3 = any(gems3 in m['content'] for gems3 in gems_list_3)
          check4 = any(gems4 in m['content'] for gems4 in gems_list_4)
          if check1 == False:
           if gems1(0) == 0:
             return
          if check3 == False:
           if gems1(1) == 1:
             return
          if check4 == False:
           if gems1(2) == 2:
             return
def gems1(nogem):
    bot.typingAction(str(client.channel))
    time.sleep(3)
    bot.sendMessage(str(client.channel), "owo inv")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo inv")
    client.totalcmd += 1
    time.sleep(4)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    inv = 0
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='408785106942164992' and 'Inventory' in msgs[i]['content']:
        inv=re.findall(r'`(.*?)`', msgs[i]['content'])
        i = length
     else:
        i += 1
    if not inv:
       time.sleep(5)
       return
    else:
      if '50' in inv:
        bot.sendMessage(str(client.channel), "owo lb all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo lb all")
        time.sleep(13)
        return
      if '100' in inv:
        bot.sendMessage(str(client.channel), "owo crate all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo crate all")
        time.sleep(2)
      for item in inv:
        try:
          if int(item) > 100:
            inv.pop(inv.index(item)) #weapons
        except: #backgounds etc
          inv.pop(inv.index(item))
      tier = [[],[],[]]
      print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Found {len(inv)} gems Inventory")
      for gem in inv:
        gem = re.sub(r"[^a-zA-Z0-9]", "", gem)
        gem = int(float(gem))
        if 50 < gem < 58:
          tier[0].append(gem)
        elif 64 < gem < 72:
          tier[1].append(gem)
        elif 71 < gem <  79:
          tier[2].append(gem)
      for level in range(0,1):
        if not len(tier[level]) == 0 and client.stopped != True:
         if not len(tier[nogem]) == 0:
          time.sleep(2)
          bot.sendMessage(str(client.channel), "owo use "+str(max(tier[nogem])))
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo use {str(max(tier[nogem]))}")
         else:
          return nogem
def daily():
 global pain
 if client.daily == "YES" and pain == "Premium":
    bot.typingAction(str(client.channel))
    time.sleep(3)
    bot.sendMessage(str(client.channel), "owo daily")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo daily")
    client.totalcmd += 1
    time.sleep(3)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    daily = ""
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='408785106942164992' and msgs[i]['content'] != "" and "Nu" or "daily" in msgs[i]['content']:
        daily = msgs[i]['content']
        i = length
     else:
        i += 1
    if not daily:
       time.sleep(5)
       return
    else:
       if "Nu" in daily:
         daily = re.findall('[0-9]+', daily)
         client.wait_time_daily = str(int(daily[0]) * 3600 + int(daily[1]) * 60 + int(daily[2]))
         if "0" in client.wait_time_daily:
           client.wait_time_daily.replace("0","0o")
           print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Next Daily: {client.wait_time_daily.replace('o','')}s")
       if "Your next daily" in daily:
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Claimed Daily")
@bot.gateway.command
def othercommands(resp):
 prefix = client.prefix
 if resp.event.message:
   m = resp.parsed.auto()
   if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
    if prefix == "None":
     bot.gateway.removeCommand(othercommands)
     return
    if "{}send".format(prefix) in m['content'].lower():
     message = m['content'][6::]
     bot.sendMessage(str(m['channel_id']), message)
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {message}")
    if "{}restart".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Restarting...")
     print(f"{client.color.okcyan} [INFO] Restarting...  {client.color.reset}")
     time.sleep(1)
     os.execl(executable, executable, *argv)
    if "{}exit".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Exiting...")
     print(f"{client.color.okcyan} [INFO] Exiting...  {client.color.reset}")
     bot.gateway.close()
    if "{}gm".format(prefix) in m['content'].lower():
     if "on" in m['content'].lower():
      client.gm = "YES"
      bot.sendMessage(str(m['channel_id']), "Turned On Gems Mode")
      print(f"{client.color.okcyan}[INFO] Turned On Gems Mode{client.color.okcyan}")
     if "off" in m['content'].lower():
      client.gm = "NO"
      bot.sendMessage(str(m['channel_id']), "Turned Off Gems Mode")
      print(f"{client.color.okcyan}[INFO] Turned Off Gems Mode{client.color.okcyan}")
    if "{}pm".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.pm = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Pray Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Pray Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.pm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Pray Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Pray Mode{client.color.reset}")
    if "{}sm".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.sm = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Sleep Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Sleep Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.sm = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Sleep Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Sleep Mode{client.color.reset}")
    if "{}em".format(prefix) in m['content'].lower():
      if "on" in m['content'].lower():
       client.em = "YES"
       bot.sendMessage(str(m['channel_id']), "Turned On Exp Mode")
       print(f"{client.color.okcyan}[INFO] Turned On Sleep Mode{client.color.reset}")
      if "off" in m['content'].lower():
       client.em = "NO"
       bot.sendMessage(str(m['channel_id']), "Turned Off Exp Mode")
       print(f"{client.color.okcyan}[INFO] Turned Off Sleep Mode{client.color.reset}")
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  pray = 0
  owo=pray
  daily_time = pray
  change = pray
  gemstime = pray
  main=time.time()
  stop = main
  while x:
      runner()
      if time.time() - pray > random.randint(300, 600):
        owopray()
        pray=time.time()
      if time.time() - owo > random.randint(5, 15):
        owoexp()
        owo=time.time()
      if client.sm == "YES":
       if time.time() - main > random.randint(1000, 2000):
        main=time.time()
        print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Sleep Mode active")
        time.sleep(random.randint(500, 700))
      if time.time() - daily_time > int(client.wait_time_daily):
        daily()
        daily_time = time.time()
      if time.time() - change > random.randint(600,1500):
       if not client.channel2 == []:
        print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Changed Channel To: {client.channel2[1]}")
        client.channel = client.channel2[0]
        change = time.time()
      if client.stop != "None":
       if time.time() - stop > int(client.stop):
         bot.gateway.close()
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)
@atexit.register
def atexit():
 print(f"{client.color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{client.color.reset}")
 time.sleep(0.5)
 print(f"{client.color.okgreen}Total Number Of Random Text Sent: {client.totaltext}{client.color.reset}")
 time.sleep(0.5)
 print(f"{client.color.purple} [1] Restart {client.color.reset}")
 print(f"{client.color.purple} [2] Support {client.color.reset}")
 print(f"{client.color.purple} [3] Exit    {client.color.reset}")
 choice = None
 try:
  print("Automatically Pick Option [3] In 10 Seconds.")
  choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
 except TimeoutOccurred:
  choice = "4"
 if choice == "1":
  os.execl(executable, executable, *argv)
 elif choice == "2":
  print("Having Issue? Tell Us In Our Support Server")
  print(f"{client.color.purple} https://discord.gg/3kTrhbBVQm {client.color.reset}")
 elif choice == "3":
  bot.gateway.close()
 else:
  bot.gateway.close()
