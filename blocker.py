import time
from datetime import datetime as dt
import sbConstants 
import shutil

def fn_blocksite(website_list): 
    #recopy temp working file from master file everytime
    #temp file will be modified by the sub program
    print('Reset temp hosts file')
    shutil.copyfile(sbConstants.host_master,sbConstants.host_temp)   

    print('Modifying temp hosts file')
    with open(sbConstants.host_temp,'a') as file:

        #add comments to host file
        file.write('\n')
        file.write(sbConstants.hostFileComment_Start + " at " + dt.now().strftime("%b %d %Y %H:%M:%S") + '\n')
        file.write('\n')
        #start adding websites to block
        for website in website_list:
            file.write(sbConstants.redirect + ' ' + website + '\n')

        #add an new line char to ignore anything added above and start with new line
        file.write('\n')
        file.write(sbConstants.hostFileComment_End + " at " + dt.now().strftime("%b %d %Y %H:%M:%S") + '\n')         
    #replace target file
    print('Replace target file')
    shutil.copyfile(sbConstants.host_temp,sbConstants.host_target_file)   
    time.sleep(sbConstants.sleepTime)

