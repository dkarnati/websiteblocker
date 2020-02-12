# websiteblocker
Website blocker written in Python

Welcome to the website blocker wiki!

Written in Python, the program lets you block websites on a schedule for during work hours and after work hours. This can help with distractions(at least for me) and be productive at work. It can also help you block any websites that you accidentally don't want to open during your normal work hours.

Please follow the steps below to try this program:

1) Download the files to any folder.
2) Add list of sites that you would like to block by editing files "blocklist_workhours" and "blocklist_afterhours".
3) Optionally, edit your work hours schedule. Open sbConstants.py and modify the defaults:
   - workHours_Start: Start of work hours (24 hours format).
   - workHours_End: End of work hours (24 hours format).
4) You need admin privileges to your command prompt before running the program.
5) Most importantly, please make a copy of your host file located at "C:\Windows\System32\drivers\etc" before trying this program. You can    always revert back when needed.
6) Run "schedule_website_blocker.py" to start the program.

PS: This program is compatible with windows only as of now.
