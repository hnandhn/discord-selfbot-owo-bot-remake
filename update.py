import requests
from os import getcwd

directory = getcwd()
filename = directory + '/main.py'
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/main.py"
r = requests.get(url)

#main.py
f = open(filename, 'w')
filename = directory + '/main.py'
print("Updating: ",filename)
f.write(r.text)
f.close()

#newdata.py
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/newdata.py"
filename = directory + '/newdata.py'
print("Updating: ",filename)
f.write(r.text)
f.close()

#setup.py
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/setup.py"
filename = directory + '/setup.py'
print("Updating: ",filename)
f.write(r.text)
f.close()

#settings.json
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/settings.json"
filename = directory + '/settings.json'
print("Updating: ",filename)
f.close()

#version.txt
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/version.txt"
filename = directory + '/version.txt'
print("Updating: ",filename)
f.write(r.text)
f.close()

#requirements.txt
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/requirements.txt"
filename = directory + '/requirements.txt'
print("Updating: ",filename)
f.write(r.text)
f.close()

#README.md
f = open(filename, 'w')
url = "https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/main/source/README.md"
filename = directory + '/README.md'
print("Updating: ",filename)
f.write(r.text)
f.close()

print("Successfully Updated All File!")
