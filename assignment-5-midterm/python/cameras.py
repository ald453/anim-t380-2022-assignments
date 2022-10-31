# Assignment 5 - Midterm // Adrianna Deeb
# Prompt 4 - Maya Cameras from CSV List

# This script creates cameras, with correct focal length and filmback size, from a CSV list gathered while on set. More info in the README document.

# import argparse maya commands
import argparse
import maya.cmds
import maya.standalone

# creating a parser and argument for user input
parser = argparse.ArgumentParser(description='This script creates cameras from a CSV list with the proper focal length and filmback size.')
parser.add_argument('filePath', type=str, help="File Path to the csv list of cameras on set")
parser.add_argument('chartPath', type=str, help="File Path to the framing chart image")
parser.add_argument('fileName', type=str, help="The name of the Maya file. This script will save the scene as a Maya ASCII file.")
args = parser.parse_args()

# initialize Maya standalone
maya.standalone.initialize()

# use the filepath to read the file. using readlines() will keep each camera info in its own line
with open( args.filePath , 'r' ) as f:
    lines = f.readlines()

# create a for loop to create all cameras on the list
loop = 0                # to keep track of iterations
for i in lines:
    info = lines[loop]          # get the necessary information from the correct line
    cameraName, focalLength, filmBackSizeX, filmBackSizeY = info.split(",")         # split that line up into individual variables

    # create the camera in maya and name it with the name from the csv list
    newCam = maya.cmds.camera(name=str(cameraName)) 
    # define cameraShape to make setting camera attributes easier
    cameraShape = str(newCam[1])
    
    # set the horizontal film aperture (aka horizontal film back size)
    maya.cmds.setAttr(cameraShape + ".horizontalFilmAperture", int(filmBackSizeX))
    # set the vertical film aperture (aka vertical film back size)
    maya.cmds.setAttr(cameraShape + ".verticalFilmAperture", int(filmBackSizeY))
    # set the focal length
    maya.cmds.setAttr(cameraShape + ".focalLength", int(focalLength))
    
    # make image plane and add the chart as the image
    maya.cmds.imagePlane(camera=cameraShape, lookThrough=cameraShape, showInAllViews=False, fn=str(args.chartPath))

    # set camera as renderable
    maya.cmds.setAttr(cameraShape + ".renderable", 1)
    # complete a test render
    maya.cmds.render(newCam[0]) 
    # save the render
    maya.cmds.sysFile('C:/maya/projects/default/images/' + newCam[0] +'/untitled.png', rename='C:/maya/projects/default/images/test/' + newCam[0] + '/testrender.png')

    # increment the loop variable to create the next camera
    loop = loop + 1

# save the maya file
maya.cmds.file( rename= args.fileName + '.ma' )
maya.cmds.file( save=True, type='mayaAscii' )

# close the camera list csv file
f.close()