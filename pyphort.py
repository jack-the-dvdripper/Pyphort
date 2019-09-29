#!/usr/bin/python3

""" small python utility to sort pictures into albums
YYYY/MM/DD like 2019/07/06 based on exif metadata
"""

from datetime import datetime
from exif import Image
import os
import sys
import shutil 


def checkdir(path):
	return(os.path.isdir(path))

''' os.makedirs(path) → similar to mkdir -p path (shell)'''
def createalbum(path):
	try:
		os.makedirs(path)
		print("path " + path + " " +"created")
	except OSError:
		print("Creation of %s failed" % path)
		


'''picture format that supports exif metadata'''
file_extension=('.jpg','.JPG','.jpeg','.webp','.tiff','.TIF')

filepaths=[]

if len(sys.argv) < 3 :
	print("Usage: " + sys.argv[0] + " image_folder (input)" + " " + " output_folder")
	print("developed by Johannes Hausmann")
	quit()

else:
	print (sys.argv[0])
	print ("--> scanning " + sys.argv[1] + " for pictures to sort")


''' scann input dir for images'''

with os.scandir(sys.argv[1]) as indir:
	for entry in indir:
		file=str(entry.name)
		if entry.is_file():
			if file.endswith(file_extension):
				filepaths.append(os.path.join(sys.argv[1],file))
				
		else:
			print (file + " not supported by pyphort")
			continue	

''' retrieve exif information from images'''
if len(filepaths) > 0:
	
	for file in filepaths:
		image_file=open(file,'rb')
		image=Image(image_file)
		''' check for exif data '''
		if image.has_exif:
			image_time=datetime.strptime(str(image.datetime_original),'%Y:%m:%d %H:%M:%S')
			album_path=os.path.join(str(sys.argv[2]), str(image_time.year), str(image_time.month), str(image_time.day))
			
			if checkdir(album_path): 
				shutil.copy(file,album_path)
				print (file + " --> " + album_path)
			
			else: 
				createalbum(album_path)
				shutil.copy(file,album_path)
				print (file + " --> " + album_path)

else:
    print("No pictures to sort into albums.")




