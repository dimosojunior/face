from django.shortcuts import render,redirect
from MyApp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
from MyApp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
	
	return render(request, 'base.html')

def home(request):
	activities = Activities.objects.all()

	context = {
		"activities":activities,
	}
	
	return render(request, 'home.html', context)
@login_required(login_url='signin')
def detect(request):
	
	return render(request, 'detect.html')
@login_required(login_url='signin')
def criminals_records(request):
	records = Records.objects.all()
	form = CriminalsSearchForm(request.POST or None)
	if request.method =="POST":
		records = Records.objects.filter(criminals__name__icontains=form['criminals'].value())

	context = {
		"records":records,
		"form": form,
	}
	
	return render(request, 'criminals_records.html', context)
@login_required(login_url='signin')
def view_criminals_records(request, id):
	records = Records.objects.get(id=id)

	context = {
		"records":records,
	}
	
	return render(request, 'view_criminals_records.html', context)
@login_required(login_url='signin')
def search_criminal_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    criminal = Criminals.objects.filter(search)
    mylist= []
    mylist += [x.name for x in criminal]
    return JsonResponse(mylist, safe=False)
@login_required(login_url='signin')
def add_criminal_records(request):
	form = AddCriminalRecordsForm()
	if request.method == "POST":
		form=AddCriminalRecordsForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			#criminal_name = request.POST['criminal_name']
			#form.criminals = criminal_name
			form.save()
			return redirect('criminals_records')

	context = {
		"form":form,

	}
	
	return render(request, 'add_criminal_records.html', context)
@login_required(login_url='signin')
def update_criminal_records(request,id):
	x = Records.objects.get(id=id)
	form = UpdateCriminalRecordsForm(instance=x)
	if request.method == "POST":
		form=UpdateCriminalRecordsForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			return redirect('view_criminals_records',id=id)

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'update_criminal_records.html', context)
@login_required(login_url='signin')
def delete_criminal_records(request,id):
	x = Records.objects.get(id=id)
	if request.method == "POST":
		
		x.delete()
		return redirect('criminals_records')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'delete_criminal_records.html', context)

@login_required(login_url='signin')
def add_criminal(request):
	form = AddCriminalForm()
	if request.method == "POST":
		form=AddCriminalForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('all_criminals')

	context = {
		"form":form,

	}
	
	return render(request, 'add_criminal.html', context)
@login_required(login_url='signin')
def all_criminals(request):
	criminals = Criminals.objects.all().order_by('-id')
	form = AllCriminalsSearchForm(request.POST or None)
	if request.method =="POST":
		criminals = Criminals.objects.filter(name__icontains=form['name'].value())

	context = {
		"criminals":criminals,
		"form": form,
	}
	
	return render(request, 'all_criminals.html', context) 
@login_required(login_url='signin')
def update_criminal(request,id):
	x = Criminals.objects.get(id=id)
	form = UpdateCriminalForm(instance=x)
	if request.method == "POST":
		form=UpdateCriminalForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			return redirect('all_criminals')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'update_criminal.html', context)

@login_required(login_url='signin')
def delete_criminal(request,id):
	x = Criminals.objects.get(id=id)
	if request.method == "POST":
		
		x.delete()
		return redirect('all_criminals')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'delete_criminal.html', context)  
@login_required(login_url='signin')
def face_detection(request):
	import cv2
	import numpy as np
	import pickle
	#from . import face_train

	import os
	from PIL import Image
	
	

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))

	# Load the cascade
	face_cascade = cv2.CascadeClassifier(BASE_DIR +'/haarcascade_frontalface_default.xml')

	#eye_cascade = cv2.CascadeClassifier('haarcascade_frontalface_eye.xml')

	#smile_cascade = cv2.CascadeClassifier('haarcascade_frontalface_smile.xml')

	recorgnizer = cv2.face.LBPHFaceRecognizer_create()
	#recorgnizer.read("trainner.yml")


#MWANZO WA MODEL YA KUTRAIN FACE
	


	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	image_dir = os.path.join(BASE_DIR, "media")
	#print(BASE_DIR)
	#print(image_dir)

	#face_cascade = cv2.CascadeClassifier('C:\\Users\\DIMOSO EL JUNIOR\\Desktop\\DjangoFaceDetection\\OpencvProject\\MyApp\\haarcascade_frontalface_default.xml')
	face_cascade = cv2.CascadeClassifier(BASE_DIR +'/haarcascade_frontalface_default.xml')
	#print(face_cascade)


	recorgnizer = cv2.face.LBPHFaceRecognizer_create()


	current_id = 0
	label_ids = {}
	y_labels =[]
	x_train = []
	for root, dirs, files in os.walk(image_dir):

		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				path = os.path.join(root, file)

				label = os.path.basename(root).replace(" ","-").lower()

				print(label, path)

				if not label in label_ids:
					label_ids[label] = current_id
					current_id += 1
					
				id_ = label_ids[label]
				#print(label_ids)
				#y_labels.append(label) #some numbers for label
				#x_train.append(path) #verify this image
				pil_image = Image.open(path).convert("L")


				size =(550, 550)
				final_image = pil_image.resize(size, Image.ANTIALIAS)




				image_array = np.array(final_image, "uint8")
				# print(image_array)

				faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
				for (x, y, w, h) in faces:
					# print(x,y,w,h)
					roi = image_array[y:y+h, x:x+w]
					x_train.append(roi)
					y_labels.append(id_)

	with open("labels.pickle", 'wb') as f:
		pickle.dump(label_ids, f)

	recorgnizer.train(x_train, np.array(y_labels))
	#recorgnizer.save("C:\\Users\\DIMOSO EL JUNIOR\\Desktop\\DjangoFaceDetection\\OpencvProject\\MyApp\\trainner.yml")
	recorgnizer.save(BASE_DIR +"/trainner.yml")


	#MWISHO WA MODEL YA KUTRAIN FACE





	labels = {"person_name": 1}
	with open("labels.pickle", 'rb') as f:
		og_labels = pickle.load(f)
		labels = {v:k for k,v in og_labels.items()}




	cap = cv2.VideoCapture(1)

	userId = 0
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
				name = "DETECTED" #labels[id_]
				
				color = (255,255,255)
				stroke = 2
				userId = id_
				cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
				#cv2.putText(frame, "DETECTED", (x,y), font, 1, color, stroke, cv2.LINE_AA)
			else:
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = "UNKNOWN" #labels[id_]
				
				color = (255,255,255)
				stroke = 2
				cv2.putText(frame, name,  (x,y), font, 1, color, stroke, cv2.LINE_AA)



			#img_item = "C:\\Users\\DIMOSO EL JUNIOR\\Desktop\\DjangoFaceDetection\\OpencvProject\\MyApp\\static\\MyApp\\criminalsImages\\myimage.png"
			img_item = BASE_DIR +"/static/MyApp/criminalsImages/myimage.png"
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

		elif(userId != 0):
			cv2.waitKey(1000)
			cap.release()
			cv2.destroyAllWindows()
			#return redirect('/records/details/'+str(userId))
			#return redirect('criminals_records')
			return redirect('welcome')
			#return redirect('welcome')
	#when everything done release the capture
	cap.release()
	cv2.destroyAllWindows()
	return redirect('detect')


def welcome(request):
	
	return render(request, 'welcome.html')

