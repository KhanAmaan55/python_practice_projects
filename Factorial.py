def fact(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num*fact(num-1)

def count_digits(num):
   factorial = fact(num)
   count = 0
   while (factorial % 10 ==0):
       count+=1
       factorial = factorial/10 
   return count
if __name__ == "__main__":
    print(fact(5))
    print(count_digits(5))