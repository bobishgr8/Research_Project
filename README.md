# Research_Project

This is all the code that i used for a NJ E-StAR research project. The main aim of the project is to develop a facial recognition system that can be used as a web authenticator.

You can check out the "SSEF poster final.pdf" for a look at the overall project. 

## Task 1

For this task, I needed to model an image in a math operable and computer understandable object. Therefore the bulk of the code here is to change the images into matrixes. 

## Task 2

In this task, the main goal is to find if 2 matrixes are the same. So no biggie.
Was mainly just:
> if matrix1 == matrix2 : 

## Task 3

In this task, it is to see if a computer is able to understand that the 2 images are the same but are slightly edited. For example, both shows the Eiffel Tower, but one is a image of it in day time while the other on is in night time.

## Yale test

Inside this is where we test the ideas of Task 3 onto the yale faces dataset. Main method used was k-Nearest Neighbor. Later versions included a feature extractor.

## Web login form

The code for the scaled up FRS for the web server.