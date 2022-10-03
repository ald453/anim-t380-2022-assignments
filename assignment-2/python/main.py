# Assignment 2 // Adrianna Deeb
# STILL A WORK IN PROGRESS

# import argparse, maya standalone, and maya commands
import argparse
import maya.standalone
import maya.cmds

# creating a parser and argument for user input
parser = argparse.ArgumentParser(description='This script creates a bunch of toruses.')
parser.add_argument('num_torus', type=int, help="Number of Toruses")
args = parser.parse_args()

print("Creating {} cube(s)...".format(args.num_torus))

# initializing maya standalone
maya.standalone.initialize()

# create for loop to create toruses
for i in range(args.num_torus):
    print("Created Torus #{}".format(i))
    maya.cmds.polyTorus()

# print results
print("Meshes in the Maya scene:", maya.cmds.ls(geometry=True))

# save file as a Maya ASCII file
maya.cmds.file((input("Name the Maya File to save")) + ".ma")
maya.cmds.file(save=True, type='mayaAscii')
