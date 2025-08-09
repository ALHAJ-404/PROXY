import os, platform
import requests
bit = platform.architecture()[0]
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
if bit == "64bit":
        from a import Subscraption
        Subscraption()
 
elif bit == "32bit":
        from a import Subscriptions
        Subscraption()
 