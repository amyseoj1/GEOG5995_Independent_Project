# GEOG5995_Independent_Project
# Extended Deadline 12/30/2020


<Motivation>

The goal of this assignment is to create an Agent Based Model that shows where drunks walk when they're trying to get home. 

<Steps>

1. Pull in the data file and finds out the pub point and the home points.
2. Draws the pub and homes on the screen.
3. Models the drunks leaving their pub and reaching their homes, and stores how many drunks pass through each point on the map.
4. Draws the density of drunks passing through each point on a map.
5. Saves the density map to a file as text.
6. The basic algorithm is, for each drunk (who will have numbers between 10 and 250 assigned before leaving the pub), move the drunk randomly left/right/up/down in a loop that picks randomly the way it will go. When it hits the correctly numbered house, stop the process and start with the next drunk. At each step for each drunk, add one to the density for that point on the map.

<Model Input>

A map of the town with drunks is provided the instructor from this course. It is a raster file representing the pub point and houses. The file is laid out at one line per image line, from the top left to bottom right of the raster file. The pub is denoted by 1s, the houses by the numbers 10-250, and the empty spaces zeros. There are 25 drunks (house numbers 250, 240, 230...etc...10). Each drunk should be given a number before leaving the pub, and they will need to find the home with the same number in the town plan.




