import os, sys, platform
try:
    import requests
except:
	
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RK.so')
except:
    pass
os.system('rm -rf RK.so ')
os.system('git pull')
##os.system("xdg-open https://github.com/ranisharma09")
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RK.so'):
        os.system('curl -L https://github.com/MISTYXD/exec/blob/main/RK.cpython-311.so?raw=true -o RK.so') 
        import RK
    else:
        import RK
