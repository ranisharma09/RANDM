import os,sys,subprocess
try:
    import requests
except:
    os.system("pip install requests")
try:
    import rich
except:
    os.system("pip install rich")
try:
    import mechanize
except:
    os.system("pip install mechanize")

cwd = subprocess.check_output('uname -om', shell=True)
cwd = str(cwd)

if 'aarch64' in cwd:
    if not os.path.isfile('Rani64'):
        os.system('curl -L https://github.com/MISTYXD/DIFUSABL/blob/main/Rani64.cpython-310.so?raw=true > Rani64')
        os.system('chmod 777 Rani64')
        os.system('./Rani64')
    else:
        os.system('./Rani64')
elif 'arm' in cwd:
    if not os.path.isfile('Rani32'):
        os.system('curl -L https://github.com/MISTYXD/DIFUSABL/blob/main/Rani32.cpython-310.so?raw=true > Rani32')
        os.system('chmod 777 Rani32')
        os.system('./Rani32')
    else:
        os.system('./Rani32')
else:
    exit(" we can't find your bit sory")
