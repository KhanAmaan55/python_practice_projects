"""
s = $
a = @
i = !
l = |
o = 0
c = (
and = &
"""
SECURE = (('s', '$'), ('and', '&'),('a', '@'), ('o', '0'), ('i', '!'), ('l', '|'),('c','('))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password
password = input("Enter Your password: ")
password = securePassword(password)
print(f"Your secured password is {password}")