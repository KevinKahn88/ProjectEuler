'''
Created on Sep 14, 2015

@author: Kevin
'''

class Collatz(object):
    
    def __init__(self):
        self.seqHash = {}
        self.lenHash = {}
        self.lenHash[1]=1
        
    def sequence(self,num):
        try:
            return self.lenHash[num]
        except KeyError:
            if num%2 == 0:
                nextNum = int(num/2)
            else:
                nextNum = 3*num+1
            self.seqHash[num] = nextNum
            self.lenHash[num] = self.sequence(nextNum)+1
            return self.lenHash[num]
                


if __name__ == '__main__':
    collatzSequence = Collatz()
    maxScore = 0
    maxInd = -1
    for ind in range(1,1000000):
        if ind%10000 == 0:
            print(ind)
        if collatzSequence.sequence(ind)>maxScore:
            maxInd=ind
            maxScore = collatzSequence.sequence(ind)
    print(maxInd)
    print(maxScore)