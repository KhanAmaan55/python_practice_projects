currency = {}
with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    parsed  = line.split('-')
    currency[parsed[0]] = parsed[1]
# print(currency)
amount = int(input("Enter the amount you want to convert: "))
print("\nAvailable options to convert : ")
[print(item) for item in currency.keys()]
cur = input("Please select the currency from the available options: ")
converter =  amount * float(currency[cur])
print(f"{amount} INR in equal to {converter} {cur}")