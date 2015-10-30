'''
Created on Sep 14, 2015

@author: Kevin
'''

class Binary(object):
    '''
    classdocs
    '''
    
    def __init__(self, num = None):
        '''
        Constructor
        '''
        if num is None:
            self.binNum = []
        else:
            self.binNum = decToBin(num)
        
    # Adds a number to itself
    # Number can either be an integer or another Binary object
    def add(self, num):
        try:
            int(num)
            self.add(Binary(num))
        except TypeError:
            diffSize = len(self.binNum) - len(num.binNum)
            if diffSize>0:
                num.zeropad(diffSize)
            elif diffSize<0:
                self.zeropad(-diffSize)
            carry = 0
            for ind in range(0,len(self.binNum)):
                tempsum = self.binNum[ind]+num.binNum[ind]+carry
                self.binNum[ind] = int(tempsum%2)
                carry = int(tempsum/2)
            if carry == 1:
                self.binNum.append(1)
                
    # Pad n zeros to the end            
    def zeropad(self,n):
        self.binNum.extend([0]*n)
    
    # Remove trailing zeros (i.e. most significant zeros)
    def squeeze(self):
        while self.binNum[-1]==0:
            self.binNum.pop()
            
    # Convert binary to decimal
    def toDec(self):
        self.squeeze()
        decNum = 0
        for ind in range(len(self.binNum)):
            if self.binNum[ind] == 1:
                decNum += pow(2,ind)
        return decNum
            
        
        
        
        
# Converts decimal to binary
def decToBin(num):
    binNum = []
    while num > 0:
        rem = int(num%2)
        binNum.append(rem)
        num = (num-rem)/2
    return binNum