import face_recognition

image = face_recognition.load_image_file("002.jpeg")
face_locations = face_recognition.face_locations(image)

# [(98, 469, 284, 283)]
print(face_locations)
