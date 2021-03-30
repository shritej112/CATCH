#from image_capture_mulitprocessing_test import *
#from image_capture_mulitprocessing_test_2 import *
from image_recog_multiprocessing_test import *
from multiprocessing import Process



if __name__ == "__main__":
	
	search = input("Enter the name of the person to be searched : ")
	
	'''
	p1 = Process(target = capture_windows)
	p1.start()
	p2 = Process(target = capture_android)
	p2.start()
	'''
	#capture_windows()
	#capture()
	print("Searching....")
	recog(search)
