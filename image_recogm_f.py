# USAGE
# python3 image_recog_multiprocessing_test2.py
# python3 image_recog_multiprocessing_test2.py --encodings encodings.pickle
# python3 image_recog_multiprocessing_test2.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import os
import time
import concurrent.futures	# Multiprocessing library
#from fetch import *

# construct the argument parser and parse the arguments
'''ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=False, default="encodings.pickle",
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=False,
	help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="hog",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())'''
args = {"encodings" : "encodings.pickle", "detection-method" : "hog"}
data = pickle.loads(open(args["encodings"], "rb").read())

# initialize the list of names for each face detected
#names = []
#name = "Unknown"

def image_recog(filename, dirpath, search):
	
	#print("aaa")
		
	if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):

		# load the input image and convert it from BGR to RGB
		#image = cv2.imread(args["image"])
		
		image = cv2.imread(os.path.join(dirpath, filename))
		
		
		#image = cv2.resize(image, (1280, 720)) 
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		#r = image.shape[1] / float(rgb.shape[1])

		# detect the (x, y)-coordinates of the bounding boxes corresponding
		# to each face in the input image, then compute the facial embeddings
		# for each face
		#print("[INFO] recognizing faces...")
		boxes = face_recognition.face_locations(rgb, model=args["detection-method"])
		encodings = face_recognition.face_encodings(rgb, boxes)

		

		# initialize the list of names for each face detected
		names = []
		#print("aaa")

		# loop over the facial embeddings
		for encoding in encodings:
			# attempt to match each face in the input image to our known
			# encodings
			matches = face_recognition.compare_faces(data["encodings"],
				encoding)
			name = "Unknown"

			# check to see if we have found a match
			if True in matches:
				# find the indexes of all matched faces then initialize a
				# dictionary to count the total number of times each face
				# was matched
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# determine the recognized face with the largest number of
				# votes (note: in the event of an unlikely tie Python will
				# select first entry in the dictionary)
				name = max(counts, key=counts.get)
			
			# update the list of names
			names.append(name)
		
				
		
		# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):
			# rescale the face coordinates
			'''top = int(top * r)
			right = int(right * r)
			bottom = int(bottom * r)
			left = int(left * r)'''
				
			# draw the predicted face name on the image
			cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
				0.75, (0, 255, 0), 2)

		
		# For searching a particular person
		if (name == search):
			a = dirpath.split("/")
			#print(a)
			print(name + " has been found!!")
			print(name + " has been captured by " + a[5])
			print(a[5])
			file = "device_id.txt"
			path = "/root/meta/face/images"
			file1 = os.path.join(path , file)
			with open(file1, 'w') as f:
			    f.write(a[5])
						
			
			
			'''
			for ((top, right, bottom, left), name) in zip(boxes, names):
				roi = image[top:bottom, left:right]
				cv2.imshow(ROI_image, roi)
			'''
		# show the output image
		# Every image will be displayed for 3 seconds
		#cv2.imshow("Image", image)
		cv2.imshow(dirpath + "/" + filename, image)			
		cv2.waitKey(1000)
		time.sleep(2)
		#print("aaa")
		cv2.destroyAllWindows()
		

#print(name)

# Wrapper function for combining multiple arguments
def image_recog_wrapper(p):
	return image_recog(*p)

def recog(search):

	# load the known faces and embeddings
	#print("[INFO] loading encodings...")
	data = pickle.loads(open(args["encodings"], "rb").read())

	# The directory where the captured images are stored
	directory = '/root/meta/face/images'
	#i = 1

	combined_array = []
	
	for dirpath, dirnames, files in os.walk(directory):

		for filename in files:
			
			combined_array.append([filename, dirpath, search])
			#print(str(i) + '. Image ' + str(i))
			
			# Combining the two 1-D arrays into one 2-D array
			# combined_array2 = list(zip(files, dirpath))
			
		
	#print(combined_array)
	# print(combined_array2)		
	
	with concurrent.futures.ProcessPoolExecutor() as executor:
		#executor.map(lambda p: image_recog(*p), combined_array)
		executor.map(image_recog_wrapper, combined_array)

			


# To run the above function
# main method

'''if __name__ == "__main__":
	
	search = input("Enter the name of the person to be searched : ")
	recog(search)
	
	#abc='shritej'	
	#main_image_recog(abc)	'''
	


		

