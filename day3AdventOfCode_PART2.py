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

