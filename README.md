# Personal Project : NFT Image Generator and Auto Uploader

Objective:
Take a folder and its subfolders that contains PNG images of different image layers.
For example a background image, body, and different accessories and features.
The program then generates an image and saves it.
Upload the images with meta data to an NFT market place.
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

Program Outline for Auto Uploader: Simple Python script to navigate Chrome and upload the images.
Lots of try-excepts to make sure the program doesn't straight up crash.
Used Selenium to navigate the pages.

Note: These programs are more of an archival thing.
While it can be used by someone else, it is not recommended.
Additionally, this project was written myself.
The images were drawn by colleagues.
While the general NFT project didn't get far, it was a valuable learning expierence to try new things.
