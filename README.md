# GEOG5995_Independent_Project
# Extended Deadline 12/30/2020


Motivation


Model outputs 






Project ideas Broadly speaking, your project should:  
- Read in some data. 
- Process it in some way. 
- Display the results. 
- Write the results to a file.


Imagine you are in control of town planning, and your town is full of drunks. You need to build a model that shows where drunks walk when they're trying to get home.

You have a map of the area in a file, that contains the pub from which all the town's drunks spew out at night. You also have a map of all their homes. Essentially any given drunk will leave the pub and wonder randomly around until they hit their home.

(Strangely, though I put 'modelling drunks for planning' together as a joke a few years ago, someone has now actually done this).

Build a program to do the following...

Pull in the data file and finds out the pub point and the home points.
Draws the pub and homes on the screen.
Models the drunks leaving their pub and reaching their homes, and stores how many drunks pass through each point on the map.
Draws the density of drunks passing through each point on a map.
Saves the density map to a file as text.
The basic algorithm is, for each drunk (who will have numbers between 10 and 250 assigned before leaving the pub), move the drunk randomly left/right/up/down in a loop that picks randomly the way it will go. When it hits the correctly numbered house, stop the process and start with the next drunk. At each step for each drunk, add one to the density for that point on the map.

Additional marks are awarded for the following.

Stopping the drunks from retracing their steps, or other ways of helping them find their way home.

Files for this project.

1 (300 by 300) raster file representing the pub point and houses. The file is laid out at one line per image line, from the top left to bottom right of the raster file. The pub is denoted by 1s, the houses by the numbers 10-250, and the empty spaces zeros. There are 25 drunks (house numbers 250, 240, 230...etc...10). Each drunk should be given a number before leaving the pub, and they will need to find the home with the same number in the town plan.

300 x 300 pixel raster file of the town plan: drunk.plan (GIF version for comparison - this should not be used in the project). Each line in the file is a line in the raster image, starting at the top left corner. The backgroung is denoted by the number zero, the pub by one's, and the houses by the other numbers.
