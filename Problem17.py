'''
Created on Sep 15, 2015

@author: Kevin
'''

def numLetters(num):
    #one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
    #twenty thirty forty fifty sixty seventy eighty ninety
    #hundred thousand
    numdict = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tendict = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    letters = 0
    if num%100 < 20:
        letters += numdict[num%100]
    else:
        letters += numdict[num%10] + tendict[int(num/10)%10]
    if num>=100:
        letters += numdict[int(num/100)] + 10
        if num%100 == 0:
            letters -= 3
        
    return letters
         
        

if __name__ == '__main__':
    letSum = 0
    for num in range(1,1000):
        letSum += numLetters(num)
    letSum += 11
    print(letSum)