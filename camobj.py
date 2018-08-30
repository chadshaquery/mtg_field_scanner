import base64
import time
import sys
#if sys.version_info[0] < 3: 
#	from urllib2 import request as urlopen
#	import cv
#	import cv2
#else:
import cv2
#	from urllib.request import urlopen
#	import cv2.cv
import numpy as np
from skimage import io

"""
Examples of objects for image frame aquisition from both IP and
physically connected cameras
Requires:
 - opencv (cv2 bindings)
 - numpy
"""


class ipCamera(object):
	def __init__(self, url, user=None, password=None):
		self.url = url
#		auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1] self.req = io.imread(self.url) self.req.add_header('Authorization', 'Basic %s' % auth_encoded)

	def get_frame(self):
		#response = urllib2.urlopen(self.url)
		#img_array = np.array(bytearray(response.read()), dtype=np.uint8)
		#frame = cv2.imdecode(img_array,-1)
		img = io.imread(str(self.url,"shot.jpg"))
#		img = cv2.cv.fromarray(img)
		frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		return frame


class Camera(object):
	def __init__(self, camera=0):
		self.cam = cv2.VideoCapture(camera)
		if not self.cam:
			raise Exception("Camera not accessible")

		self.shape = self.get_frame().shape

	def get_frame(self):
		_, frame = self.cam.read()
		return frame
