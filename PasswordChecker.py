import string

from numpy import character


# print(string.ascii_letters)   > abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase) > abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase) > ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)          > 0123456789
# print(string.punctuation)     > !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


password = "ufHHEHJKJjkdkqewruqfasdf234r2t"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special    = any([1 if c in string.punctuation else 0 for c in password])
digits     = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case,lower_case,special,digits]

length = len(password)

with open('common_password.txt','r') as f:
    common = f.read().splitlines()


if password in common:
    print('Password was found in a common list')



score = 0 
if length > 8:
    score +=1
if length > 12:
    score+=1
if length > 17:
    score +=1
if length > 20:
    score +=1

print(f'password length is {str(length)}, adding {str(score)} points!')

if sum(characters) > 1:
    score+=1
if sum(characters) > 2:
    score+=1
if sum(characters) > 3:
    score+=1
if sum(characters) > 4:
    score+=1 

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)} points")


if score < 4:
    print(f"the password is quit weak! score: {str(score)}")
elif score == 4:
    print(f"the password is ok! score: {str(score)}")
elif score > 4 and score <6:
    print(f"the password is quit weak! score: {str(score)}")
elif score < 6:
    print(f"the password is strong! score: {str(score)}")