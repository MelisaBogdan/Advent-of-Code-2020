'''
--- Part Two --- DAY 4
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
'''

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

