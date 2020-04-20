passwords = {"ali": "@123", "veli": "@345"}
customer = input("Enter your name : ").lower()
if customer in passwords:
    for key, value in passwords.items():
     if customer == key:
      print(f"Hello {customer}. Your Password is {value}")
else:
    print(f"Thank you {customer}, see you later.")