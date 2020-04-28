getnumber = int(input("Please enter a number ? "))
count = 0
for i in range(2,getnumber):
    if getnumber % i ==0:
        count += 1
    else:
        count += 0
if count == 0:
    print(f"{getnumber} is a prime number")
else:
    print(f"{getnumber} is not a prime number")
