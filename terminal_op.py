## This script saves the details about the devices connected in the network as the master machine.


from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole
import sys
import time
import os


client = MsfRpcClient('yourpassword11', ssl=True)

#exploit = client.modules.use('exploit', 'multi/handler')
#exploit['ExitOnSession'] = False


x=client.sessions.list


f = open("terminal_output.txt", 'w')
sys.stdout = f

for i in range(1,100):
	try:
		print("id : - ",i ,"name : -" , x[str(i)]["info"])
		shell = client.sessions.session(i)
		shell.write('sysinfo')
	except:
		print("",end="")
		continue	

#print("This is a demo test 2")

f.close()
