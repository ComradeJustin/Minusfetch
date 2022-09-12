
import psutil
import platform
from art import *
import time
import math
import socket
from platform import python_version
from psutil import virtual_memory
uname = platform.uname()
Uptime = time.time() - psutil.boot_time()
hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)
Time_elapsed = round(Uptime/60/60, 2)
mem = virtual_memory()
totalmem = round(mem.total/1000/1000, 2)

 

Art = text2art("-Fetch", font='block', chr_ignore=True)
print(Art)
print("="*40, "System Information", "="*40)
print(f"                 Cpu usage is = " + str(psutil.cpu_percent(1))+"%")
print(f"                 OS:  {uname.release} {uname.system} {uname.machine}")
print(f"                 Computer name: {uname.node}")
print(f"                 CPU: {uname.processor}, Core count: {psutil.cpu_count(logical=True)}  ")
print(f"                 Uptime: {Time_elapsed} Hours")
print(f"                 IP: {IpAddress}")
print(f"                 Python version: {python_version()}")
print(f"                 TotalRam: {totalmem}MB")


