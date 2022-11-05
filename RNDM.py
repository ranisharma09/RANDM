import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MISTTY.so')
except:
    pass
os.system('rm -rf MISTTY.so ')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MISTTY.so'):
        os.system('curl -L https://github.com/MISTYXD/RANI/blob/main/MISTTY.cpython-311.so?raw=true -o MISTTY.so') 
        import MISTTY
    else:
        import MISTTY
