#!/usr/bin/env python3
import os
import sys
import subprocess
import librosa
import math

usage='''
Usage: slideshow.py [input dir] [audiotrack] [output] 
slideshow will take a picture folder and an audio file to create a simple slideshow
slideshow.py will set the framerate automatically according to the audio length.
'''

try:
    subprocess.check_call(['ffmpeg','-h'])

except subprocess.CalledProcessError:
    print("Please install the ffmpeg")

if len(sys.argv) < 4:
    print(usage)
    quit()

files =[]

inputdir=os.path.realpath(sys.argv[1])
output=sys.argv[3]

audiofile=os.path.realpath(sys.argv[2])
audiolength=(librosa.get_duration(filename=str(audiofile)))


with os.scandir(inputdir) as dir:
    for entry in dir:
        if entry.is_file():
            files.append(os.path.join(inputdir,entry))

framerate = round((len(files) / audiolength),1)

with open('file.txt','w') as f:
    for entry in sorted(files):
        f.write("file "+'\''+ entry+'\''+'\n')


# create commmand
command='ffmpeg'
options= ' '.join([
    '-r', str(framerate),
    '-f', 'concat', '-safe 0',
    '-i','file.txt',
    '-i', str(audiofile), '-acodec copy',
    '-vsync', 'vfr', output
    ])
process=(' '.join([command,options]))
    
print(process + '''
        -----''' *4)
subprocess.call([process],shell=True)

