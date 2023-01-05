def armstrong(num, nlen, narr):
    sum = 0
    i = 0
    while i < nlen:
        sum = sum + int(narr[i])**nlen
        i+=1
    if sum == int(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is a NOT an Armstrong number")

if __name__ == '__main__':
    num = input("Enter a number: ")
    nlen = len(num)
    narr = list(num)
    armstrong(num, nlen, narr)