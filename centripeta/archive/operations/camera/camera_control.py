import os
import sys
import inspect

HERE = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_path = os.path.join(HERE, "..", "..")
op_path = os.path.join(HERE, "..")

sys.path.append(root_path)
sys.path.append(op_path)

from base_layer.camera import camera_setup

class CameraControl(object):
    def __init__(self):
        pass

    #Records the video and saves it as an avi file
    def record(self, video_name, duration):
        print("Taking video...")
        camera_setup.record_video(video_name, duration)

    # Take an image
    def take_image(self, save_loc):
        print("Taking image...")
        camera_setup.take_image(save_loc)
