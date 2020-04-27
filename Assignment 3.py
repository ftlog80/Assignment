number_1 = input("Please enter a number : ")
if number_1.isdigit() and int(number_1) >= 0:
    sum_num = 0
    for i in range(len(number_1)):
        new_element = int(number_1[i])**len(number_1)
        sum_num += new_element
    if sum_num == int(number_1):
        print(f"{number_1} is an Armstrong Number.")
    else:
        print(f"{number_1} is not an Armstrong Number.")
elif "." in number_1 or "," in number_1:
    print("Please enter an integer ! ")
elif number_1.isalnum():
    print("Please enter a number ! ")
elif int(number_1) < 0:
    print("Please enter a positive number !")
