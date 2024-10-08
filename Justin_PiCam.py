import time
from picamera2 import Picamera2, Preview
from libcamera import Transform, controls

#Create the camera 
camera = Picamera2()

#Create the configuration options for camera and set config
camera.configure(camera.create_preview_configuration())


#Set controls (Check appendecy of manual for desc and list of controls)
camera.set_controls({"Brightness": 1.0})


#Start the preview
#Use .DRM for non GUI
camera.start_preview(Preview.QTGL,x=100,y=200, width=800, height=600, transform=Transform(hflip=1, vflip=1))


#Start the camera
camera.start()


# camera.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})

#Stay in preview for how long before image is taken
time.sleep(2)
camera.capture_file("test2.jpg")