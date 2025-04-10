# def BubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]

# num = [5,1,4,2,8]
# BubbleSort(num)
# print(num)
# num.reverse()
# print(num)


# def InsertionSort(list):
#     n=len(list)
#     for i in range(1,n):
#         key = list[i]
#         j = i - 1
#         while j>=0 and  key<list[j]:
#             list[j+1] = list[j]
#             j-=1
#             list[j+1] = key
# num = [12,11,13,5,6]
# InsertionSort(num)
# print(num)

# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks
# class Sort(Student):
#     def add_student(self,name,marks):
#         super().__init__(name,marks)


# def BubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
                
# num = [3,5,1,7,4,8,2,9]
# BubbleSort(num)
# print(num)

# def InsertionSort(list):
#     n=len(list)
#     for i in range(1,n):
#         key = list[i]
#         j = i-1
#         while j>=0 and key<list[j]:
#             list[j+1] = list[j]
#             j -= 1
#             list[j+1] =key
# num = [3,5,1,7,4,8,2,9]
# InsertionSort(num)
# print(num) 

#LINEAR SEARCH: it is a way to find the list by checking each element one by one until we find a match
# def LinearSearch(list, target):
#     n =len(list)
#     for i in range(n):
#         if list[i] ==target:
#             return i
#     return -1
# num = [2,4,5,7,3,9,8,1]
# target = 7
# Result = LinearSearch(num,target)
# if Result != -1:
#     print("Element found at index", Result)
# else:
#     print("Element not found")

#BINARY SEARCH: it is a way to search in a sorted list by repeatedly dividing the search interval in half
#It only works when list is alrdy sorted
# def BinarySearch(list, target):
#     n=len(list)
#     low = 0
#     high = n-1
#     while low<=high:
#         mid = (low+high)//2
#         if list[mid] == target:
#             return mid
#         elif list[mid]<target:
#             low = mid+1
#         else:
#             low = mid-1
#     return -1
# num = [1,2,3,4,5,6,7]
# target = 7
# Result = BinarySearch(num,target)
# if Result != -1:
#     print("Element found at index", Result)
# else:
#     print("Element not found")

#Bubble sort and binary search
# num = [2,4,5,7,3,9,8,1]
# def BubbleSort(list):
#     n = len(list)
#     for i in range(n):
#         for j in range(n-i-1):
#             if list[j]>list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]

# def BinarySearch(list, target):
#     n = len(list)
#     low = 0
#     high = n-1
#     while low<=high:
#         mid = (low+high)//2
#         if list[mid] == target:
#             return mid
#         elif low<=target:
#             low=mid+1
#         else:
#             low = mid-1
#     return -1

# num = [2,4,5,7,3,9,1]
# BubbleSort(num)
# print(num)
# target = 4
# Result = BinarySearch(num,target)
# if Result != -1:
#     print("Element found at index", Result)
# else:
#     print("Element not found")
