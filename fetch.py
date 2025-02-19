import re
import os
import sys

# file = 'fetch_location.txt'

#inp = 1
def fetch_id():
	file = "device_id.txt"
	path = "/root/meta/face/images"
	lines = []
	file1 = os.path.join(path , file)
	with open(file1, 'r') as f:
		for line in f:
			lines.append(line.rstrip('\n\r'))
			#folder = line[0]

			return(lines[0])
			#print(line)


def fetch_location(folder):
    path = "images/" + folder
    txt_file = folder + ".txt"
    file1 = os.path.join(path, txt_file)
    
    lines = []

    with open(file1, 'r') as f:

        #lines = f.readlines()
        for line in f:
            lines.append(line.rstrip('\n\r'))
            # lines.append(line.rstrip('\r'))
        #pattern = re.compile(r'^[1-9]\d*(\.\d+)?$')

    substring = '        Latitude        Longitude'

    # print(lines)
    index = lines.index(substring)

    # This is the actual new index
    new_index = index + 2
    
    # Temp new index
    #new_index = index + 4
    coordinates = lines[new_index]

    coordinates = re.split(' ', coordinates)

    while ("" in coordinates):
        coordinates.remove("")

    # print(coordinates)

    lat = coordinates[0]
    long = coordinates[1]

    return (lat,long)
'''folder = fetch_id()
lat,long = fetch_location(folder)

print(lat + " | " + long)'''

def fetch_coordinates():
    folder = fetch_id()
    print(folder)
    lat, long = fetch_location(folder)
    print(lat,long)

    return(lat, long)


