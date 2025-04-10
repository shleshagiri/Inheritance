##1. 
# import random 
# Data = random.sample(range(1,1001),200)
# print("Data=", Data)
# largest = Data[0]
# for num in Data:
#     if num > largest:
#         largest = num
# print(largest)

# # 2.
# import random 
# Data = random.sample(range(1,101),20)
# print("Data=", Data)
# largest = Data[0]
# smallest = Data[0]
# for num in Data:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print(largest)
# print(smallest)

##3.
# def ValidRegistration(Registration):
#     if len(Registration)<6 or len(Registration)>9:
#         return False
#     if not Registration[0:3].isalpha() or not Registration[0:3].isupper():
#         return False
#     if not Registration[3:5].isdigit():
#         return False
#     if len(Registration)>5:
#         for char in Registration[5:]:
#             if not char.isalpha() or not char.isupper():
#                 return False
#         return True
# print(ValidRegistration("ABC12X"))
# print(ValidRegistration("abc12X"))
# print(ValidRegistration("ABC123"))

##4.
# def ValidatePassword(Pass):
#     l_count = 0
#     u_count = 0
#     digit_count = 0
#     for char in Pass:
#         if not char.isdigit() and not char.isalpha():
#             return False
#         if char.islower():
#             l_count+=1
#         elif char.isupper():
#             u_count+=1
#         elif char.isdigit():
#             digit_count+=1
#     if l_count >=2 and u_count >= 2 and digit_count >= 3:
#         return True
#     else:
#         return False
# print(ValidatePassword("AaBb123"))
# print(ValidatePassword("A1b2"))
# print(ValidatePassword("A@b123"))

##5.
# def Frequency():
#     name = input("Enter a string")
#     count_a = 0
#     count_e = 0
#     count_i = 0
#     count_o = 0
#     count_u = 0
#     name = name.lower()
#     for char in name:
#         if char == 'a':
#             count_a+=1
#         elif char == 'e':
#             count_e+=1
#         elif char == 'i':
#             count_i+=1
#         elif char == 'o':
#             count_o+=1
#         elif char == 'u':
#             count_u+=1
#     print("a:", count_a)
#     print("e:", count_e)
#     print("i:", count_i)
#     print("o:", count_o)
#     print("u:", count_u)
# Frequency()

##6.
# def CountDigits():
#     Instring = input("Enter a string of digits")
#     Result = [0]*10
#     for char in Instring:
#         if char.isdigit():
#             digit = int(char)
#             Result[digit]+=1
#     for i in range(10):
#         print("digit", i, ":", Result[i])
# CountDigits()

##7.
# def IterativeVowels(text):
#     l_count = 0
#     for char in text:
#         if char =='a' or char=='e' or char=='i' or char=='o' or char=='u':
#             l_count+=1
#     print(l_count)
# IterativeVowels("Hello World")

##8.
# def Car():
#     cost = int(input("Enter cost of new car"))
#     year = 1
#     while cost >= 1000 and year <= 9:
#         if year == 1:
#             cost*=0.6
#         else:
#             cost*=0.8
#         print("Year", year, ": $", round(cost))
#         year+=1
# Car()

##8.
# def Calculate(expression):
#     for i in range(len(expression)):
#         if expression[i] in '+-*/':
#             operator = expression[i]

