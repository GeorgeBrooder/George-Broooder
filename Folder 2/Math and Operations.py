# print(2 ** 8)
# 256

# print(7/5)
# 1.4

# print(7 % 5)
# 2

#num_given = int(input("Give a number"))
#if(num_given):
#    print("Even")
#else:
#    print("Odd")


# num = 5
# print(num%2)

# x = 5

# y = 5

# print(y is x)

# str1 = "Suck my"
# str2 = "fat nuts"

# print(str1 + " " + str2)

# x = 5

# x+= 2

# print(x)

# multi_string = """
# Shut 
# your
# stupid ass
# up
# """

# if(6 >= 6):
#     print("hello")
# else:
#     print("goodbye")

# expression = "hello" if 6 >= 6 else "goodbye"
# print(expression)

# sale = True
# store_message = "Hello we have a sale today!" if sale else "we dont have a sale today"

# print(store_message)

# store_message = ""
# sale = True
# if(sale):
#     store_message = "Hello, we have a sale today!"
# else:
#     store_message = "We dont have a sale today"

# if((2**3 == 8) and (4**2 == 8)):
#     print("True")
# else:
#     print("False")

# if((not (2**3 == 8) or (4**2 == 8)):
#     print("True")
# else:
#     print("False")

# def add_two_if_even_and_add_three_if_three(num):
#     if(num % 2 == 0):
#         return num + 2
#     elif(num==3):
#         return num + 3
#     return num

# x = 1
# y = 2
# z = 3
# print(add_two_if_even_and_add_three_if_three(x))
# print(add_two_if_even_and_add_three_if_three(y))
# print(add_two_if_even_and_add_three_if_three(z))


try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("b was equal to zero, computers can't divide by zero dipshit.")
    b = int(input("b: "))
    print(a/b)
