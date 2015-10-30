'''
Created on Sep 16, 2015

@author: Kevin
'''

if __name__ == '__main__':
    # loop through factorial manually and remove 10s
    
    noTenFact = 1
    
    for ind in range(2,101):
        noTenFact *= ind
    print(sum([int(x) for x in str(int(noTenFact))]))