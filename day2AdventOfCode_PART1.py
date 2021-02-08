import csv

file=open('inputDay2part1.txt')
Lines=csv.reader(file, delimiter= ' ')
count=0

for line in Lines:
    maxmin, letter, word = line[0], line[1][0], line[2]
    limit= maxmin.index('-')
    
    low=int(maxmin[:limit])             #digits before '-'
    up=int(maxmin[limit+1:])            #digits after '-'

    ct=0
    for char in word:                   #increase the counter variable every time we find the letter in the word
        if char ==letter: ct+=1

    if ct>= low and ct<=up: count+=1

print(count)


