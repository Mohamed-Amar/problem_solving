num = int(input())

for i in range(2, 10):
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("YES")
        break

    if num % i == 0:
        print("NO")
        break
else:
    print("YES")

# # Program to check if a number is prime or not


# # To take input from the user
# num = int(input("Enter a number: "))

# # define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")
