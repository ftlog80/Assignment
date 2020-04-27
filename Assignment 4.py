get_nmb = int(input("Please input a number ! "))
for i in range(2,get_nmb,1):
    if  get_nmb % i == 0:
        print(f"{get_nmb} is not a prime number !")
    else:
        print(f"{get_nmb} is a prime number .")
    break


