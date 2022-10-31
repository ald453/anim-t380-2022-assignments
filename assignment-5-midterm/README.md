# Assignment 5 - Midterm // Adrianna Deeb

## cameras.py

**Description**

This script creates cameras, with correct focal length and filmback size, from a CSV list gathered while on set.

**Arguments**

This script requires three arguments:

*Argument 1:* the filepath of the list of cameras that were on set. Inside the file, the following information must be presented in this order, seperated by commas:

```cameraName, focalLength, filmBackSizeX, filmBackSizeY```

Each camera must have its own line of information. Example:

``` TEST, 50, 1, 2 ```

*Argument 2:* the filepath of the framing chart image. This framing chart will be attached to each camera in maya as an image plane.

*Argument 3* the name of the Maya file to save. It will save the scene as a Maya ASCII (.ma) file.

**Example**

I successfully ran this script in the VSCode terminal. I gave these 3 arguments:

the csv list of cameras:    ``` c:\Users\adria\code\anim-t380-2022-assignments\assignment-5-midterm\etc\cameras.txt ```  

the framing chart:  ``` c:\Users\adria\Downloads\netflixframingchart.png ```  

the name of the maya file to save:  ``` testing ```  

The script created a testing.ma file in the scenes folder of my default maya project. The images folder was populated with two folders, one for each camera in my list, labeled with the camera names. Inside there was a test render displaying the framing chart. When opening the maya file, the cameras were inside as expected!