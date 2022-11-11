#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Rani64.so')
except:
    pass
os.system('rm -rf Sarfraz.so Rani32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Rani64.so'):
        os.system('curl -L https://github.com/MISTYXD/DIFUSABL/blob/main/Rani64.cpython-310.so?raw=true -o Rani64.so') 
        import Rani64
    else:
        import Rani64

elif bit == '32bit':
    if not os.path.isfile('Rani32.so'):
        os.system('curl -L https://github.com/MISTYXD/DIFUSABL/blob/main/Rani32.cpython-310.so?raw=true -o Rani32.so') 
        import Rani32
    else:
        import Rani32
