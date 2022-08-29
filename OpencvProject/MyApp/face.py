import cv2
import numpy as np
import pickle

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_frontalface_eye.xml')

#smile_cascade = cv2.CascadeClassifier('haarcascade_frontalface_smile.xml')

recorgnizer = cv2.face.LBPHFaceRecognizer_create()
recorgnizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}




cap = cv2.VideoCapture(0)

while True:
	#capture frame by frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		#Recognizer
		id_, conf = recorgnizer.predict(roi_gray)

		if conf >= 45 and conf <= 85:
			#print(id_)
			#print(labels[id_])

			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			color = (255,255,255)
			stroke = 2
			cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)



		img_item = "savedImages/myimage.png"
		cv2.imwrite(img_item, roi_gray)

		#Draw rectangle
		color = (255, 0, 0)
		stroke = 5
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color,stroke)

		#eyes = eye_cascade.detectMultiScale(roi_gray)
		#for (ex,ey,ew,eh) in eyes:
			#cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)

		#smiles = smile_cascade.detectMultiScale(roi_gray)
		#for (ex,ey,ew,eh) in smiles:
			#cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)


	#Display te resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
#when everything done release the capture
cap.release()
cv2.destroyAllWindows()

