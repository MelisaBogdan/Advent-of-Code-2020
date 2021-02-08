file=open('inputDay4.txt')
passport= file.readlines()
passport=[line.strip() for line in passport]    #eliminating spaces before and afterwards
fields=['pid', 'ecl', 'hcl', 'hgt', 'eyr', 'iyr', 'byr']
choises=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

#functions used

def valid_passport(p):
    for field in fields:
            if field not in currentP:
                return False
    return True

def valid_data(p):
    #split the data into each field and its values afterwards
    p=p.split()
    data={}
    for i in p:
        key = i[:3]      #byr, hgt etc
        value= i[4:]
        data[key]=value     # dictionary with the values we have to check
    print(data)
    if not valid_byr(data['byr']):
        print(1)
        return False
    if not valid_iyr(data['iyr']):
        print(2)
        return False
    if not valid_eyr(data['eyr']):
        print(3)
        return False
    if not valid_hgt(data['hgt']):
        print(4)
        return False
    if not valid_hcl(data['hcl']):
        print(5)
        return False
    if not valid_ecl(data['ecl']):
        print(6)
        return False
    if not valid_pid(data['pid']):
        print(7)
        return False
    return True
    


# break-down functions used in valid_data
#---------------------------------------------
    
def valid_pid(pid):
    if len(pid)!=9: return False #and pid[0]==pid[1]==0: return True
    return True

def valid_ecl(ecl):
    e=ecl
    if e in choises: return True
    return False


def valid_hcl(hcl):
    h=hcl
    if h[0]!='#':   return False        #must start with # key
    if len(h[1:])!=6:  return False     #if it doesn't have the 6 character afterwards
    return True
    

def valid_hgt(hgt):
    nr=int(hgt[:-2])                                #height in digits
    typee=hgt[-2:]                                  #cm or in
    if typee not in ['in', 'cm']: return False      #unknown type therefore not valid
    if typee=='cm':
        if nr<150 or nr>193:    return False                                     
        
    if typee=='in':
        if nr<59 or nr>76:    return False

    return True

def valid_eyr(eyr):
    if int(eyr)>=2020 and int(eyr)<=2030: return True
    return False

def valid_iyr(iyr):
    if  int(iyr)>=2010 and int(iyr)<=2020:  return True
    return False

def valid_byr(byr):
    if int(byr)>=1920 and int(byr)<=2002: return True
    return False

#--------------------------------------------------------------------

count=0                                         #counting valid passwords
validpassports=[]                               #list of valid passports                                     
currentP=' '
#building  passports
for line in passport:
    if line!= '' :                              #new passports are separated by empty line
        currentP+=' ' +line                      #so we stop when we meet one
    else:                                        #end of current passport
        #print(currentP)
        if valid_passport(currentP):
            count+=1
            validpassports.append(currentP)
        currentP= ''

#for the last set of passports
if valid_passport(currentP)==True:
    count+=1
    validpassports.append(currentP)


count=0
#print(validpassports)
for p in validpassports:
    if valid_data(p):
        print("yay")
        count+=1
        
print(count)

