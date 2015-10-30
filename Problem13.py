'''
Created on Sep 14, 2015

@author: Kevin
'''
import functions.binary as binary

f = open('Problem13Data.txt','r')
print(f)
data = f.readline()
binSum = binary.Binary(int(data))
data = f.readline()
while True:
    binSum.add(binary.Binary(int(data)))
    data = f.readline()
    if not data:
        break
print(binSum.toDec())
    

if __name__ == '__main__':
    pass