# Assignemnt 3 // Adrianna Deeb
# this script makes directory using an environment variable called "asset"

# import operating system 
import os

# establish the asset environment variable
asset = os.getenv("asset")

# make the directory
os.makedirs("assets/{}/maya/scenes".format(asset))
