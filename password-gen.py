import random
import string

lowerReq = input('Please enter in the number of lowercase letters needed: ')
upperReq = input('Please enter in the number of Uppercase letters needed: ')
specicalChar = input('Please enter in the number of Special Characters needed:')
digitReq = input('Please enter in the number of digits needed: ')

generatedPass = []

def lowerCaseGen():
    tempRand = random.choice(string.ascii_lowercase)
    return str(tempRand)

def upperCaseGen():
    tempRand = random.choice(string.ascii_uppercase)
    return str(tempRand)
    
def specicalCharGen():
    tempRand = random.choice('!@#$%^&*?') 
    return str(tempRand)

def randDigitGen():
    tempRand = random.choice(string.digits)
    return str(tempRand)

for i in range(0,int(lowerReq)):
    generatedPass.append(lowerCaseGen())

for i in range(0, int(upperReq)):
    generatedPass.append(upperCaseGen()) 

for i in range(0, int(specicalChar)):
    generatedPass.append(specicalCharGen())

for i in range(0, int(digitReq)):
    generatedPass.append(randDigitGen())

random.shuffle(generatedPass)

print(''.join(generatedPass))
