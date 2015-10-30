'''
Created on Sep 15, 2015

@author: Kevin
'''

import re

def parseNums(in_Str):
    return [int(x) for x in re.findall('\d+',in_Str)]

if __name__ == '__main__':
    # Open file
    #f = open('Problem18Data.txt','r')
    f = open('p067_triangle.txt')
    
    # Initialize tracker
    tracker = parseNums(f.readline())
    
    # Loop through each line in the file
    while True:
        # Read next line
        nextLine = f.readline()
        
        # If empty, break
        if not nextLine:
            break
        # Else parse into array
        else:
            nextData = parseNums(nextLine)
            
        # Find the largest path for each node given
        pathLeft = [tracker[ind]+nextData[ind] for ind in range(0,len(tracker))] + [0] 
        pathRight = [0] + [tracker[ind]+nextData[ind+1] for ind in range(0,len(tracker))] 
        tracker = [max(pathLeft[ind],pathRight[ind]) for ind in range(len(pathLeft))]
        
    # Find max and output
    print(max(tracker))