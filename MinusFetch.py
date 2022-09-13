
import psutil
import platform
from art import *
import time
import math
import socket
import time
import colorama



uname = platform.uname() 
Uptime = time.time() - psutil.boot_time()
hostname = socket.gethostname()
Time_elapsed = round(Uptime/60/60, 2)
mem = psutil.virtual_memory()
totalmem = round(mem.total/1000/1000, 2)

 

Art = text2art("-Fetch", font='block', chr_ignore=True)
for x in range (0,4):  
    b = "Loading" + "." * x
    print (colorama.Fore.GREEN + b, end="\r")
    time.sleep(1)

print(colorama.Fore.GREEN + f"{Art}")
time.sleep(0.1)
print(colorama.Fore.WHITE + "="*40, colorama.Fore.LIGHTBLUE_EX+ "System Information", colorama.Fore.WHITE +"="*40)
time.sleep(0.4)


print(colorama.Fore.LIGHTCYAN_EX + "                 Cpu usage is =", colorama.Fore.WHITE + f"{str(psutil.cpu_percent(1))}" + colorama.Fore.WHITE +"%")
print(colorama.Fore.LIGHTCYAN_EX + "                 OS:", colorama.Fore.WHITE + f"  {uname.release} {uname.system} {uname.machine}")
print(colorama.Fore.LIGHTCYAN_EX + "                 Computer name:", colorama.Fore.WHITE + f"{uname.node}")
print(colorama.Fore.LIGHTCYAN_EX + "                 CPU:", colorama.Fore.WHITE + f"{uname.processor}", "Core count:", colorama.Fore.WHITE + f" {psutil.cpu_count(logical=True)}")
print(colorama.Fore.LIGHTCYAN_EX + "                 Uptime:", colorama.Fore.WHITE + f"{Time_elapsed} Hours")
print(colorama.Fore.LIGHTCYAN_EX + "                 Hostname:", colorama.Fore.WHITE + f"{hostname}")
print(colorama.Fore.LIGHTCYAN_EX + "                 Python version:", colorama.Fore.WHITE + f"{platform.python_version()}")
print(colorama.Fore.LIGHTCYAN_EX + "                 TotalRam:", colorama.Fore.WHITE + f"{totalmem}MB")
print(colorama.Fore.CYAN +         "                 Welcome to", colorama.Fore.RED + f"{uname.system}!")
time.sleep(10)
print(colorama.Style.RESET_ALL)
print("")


