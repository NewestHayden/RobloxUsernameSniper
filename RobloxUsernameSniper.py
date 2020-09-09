import robloxpy
import requests
import time

i = 15700
maxval2 = 9999999999999999999
print("Haydens Number Username Sniper\nBeing saved to UserArchive.txt under your user file")

while True:
    file1 = open("UserArchive.txt", 'a')
    if i == maxval2:
            print("No number usernames open!")
            file1.write("\nAll number usernames taken (wait what?)")
            file1.close()
            break
    else:
        iuse = str(i)
        result = robloxpy.DoesNameExist(iuse)
        if result == False:
            print("Username " + iuse + " is open")
            file1.write(iuse + " is open!")
            file1.close()
            break
        else:
             print(iuse + " is taken")
             file1.write("\n" +iuse + " is in use")
             file1.close()
             i = i +1
             time.sleep(1)
            
            
        
