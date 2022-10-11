# Assignment 3 // Adrianna Deeb
# this script creates an empty group in Maya

# import operating system, maya standalone, and maya commands
import os
import maya.standalone
import maya.cmds

# establish the asset environment variable
asset = os.getenv("asset")

# create the empty group using the asset name from the argument
maya.cmds.group( em=True, name=asset )