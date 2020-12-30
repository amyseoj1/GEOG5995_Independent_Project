"""

GEOG5995 Assessment 2:  Independent Project

Extended Deadline 12/30/2020


@author: Amy Jungmin Seo
email: jungmin.seo@postgrad.manchester.ac.uk

The goal of this project is to build a model that shows where drunks walk when 
they're trying to get home for town planning. The basic algorithm is, for each 
drunk (who will have numbers between 10 and 250 assigned before leaving the pub), 
move the drunk randomly left/right/up/down in a loop that picks randomly the way it will go. 
When it hits the correctly numbered house, stop the process and start with the next drunk. 
At each step for each drunk, add one to the density for that point on the map.


File for this project was downloaded from

https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment2/drunk.html

The raster file (300 by 300) represents the pub point and houses. The file is laid out 
at one line per image line, from top left to bottom right of the raster file. 
The pub is denoted by 1s, the houses by the numbers 10-250, and the empty spaces zeros. 
There are 25 drunks (house numbers 250, 240, 230...etc...10). 
Each drunk should be given a number before leaving the pub, and they will need to 
find the home with the same number in the town plan.

"""

import random
import numpy as np
import pandas as pd
import drunkplan_framework
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import csv


# Count the number of arguments
num_of_iterations = len(sys.argv)
print("Number of iterations: ", num_of_iterations)


# Step 1. Pull in the data file and finds out the pub point and the home points.


#   Step 1-1-1 Read txt data into data frame 
town = []
town_df = pd.read_csv('drunkplan.txt', header = None)
print(town_df)

# Creating an empty list a
rowlist = [] 

# Convering DataFrame to a list containg all the rows 
# Iterating through the rows of dataframe 
for row in town_df: 
      
    # Storing the rows into a temporary list 
    li = town_df[row].tolist() 
      
    # appending the temporary list 
    rowlist.append(li) 
    town.append(rowlist)
      
# Printing the final list 
print(town)


# visualize the town: 300 by 300

maxx = len(town_df[0]) 
maxy = len(town_df[1])

# 1-2 Find out the pub point (the pubs are denoted by 1s)

pub_rows = []
pub_cols = []
plt.imshow(town_df)

for row in range(town_df.shape[0]): 
         for col in range(town_df.shape[1]):
             if town_df.iat[row,col] == 1: # the pubs are denoted by 1s)
                 pub_rows.append(row)
                 pub_cols.append(col)
                 
                 
# 1-3 Find out the home point (the houses are denoted by 10-250)
                 
house_num = range(10,260,10) # the houses are denoted by 10-250
                 
house_rows = []
house_cols = []

for row in range(town_df.shape[0]): 
         for col in range(town_df.shape[1]):
             if town_df.iloc[row,col] in house_num: 
                 house_rows.append(row)
                 house_cols.append(col)

# Visualize location of pubs and houses

plt.scatter(pub_rows, pub_cols, color = 'green', s = 0.5)       
plt.scatter(house_rows, house_cols, color = 'red', s = 0.5)       
plt.show()       

# 3. Models the drunks leaving their pub and reaching their homes, and stores 
# how many drunks pass through each point on the map.

num_of_drunk = 25
drunk_nums = list(range(10, 260, 10))
carry_on = True


# Create the drunks.
drunk_people = []
for i in range(len(drunk_nums)):
    drunk_people.append(drunkplan_framework.Drunk(town, drunk_nums[i], house_rows[i], house_cols[i]))


# update function
counter = 0 # Set the counter equals to 0 
def update(misc):

    fig.clear()  
    global carry_on
    global counter 
    global num_of_iterations

    for drunk in drunk_people:          
        if town[drunk.y][drunk.x] == drunk:
            drunk_people.remove(drunk)
        elif town[drunk.y][drunk.x] > -1:
            drunk.steps()
            drunk.move()           
        else:
            drunk.move()
    
    
    counter += 1 # incremented the counter variable by 1
    
    if counter == (num_of_iterations):       
        for drunk in drunk_people:
            drunk.go_home()
        carry_on = False

    
    if len(drunk_people) == 0: # Stop when remaining number of drunks are 0 
        carry_on = False
        print("all drunks got home")           


# 4. Draws the density of drunks passing through each point on a map.

    plt.xlim(0, maxx)
    plt.ylim(0, maxy)
    plt.imshow(town)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title('Drunks')  
    
    for drunk in drunk_people:
        plt.scatter(drunk.x, drunk.y, s=30, color = 'pink', label = 'drunks in town') 


# 5. Saves the density map to a file as text.


def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a <= num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# Define Animation figure

fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True	

animation = animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
fig.show()

# save the density map
# writing to csv file  
with open('town_drunk.density.txt', 'w', newline='') as d_csv:
    densitymap_csv = csv.writer(d_csv, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

# writing the data rows
    for rows in town:
        # writing the data rows
         densitymap_csv.writerows(rows)  
        
