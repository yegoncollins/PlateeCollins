"""
test, parsing cv2 to browser -->> test passed
build skeleton for running in browser, not the native commandline

"""
from flask import Flask, render_template, Response
import cv2, numpy as np
face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt2.xml')
app = Flask(__name__)

camera = cv2.VideoCapture(0)

def gen_frames():
	
	while True:
		success, frame = camera.read()
		imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		Funner = face_cascade.detectMultiScale(frame, scaleFactor = 1.06, minNeighbors = 5, minSize = (30, 30))
		for x, y, width, height in Funner:
			cv2.rectangle(frame, (x, y), (x + width, y + height), color = (0,0,255), thickness = 2)

		ret, buffer = cv2.imencode('.jpg', frame)
		
		imgray = buffer.tobytes()
		yield (b'--imgray\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + imgray + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=imgray')

@app.route('/')
def index():
	"""Video streaming home page."""
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)