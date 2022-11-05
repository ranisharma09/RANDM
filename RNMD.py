import os, sys, platform
try:
    import requests
except:
	
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MISTYY2.so')
except:
    pass
os.system('rm -rf MISTYY2.so ')
os.system('git pull')
os.system("xdg-open https://github.com/ranisharma09")
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MISTYY2.so'):
        os.system('curl -L https://github.com/MISTYXD/RANI/blob/main/MISTYY2.cpython-311.so?raw=true -o MISTYY2.so') 
        import MISTYY2
    else:
        import MISTYY2
