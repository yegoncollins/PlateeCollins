from flask import Flask, render_template, Response, Blueprint
import cv2

#: app = Flask(__name__)

app_old_bp = Blueprint("app_old_bp", __name__, template_folder="templates")

camera = cv2.VideoCapture('./test2.mp4')  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app_old_bp.route('/video_feed', methods=["GET"])
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

"""
@app_old_bp.route('/')
def index():
    #: Video streaming home page.
    return render_template('sign_up.html')
"""

