sum = 0
i=0
j=0
print("!!! WELCOME TO KHAN STORE !!!")
customer = input("Enter the name of customer: ")
items = []
prizes = []
quantites = []
while(True):
    print()
    item = input("Enter the name of item or press q to quit: ")
    if item!='q':
        prize = int(input("Enter the prize of item: "))
        quantity = int(input("Enter the quantity of item: "))
        total_prize = prize * quantity
        items.append(item)
        prizes.append(prize)
        quantites.append(quantity)
        sum = sum + total_prize
        i+=1
    else:
        print("Thanks for shopping!!!")
        print(f"Your total bill is Rs {sum}")
        break

f1 = open(f"{customer}'s Bill.txt", "a")
f1.write(f"Dear {customer} Thanks for shopping!!!"+"\n")
while j<i:
    f1.write(f"{j+1}. {items[j]} - {prizes[j]} X {quantites[j]} - {prizes[j] * quantites[j]}"+"\n")
    j+=1
f1.write(f"Your total bill is Rs {sum}")