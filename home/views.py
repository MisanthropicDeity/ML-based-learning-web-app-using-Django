from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import base64
import numpy as np
from PIL import Image
import cv2
import io
import matplotlib.pyplot as plt
import tensorflow as tf

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    y=cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    f = open("demofile2.txt", "w")
    f.write(str((np.array(image)).tostring()))
    f.close()
    return y




def home(request):
	
	return render(request,'home/home1.html')

def proc(request):
	print("this is first")
	if request.method == 'POST':
		img = request.POST['imgBase64']

		# print ("python")
		# print (img)
	if request.is_ajax():
		message = "Yes, AJAX!"
		print("this is se")
	else:
		message = "Not Ajax"
		print("this is sec")
	print("this is second")
	return HttpResponse("")

def getImg(request):
	print("this is first")
	if request.method == 'POST':
		img = request.POST['imgBase64']
		string_val = img[22:]
		print (string_val)
		np_arr = stringToRGB(string_val)
		
		print (type(np_arr))
		print (len (np_arr))
		print ("No. of dimensions: ", np_arr.ndim)
		print ("Shape of array: ", np_arr.shape)
		print ("Size of array: ", np_arr.size)

		arr = cv2.resize(np_arr,dsize=(28,28), interpolation=cv2.INTER_LINEAR)

		print ( type (arr) )
		print ( len (arr) )

		print ("No. of dimensions: ", arr.ndim)
		print ("Shape of array: ", arr.shape)
		print ("Size of array: ", arr.size)
		plt.imshow(arr, cmap=plt.get_cmap('gray'))
		arr =arr/255
		pred=model.predict(img)
		print (pred)
		# print (np_arr.shape())

		print (arr)

		print ("python")
		
		#print (img)

		print ("python")

		return HttpResponse('done')

model=tf.keras.models.load_model('/home/deity/Documents/django/char_prediction/home/first_model')
def get_img(request):
	if request.method=="POST":
		img = request.POST['imgBase64']
		base64str=img[22:]
		b =bytes(base64str, "utf-8")
		print (base64str)

		with open("image.png","wb") as fh:
			fh.write(base64.decodebytes(b))

	img=cv2.imread('image.png',0)
	img=cv2.bitwise_not(img)
	img=cv2.resize(img,(28,28))
	img=np.array(img)
	print(img.shape)
	img=np.reshape(img,(-1,28,28))
	#img=img.reshape(1,28,28,1)
	#img=img.astype('float32')
	img=img/255.0
	pred=model.predict(img)
	print (pred)
	val = np.argmax(pred)
	print (val)

	return HttpResponse('done')