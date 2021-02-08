file=open('inputDay4.txt')
passport= file.readlines()
passport=[line.strip() for line in passport]    #eliminating spaces before and afterwards
#print(passport)


fields=['pid', 'ecl', 'hcl', 'hgt', 'eyr', 'iyr', 'byr']

count=0                             #counting valid passwords
currentP=' '

def valid_passport(p):
    for field in fields:
            if field not in currentP:
                return False
    return True

#building each passport
for line in passport:
    if line!= '' :                   #new passports are separated by empty line
        currentP+='' +line          #so we stop when we meet one
    else:                           #end of current passport
        if valid_passport(currentP)==True:
            count+=1
        currentP= ''

#for the last set of passports
if valid_passport(currentP)==True:
    count+=1

print(count)
