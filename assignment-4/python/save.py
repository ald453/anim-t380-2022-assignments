# Assignment 4 // Adrianna Deeb
# This script increments the version of a file and saves it with the proper naming convention

# importing argparse and maya commands
import argparse
import maya.cmds
import maya.standalone

# creating a parser and argument for user input
parser = argparse.ArgumentParser(description='This script increments the version of a file and saves it with the proper naming convention.')
parser.add_argument('fileName', type=str, help="File Name, following the proper naming convention order: asset.task.artist.version.extension")
args = parser.parse_args()

# initalize maya standalone
maya.standalone.initialize()

# split the file name into parts
asset, task, artist, version, extension = args.fileName.split(".")
# print statements to test along the way
print(asset)
print(task)
print(artist)
print(version)
print(extension)

# increment the version number
version = int(version) + 1     # change version to an integer to complete math
version = str(version)         # change it back in order to save
# print statement to test along the way
print(version)

# save the file
maya.cmds.file(rename= "{}.{}.{}.{}.{}".format(asset, task, artist, version, extension))  # putting the parts back together in order to save
maya.cmds.file(save=True, type='mayaAscii')
print("{}.{}.{}.{}.{} now saved".format(asset, task, artist, version, extension))
