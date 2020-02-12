import os
import shutil
import sbConstants 
from datetime import datetime as dt
from blocker import fn_blocksite


#create a master copy of host for backup and working copy of host
#master copy is created only for the first time when program runs
if not os.path.isfile(sbConstants.host_master):
    shutil.copyfile(sbConstants.host_target_file,sbConstants.host_master)

#get list of websites to block
target_site_file_wh = open(os.path.join(sbConstants.cwd,'blocklist_workhours.txt'))
website_list_wh = target_site_file_wh.read().splitlines()
target_site_file_wh.close()

target_site_file_ah = open(os.path.join(sbConstants.cwd,'blocklist_afterhours.txt'))
website_list_ah = target_site_file_ah.read().splitlines()
target_site_file_ah.close()

#run blocker
while True:
    if(sbConstants.workHours_Start < dt.now().time().hour < sbConstants.workHours_End):
        fn_blocksite(website_list_wh)
    else:
        fn_blocksite(website_list_ah)


