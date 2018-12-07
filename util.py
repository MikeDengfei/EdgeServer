import os
from flask import request
from py_faster_rcnn import get_net, detect_person
import os.path as osp
from Queue import Queue
from threading import Thread
import time

frame_name = Queue()      # queue of received frames
detected_person = Queue()  # queue of detected persons

data_dir = osp.abspath(osp.join(osp.dirname(__file__), 'data'))
finish1 = 0
finish2 = 0

"""
func: api of uploading the frame from end to edge server
"""
def upload_image():
    frames_dir = './data/frames/'
    frame = request.files.get('frame')
    frame.save(frames_dir+frame.filename+'.png')
    frame_name.put(frame.filename)
    print(frame_name)


def finish_upload():
    global finish1
    finish1 = 1

"""
func: detect person by applying faster-rcnn to each frame
"""
def detect():
    net = get_net('zf')
    frame_name.put('test1.jpg')
    global finish1
    while frame_name.qsize()!=0 or finish1==0:
        if frame_name.qsize()!=0:
            img_name = frame_name.get()
            detect_person(net, img_name, data_dir, detected_person)
    print(detected_person.qsize())


