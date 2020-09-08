import robloxpy
import requests
import time

i = 1500
maxval2 = 9999999999999999999
print("Haydens Number Username Sniper")

while True:
     if i == maxval2:
            print("No number usernames open!")
            break
     else:
        iuse = str(i)
        result = robloxpy.DoesNameExist(iuse)
        if result == False:
            print("Username " + iuse + " is open")
            break
        else:
             print(iuse + " is taken")
             i = i +1
             time.sleep(1)
            
            
        