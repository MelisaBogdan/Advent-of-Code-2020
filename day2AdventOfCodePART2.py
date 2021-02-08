import csv

file=open('inputDay2part1.txt')
Lines=csv.reader(file, delimiter= ' ')
count=0

for line in Lines:
    maxmin, letter, word = line[0], line[1][0], line[2]
    limit= maxmin.index('-')
    
    low=int(maxmin[:limit])             #digits before '-'
    up=int(maxmin[limit+1:])            #digits after '-'


    if (letter==word[low-1] and not letter==word[up-1]) or (not letter==word[low-1] and letter==word[up-1]):
        count+=1


print(count)
