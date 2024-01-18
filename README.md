# Personal Project : Random Image Generator

Objective:
Take a folder and its subfolders that contains PNG images of different image layers.
For example a background image, body, and different accessories and features.
The program then generates an image and saves it.
There are generated sample images to understand what it created!
   

Program Outline for Image Generator:
Firstly, the program needs a parent folder.
This parent folder then has any amount of child folders where each child folder contains PNG images.
For example:
- Parent Folder
    - Child Folder 1
      - image1.png
      - image2.png
       
    - Child Folder 2
      - image1.png
      - image2.png
    - ...
    
- Firstly, the program generates an integer array where every index of the array represents the respective child folder and each integer element represents the "index" of the chosen image.
- Secondly, the progam then takes in the integer array and generates the image. It loops thru all child folders and chooses the correct image based on the current element.
- Next, the images are saves into an array of type File[] to be looped througth and layered onto a BufferedImage.
- Finally, the image is saved into the output folder.

Additionally, this code was written myself.
The images were drawn by colleagues, so much credit to them!
