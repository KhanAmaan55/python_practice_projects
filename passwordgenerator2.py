import string
import random

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation

alpha = list(s1 + s2 + s3)
beta= list(s1 + s2)
passlen = int(input("Enter the length of the password: "))
userchoice = int(input("Do You Want punctuations/symbols in the password?\nPress\t1 for Yes\t 2 for No\n"))

if userchoice == 1:
    # random.shuffle(alpha)
    # print("Generated Password is ","".join(alpha[0:passlen]))
    print("Generated Password is ","".join(random.sample(alpha , passlen)))
else:
    # random.shuffle(beta)
    # print("Generated Password is ","".join(beta[0:passlen]))
    print("Generated Password is ","".join(random.sample(beta , passlen)))