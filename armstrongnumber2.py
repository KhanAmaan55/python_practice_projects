from unicodedata import digit


def armstrong(num, nlen):
    sum = 0
    temp = num
    while(temp !=0):
        digit = temp % 10
        sum = sum + (digit**nlen)
        temp = temp//10
    
    if sum == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is a NOT an Armstrong number")

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    nlen = len(str(num))
    armstrong(num, nlen)