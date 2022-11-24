import subprocess
import os 
from tkinter import *  
from tkinter import messagebox  
 

#creates txt file if non existant (file where hwid it's stored)

if (os.path.exists("hwid.txt") == False):
    f = open("hwid.txt", "w")  

#makes file hidden

subprocess.check_call(["attrib","+H","hwid.txt"])

#gets computer HWID

def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid

#checks if HWID already stored if not will write it

filesize = os.path.getsize("hwid.txt")

if filesize == 0:
    f = open("hwid.txt", "a")
    f.write(GetUUID())
    f.close()

#check if HWID it's simillar 
with open('hwid.txt', 'r') as file:
    hwidstoredPrev = file.read().replace('\n', '')

if GetUUID() == hwidstoredPrev:
    messagebox.showinfo("Auth Info","Auth succesfully granted!")  
else:
    messagebox.showerror("HWID Blocked","We detected a HWID missmatch, please contact an administrator for further assistance!")  
