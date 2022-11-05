import os, sys, platform
try:
    import requests
except:
	os.system("xdg-open https://github.com/ranisharma09")
	
        os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MISTYY.so')
except:
    pass
os.system('rm -rf MISTYY.so ')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MISTYY.so'):
        os.system('curl -L https://github.com/MISTYXD/RANI/blob/main/MISTYY.cpython-311.so?raw=true -o MISTYY.so') 
        import MISTYY
    else:
        import MISTYY
