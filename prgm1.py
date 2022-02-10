import sys
fp=open(sys.argv[1]) 
word=0
for data in fp:
    l=data.split()
    for i in l:
        word+=1
print('Total No. of words:',word)