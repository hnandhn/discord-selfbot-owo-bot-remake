import sys
import subprocess
import pkg_resources
import os
import time
def install():
 if os.name == 'nt':
    required = {'discum', 'inputimeout', 'discord_webhook'}
 if os.name != 'nt':
    required = {'discum', 'simplejson', 'inputimeout', 'discord_webhook'}
 installed = {pkg.key for pkg in pkg_resources.working_set}
 missing = required - installed
 if not missing:
    print("Đã tải xong gói hỗ trợ!")
    time.sleep(2)
 if missing:
    print("Đang tải gói hỗ trợ bắt buộc...")
    time.sleep(1)
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    print("Đã tải xong gói hỗ trợ!")
    time.sleep(2)
