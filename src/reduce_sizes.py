#!/usr/bin/python3

import os
import subprocess
import sys

usage='''Usage: reduce_sizes.py [picture folder] [output folder]
jpegoptim needs to be in your PATH
2019 Johannes Hausmann'''


if len(sys.argv) < 3:
    print(usage)
    quit()

else:
    print("=====" * 3)

try:

    subprocess.check_call(['command','-v','jpegoptim'],shell=True)

except subprocess.CalledProcessError:
    print("Error. Please add jpegoptim to your path")
    quit()

inputdir = os.path.realpath(sys.argv[1])
outputdir = os.path.realpath(sys.argv[2])

quality = "90"

filenames = []


if os.path.isdir(inputdir) and os.path.isdir(outputdir):
    for entry in os.scandir(inputdir):
        if entry.is_file() and entry.name.endswith(".jpg"):
            filenames.append(os.path.join(inputdir,entry))
else:
    print("Error. input or output dir doesn't exists")
    quit()


for filename in sorted(filenames):
    subprocess.call(['jpegoptim','-m ' + str(quality) ,'-p', '--all-progressive' ,'-d', str(outputdir), str(filename)])
