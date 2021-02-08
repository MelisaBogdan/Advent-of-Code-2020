#--- Part Two ---
#Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

#Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.

#In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
#What do you get if you multiply together the number of trees encountered on each of the listed slopes?


file=open('inputDay3.txt')
mapp=file.readlines()
mapp=[line.strip() for line in mapp]        #getting rid of spaces before and after each line

count=0                                     #no. of trees
row=0                                       #current row
col=0                                       #current column

while row+1<len(mapp):                      #checking if next row we are about to jump to exists
    row+=1
    col+=3
                                            #geting the character on pos row,col (either . or #)
    c=mapp[row][col % len(mapp[row])]       #just % no of columns when it gets out of bounds ex: max 32 columns, col=37 so its equivalent to column 5
    if c=='#': count+=1

result=count                                #we add to the result

#WE REPEAT THE PROCESS FOR OTHER SLOPES (PATHS)
#----------------------------------------------------------------------------------------------------------#

count=0    #no. of trees
row=0      #current row
col=0      #current column

while row+1<len(mapp):      
    row+=1
    col+=1
    c=mapp[row][col % len(mapp[row])]       
    if c=='#': count+=1
    
result*=count

#----------------------------------------------------------------------------------------------------------#
count=0    
row=0      
col=0

while row+1<len(mapp):     
    row+=1
    col+=5
    c=mapp[row][col % len(mapp[row])]       
    if c=='#': count+=1

result*=count

#----------------------------------------------------------------------------------------------------------#
count=0    
row=0      
col=0        

while row+1<len(mapp):      
    row+=1
    col+=7
    c=mapp[row][col % len(mapp[row])]       
    if c=='#': count+=1

result*=count

#----------------------------------------------------------------------------------------------------------#
count=0    
row=0      
col=0        

while row+1<len(mapp):      
    row+=2
    col+=1
    c=mapp[row][col % len(mapp[row])]       
    if c=='#': count+=1

result*=count

print(result)

