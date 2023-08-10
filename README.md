ADOBE AITHON BETA

Repository for Binary Bots Team Beta's codebase for the Adobe AI-Thon 2023

LIBRARIES NEEDED:

ultralytics
cv2


PROBLEM STATEMENTS

1. Given an image, find the entities in the image and mark their position and likeliness (using the YOLOv8 model).
2. Count number of entities and group them by name. Report the count for each entity.
3. Group a set of images based on the entities found in them.
4. Given an example set of ideal advertisement images. Find the missing or extra entities in other images.
F5. or each entity in every image find the closest matching entities from all the images. (Crop out the matching entities and put one source entity in the folder, rest matching images in its sub folders) for all images.
Create an express page and express your learnings.

STRUCTURE

images/    --> contains images for all questions, as well as some test ones

predict.py --> contains basic model predict functionality, to be imported for use in other files

each question is solved with its own python file.

IMPORTANT NOTES:

Question 1: you can change the image in the code to get results for different mages

Question 2: similar to question 1 in changeability

Question 3: sorts all the images in the images/question_3_images folder

Question 4: Uses images/ideal folder for ideal images, and prints results on images from images/test folder

Question 5: Takes test images from images/question_5_images, and implements the structure in images/solution_5_images 

structure of solution is folder for each image

  ->folder for each entity in the image

    ->entity.png which is picture of the entity

    ->subfolder for each image from which similar entities were found
    
      ->similar entities from other image



TOOLS

YOLOv8 model -- ultralytics/ultralytics
