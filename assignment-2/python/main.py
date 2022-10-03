# Assignment 2 // Adrianna Deeb
# This script creates a number of toruses and saves the scene as a Maya ASCII file

# import argparse, maya standalone, and maya commands
import argparse
import maya.standalone
import maya.cmds

# creating a parser and argument for user input
parser = argparse.ArgumentParser(description='This script creates a bunch of toruses.')
parser.add_argument('num_torus', type=int, help="Number of Toruses")
args = parser.parse_args()

print("Creating {} torus(es)...".format(args.num_torus))

# initializing maya standalone
maya.standalone.initialize()

# create for loop to create toruses
for i in range(args.num_torus):
    print("Created Torus #{}".format(i))
    maya.cmds.polyTorus()

# print results
print("Meshes in the Maya scene:", maya.cmds.ls(geometry=True))

# save file as a Maya ASCII file
name = input("Name the Maya file to save: ")
maya.cmds.file( rename= name + '.ma' )
maya.cmds.file( save=True, type='mayaAscii' )

# uninitailize maya standalone to prevent it from continuing to run in the background
maya.standalone.uninitialize()