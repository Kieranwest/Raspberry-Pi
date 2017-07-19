import picamera
import time

camera = picamera.PiCamera()

time.sleep(5)
camera.vflip = True
camera.awb_mode = 'incandescent'
camera.framerate = 60
camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
