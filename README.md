# Personal Project : NFT_Image_Generator

Objective: Take a folder of folders that contains PNG images of different parts.
For example a background image, body, and different accessories and features.
The program then generates an image and saves it.
There are generated sample images to understand what it created!

Program Outline: Firstly, the program needs a parent folder.
This parent folder then has any amount of child folders where each child folder contains PNG images.
For example:
- Parent Folder
    - Child Folder 1
    - Child Folder 2
    - ...
    
Firstly, the program reads the amount of child folders and create an array with x many elements.

Secondly, it iterates through every child folder and randomaly choose an "attribute".
Each index in the array represents the child folder and each element is an integer representing the "index" of the chosen attribute.
Next, it generates an image from the integer array.
The program goes thru the child folders and saves the according image from the array to an array of files.
Finally, it renders the image by layering it and saves it.

Note: The program is more of an archival thing.
While it can be used by someone else, it is not recommended.
Additionally, this project was written myself.
The images were drawn by colleagues who also wanted to try to get into the crypto scene.
While the general NFT project didn't get far, it was a valuable learning expierence to try new things.
