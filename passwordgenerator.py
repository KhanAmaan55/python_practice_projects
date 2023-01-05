import string
import random
s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
temp =  1
passlen = int(input("Enter the length of the password: "))
password = ''
userchoice = int(input("Do You Want punctuations/symbols in the password?\nPress\t1 for Yes\t 2 for No\n"))
if userchoice == 1:
    while temp<=passlen:
        i = random.randint(0, (len(s1)-1))
        j = random.randint(0, (len(s2)-1))
        k = random.randint(0, (len(s3)-1))
        if temp%2 ==0:
            passletter = s1[i]
        elif temp%3 ==0:
            passletter = s3[k]
        else:
            passletter = s2[j]
        password = password+passletter
        temp+=1
else:
    while temp<=passlen:
        i = random.randint(0, (len(s1)-1))
        j = random.randint(0, (len(s2)-1))
        if temp%2 !=0:
            passletter = s1[i]
        else:
            passletter = s2[j]
        password = password+passletter
        temp+=1

print(f"Generated password is {password}")