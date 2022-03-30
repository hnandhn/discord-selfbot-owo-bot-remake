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
 print('========================================')
 print(f'| [0] Thoát và lưu                    |')
 print(f'| [1] Thay đổi tất cả cài đặt         |')
 print(f'| [2] Thay đổi token                  |')
 print(f'| [3] Thay đổi channel                |')
 print(f'| [4] Thay đổi chế độ pray            |')
 print(f'| [5] Thay đổi chế độ sử dụng gem     |')
 print(f'| [6] CThay đổi chế độ kinh nghiệm    |')
 print(f'| [7] Thay đổi chế độ quest (removed) |')
 print(f'| [8] Thay đổi chế độ sleep           |')
 print(f'| [9] Thay đổi cài đặt webhook        |')
 print(f'| [10] Thay đổi lệnh selfbot          |')
 print(f'| [11] Thay đổi chế độ daily          |')
 print(f'| [12] Thay đổi thời gian stop        |')
 print(f'| [13] Thay đổi mod thay channel      |')
 print('========================================')
 choice = input("Nhập lựa chọn của bạn: ")
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
 data['token'] = input("Vui lòng nhập token tài khoản của bạn: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def c(data,all):
 data['channel'] = input("Vui lòng nhập id channel: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def pm(data,all):
 data['pm'] = input("Chỉnh chế độ pray (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def gm(data,all):
 data['gm'] = input("Chỉnh chế độ tự dùng gem mạnh nhất (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def em(data,all):
 data['em'] = input("Chỉnh chế độ auto gưi text để lên level (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def qm(data,all):
 data['alt'] = input("Tự động làm quest (YES/NO): ")
 if data['alt'] == "YES":
  data['alt'] = input("Nhập id của acc clone bạn để làm quest cụ thể (removed): ")
 else:
  data['alt'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def sm(data,all):
 data['sm'] = input("Chỉnh sleep mode (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def webhook(data,all):
 data['webhook'] = input("Chỉnh Discord Webhook, Nhập link Webhook nếu bạn muốn Ping bạn nếu OwO hỏi Captcha. Nếu không thì Nhập \"Không có \": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Bạn có muốn Ping một người dùng được chỉ định khi OwO hỏi Captcha không? Nếu Có Nhập ID Người dùng. Nếu không thì Nhập \"None\": ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def oc(data,all):
 data['prefix'] = input("Chỉnh lệnh Selfbot, bạn có thể điều khiển Selfbot của mình bằng lệnh (YES/NO): ")
 if data['prefix'] == "YES":
  data['prefix'] = input("Nhập prefix của selfbot: ")
  data['allowedid'] = input("Bạn có muốn cho phép người dùng sử dụng lệnh Selfbot của bạn không? Nếu Có Nhập ID Tài khoản, Nếu Không thì Nhập None: ")
  print("Tuyệt quá! Bạn có thể xem các lệnh Selfbot tại tùy chọn [3] Thông tin tại menu chính!")
  time.sleep(1)
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def daily(data,all):
 data['daily'] = input("Chỉnh tự động nhận daily (YES/NO): ")
 if data['daily'] == "NO":
  data['daily'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def switch_channel(data,all):
 data['change'] = input("Chỉnh Chuyển kênh mặc định sang ngẫu nhiên một sau 10 phút (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
def stop(data,all):
 data['stop'] = input("Chỉnh thời gian stop  (YES/NO): ")
 if data['stop'] == "YES":
  data['stop'] = input("Thêm thời gian stop (giây): ")
 else:
  data['stop'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Lưu thành công!')
 if not all == "True":
  menu()
menu()
