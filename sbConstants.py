import sys
import os

cwd = sys.path[0]
host_temp = os.path.join(cwd,'hosts')
host_master = os.path.join(cwd,'hosts_master')
host_target_folder = 'C:\Windows\System32\drivers\etc'
host_target_file = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
sleepTime = 300 
workHours_Start = 8
workHours_End = 18

hostFileComment_Start = "#Start of section added by Siteblocker.py"
hostFileComment_End = "#End of section added by Siteblocker.py"