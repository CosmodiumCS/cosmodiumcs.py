# cosmodiumcs.py

## Install
NOTE: not yet integrated
```python
pip install cosmodiumcs
```

## Usecase
```python
from cosmodiumcs import *
```

## Debugging & Logging
Input:
```python
ccs_confirm("Access granted")
ccs_deny("Permission denied")
ccs_error("Wrong password, try again")
ccs_info("Created by : bluecosmo")
ccs_input("Enter your name")
ccs_pending("Connecting")
ccs_warning("User activity is being logged")
```
Output:
```
[+] Access granted
[-] Permission denied
[!] ERROR : Wrong password, try again
[$] Created by : bluecosmo
[~] Enter your name :
[*] Connecting...
[!] User activity is being logged
```

---
hey @everyone , its been a sec since we last touched base on this side of ccs haha! i'd really like to kick things off with a new project!

i'd like to make `cosmodiumcs` python library, and our tools will now be integrated into it. so people can do things like

```python
from cosmodiumcs import mk15 # skeletonkey

mk15.eCaesarCipher("hello, world", 5) # mjqqt, btwqi
mk15.dCaesarCipher("mjqqt, btwqi", 5) # hello, world
```

for this example, we can port the code over from skeleton key to cosmodiumcs.py. this way, skeletonkey's codebase will be much smaller, because skeleton key will really just be using our python library. plus individual devs will be able to use our codebase in their own projects. here are some more pseudo examples i thought of

```python
from cosmodiumcs import mk14 # supervision

cameras = mk14.queryCameras("Maryland")
for camera in cameras:
  print(camera.name, camera.url)
```

```python
from cosmodiumcs import mk01 as onlyrat
from cosmodiumcs.mk15 import eRSA 

onlyrat.generateInstaller("Powershell", "12.345.67.89")

if onlyrat.connectionEstablished():
  eRSA("C:/Users/daddy/Desktop/encryptme.txt")
```

love to hear y'alls thoughts :)
