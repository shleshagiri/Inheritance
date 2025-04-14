# class Person:
#     def __init__(self, name, age, gender):
#         self.__name = name
#         self.__age = age
#         self.__gender = gender
#     def Display(self):
#         print(self.__name, self.__age, self.__gender)

# class Student(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender)
#         self.__subjects = []
#     def enroll_subjects(self, subject):
#         self.__subjects.append(subject)
#     def display_info(self):
#         self.Display()
#         print("Enrolled Subjects:", self.__subjects)

# class Teacher(Person):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age, gender,)
#         self.__subjects = []
#     def assign(self, subject):
#         self.__subjects.append(subject)
#     def display_info(self):
#         self.Display()
#         print("Assigned Subjects:", self.__subjects)
        
# student = Student("Shlesha", 17, "Female")
# student.enroll_subjects("Maths")
# student.enroll_subjects("Computer")
# teacher = Teacher("Ram", 35, "Male")
# teacher.assign("Maths")
# teacher.assign("Economics")

# student.display_info()
# teacher.display_info()

# Write a program which counts the lower cases and upper cases of vowel letters. 
# def Vowels(name):
#     u_count = 0
#     l_count = 0
#     for i in name:
#         if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
#             u_count+=1
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             l_count+=1
#     print(u_count)
#     print(l_count)
 
# Vowels('ShlEsha GirI')


#9618/42/o/n/23
# StackVowel=[0]*100
# StackConsonant =[0]*100
# global VowelTop
# global ConsonantTop
# VowelTop = 0
# ConsonantTop = 0

# def PushData(letter):
#     global VowelTop
#     global ConsonantTop
#     if letter =='a' or letter =='e' or letter=='i' or letter=='o' or letter =='u':
#         if StackVowel == 100:
#             print("Stack is full")
#         else:
#             StackVowel.append(letter)
#             VowelTop+=1
#     else:
#         if ConsonantTop == 100:
#             print("Stack is full")
#         else:
#             ConsonantTop.append(letter)
#             ConsonantTop+=1

# def ReadData():
#     try:
#         file = open("StackData.txt",'r')
#         for line in file:
#             PushData(line)
#         file.close()
#     except:
#         print("File not found")

# def PopVowel():
#     global VowelTop, StackVowel
#     global ConsonantTop, StackConsonant
#     if VowelTop == 0:
#         print("No data")
#     else:
#         VowelTop -= 1
#         return StackVowel[VowelTop]
    
# def PopConsonant():
#     global VowelTop
#     global ConsonantTop
#     if ConsonantTop == 0:
#         print("No data")
#     else:
#         ConsonantTop -= 1
#         return StackConsonant[ConsonantTop]

# def Main():
#     ReadData()
#     stack = []
#     for i in range(5):
#         userinput = input("Enter your choice. Vowel or Consonant").lower()
#         if userinput == "vowel":
#             letter = PopVowel()
#         elif userinput == "consonant":
#             letter = PopConsonant()
#         else:
#             print("Invalid Input")
#     if letter == "No data":
#         print("Stack is empty")
#     else:
#         stack.append(letter)
#     print("".join(stack))
# Main()

# StackVowel= ["a", "e", "i", "o", "u"]
# StackConsonant = ["t", "s", "d", "f", "g"]
# VowelTop = 5
# ConsonantTop = 5

# print(PopVowel())
# print(PopConsonant())
# print(PopVowel())
# print(PopConsonant())


##2.
# def IterativeCalculate(Number):
#     ToFind = 0
#     Total = 0
#     while Number != 0:
#         if ToFind % Number == 0:
#             Total += Number
#         Number -= 1
#     return Total
# print(IterativeCalculate(10))

# def RecursiveValue(Number, ToFind):
#     if Number == 0:
#         return 0
#     elif ToFind % Number == 0:
#         return Number + RecursiveValue(Number-1, ToFind)
#     else:
#         return RecursiveValue(Number-1, ToFind)
# print(RecursiveValue(50,50))
    

##
# Jobs = []
# def Initialise():
#     global Jobs
#     global NumberofJobs
#     for i in range(0,100):
#         Jobs.append([-1,-1])
#     NumberofJobs = 0

# def AddJob(JobN, priority):
#     global NumberofJobs
#     global Jobs
#     if NumberofJobs == 100:
#         print("Not Added")
#     else:
#         Jobs[NumberofJobs] = [JobN, priority]
#         print("Added")
#         NumberofJobs += 1

# Initialise()
# AddJob(12,10)
# AddJob(526,9)
# AddJob(33,8)
# AddJob(12,9)
# AddJob(78,1)
# # print(Jobs)
# def InsertionSort():
#     global Jobs
#     global NumberofJobs
#     for i in range(1, NumberofJobs):
#         CurrentJob = Jobs[i]
#         j = i-1      #shifts elements towards the right side
#         while j >= 0 and Jobs[j][1]>CurrentJob[1]:
#             Jobs[j+1] = Jobs[j]
#             j -= 1
#             Jobs[j+1] = CurrentJob

# def PrintArray():
#     global Jobs
#     global NumberofJobs
#     print("Jobs sorted in ascending order")
#     for i in range(NumberofJobs):
#         print(f"Job Number = {Jobs[i][0]} and Priority = {Jobs[i][1]}")
# InsertionSort()
# PrintArray()

##
# class Character:
#     def __init__(self, Name, XCoordinate, YCoordinate):
#         self.__Name = Name
#         self.__XCoordinate = XCoordinate
#         self.__YCoordinate = YCoordinate
    
#     def GetName(self):
#         return self.__Name
    
#     def GetX(self):
#         return self.__XCoordinate
    
#     def GetY(self):
#         return self.__YCoordinate
    
#     def ChangePosition(self, XChange, Ychange):
#         self.__XCoordinate += XChange
#         self.__YCoordinate += Ychange

# Characters = []
# try:
#     with open("Character.txt", 'r') as file:
#         for line in file:
#             data = line.strip().split()
#             if len(data) == 3:
#                 Name = data[0]
#                 XCoordinate = int(data[1])
#                 YCoordinate = int(data[2])
#                 c = Character(Name, XCoordinate, YCoordinate)
#                 Characters.append(c)
# except FileNotFoundError:
#     print("File not found")

# found = False
# while not found:
#     CharacterName = input("Enter charcater's name").strip().lower()
#     for i in range(len(Characters)):
#         if Characters[i].GetName().strip().lower() == CharacterName:
#             Position = i
#             found = True
#     if not found:
#         print("Character not found")

# while True:
#     move = input("Enter move direction (A=left, W=up, S=down, D=right)").strip().upper()
#     if move == 'A':
#         Characters[Position].ChangePosition(-1, 0)
#     elif move == 'W':
#         Characters[Position].ChangePosition(0, 1)
#     elif move == 'S':
#         Characters[Position].ChangePosition(0, -1)
#     elif move == 'D':
#         Characters[Position].ChangePosition(1, 0)
#     else:
#         print("Invalid input")
#     Name = Characters[Position].GetName()
#     x = Characters[Position].GetX()
#     y = Characters[Position].GetY()
#     print(f"{Name} has changed coordinates to X = {x} and Y = {y}")


#Queue : FIFO
# Queue = []
# Queue.append("A")
# Queue.append("B")
# Queue.append("C")
# print(Queue)
# item1 = Queue.pop(0)
# print(item1)

# from queue import Queue
# queue = Queue()
# queue.put("A")
# queue.put("B")
# queue.put("C")
# print(queue.qsize())

##
# Queue = [None]*100
# HeadPointer = 0
# TailPointer = 0
# def Enqueue(value):
#     global Queue
#     global HeadPointer
#     global TailPointer
#     if TailPointer >= 100:
#         return False
#     else:
#         Queue[TailPointer] = value
#         TailPointer += 1
#         return True

# Success = True
# for i in range(1,21):
#     if not Enqueue(i):
#         Success = False
#         break
#     if Success:
#         print("Successful")
#     else:
#         print("Unsuccessful")
# for j in range(HeadPointer, TailPointer):
#     print(Queue[j])

# def RecursiveOutput(Start):
#     Total = 0
#     if Start < HeadPointer:
#         return 0
#     else:
#         return Queue[Start]+RecursiveOutput(Start-1)
# Total = RecursiveOutput(TailPointer-1)
# print(Total)

##9618/42/O/N/21
# class Picture:
#     def __init__(self, Description, Width, Height, FrameColour):
#         self.__Description = Description
#         self.__Width = Width
#         self.__Height = Height
#         self.__FrameColour = FrameColour
    
#     def GetDescription(self):
#         return self.__Description

#     def GetWidth(self):
#         return self.__Width
    
#     def GetHeight(self):
#         return self.__Height
    
#     def GetFrameColour(self):
#         return self.__FrameColour
    
#     def SetDescription(self, newD):
#         self.__Description = newD
# PictureArray = []
# for i in range(100):
#     PictureArray.append(Picture("", 0, 0, ""))

# def ReadData():
#     count = 0
#     try:
#         with open("Pictures.txt",'r') as file:
#             while count < 100:
#                     Description = file.readline().strip()
#                     if not Description:
#                         break
#                     Width = float(file.readline().strip())
#                     Height = float(file.readline().strip())
#                     FrameColour = file.readline().strip()
#                     pic = Picture(Description, Width, Height, FrameColour)
#                     PictureArray.append(pic)
#                     count += 1
#     except FileNotFoundError:
#         print("File not found")
#     return count

# FrameColour = input("Input the Frame colour ").lower()
# MaxWidth = int(input("Input the Maximum Width "))
# MaxHeight = int(input("Input the Maximum Height "))

# ReadData()
# for i in range(len(PictureArray)):
#     if PictureArray[i].GetWidth() <= MaxWidth and PictureArray[i].GetHeight() <= MaxHeight and PictureArray[i].GetFrameColour().lower() == FrameColour:
#         print(PictureArray[i].GetDescription(), " ", PictureArray[i].GetWidth(), " ", PictureArray[i].GetHeight())


# ##
# def Unknown(x, y):
#     if x < y:
#         print(x + y)
#         return Unknown(x+1, y)*2
#     elif x ==y :
#         return 1
#     else:
#         print(x + y) 
#         return Unknown(x - 1, y)//2
# print("10 and 15")
# print(Unknown(10, 15))
# print("10 and 10")
# print(Unknown(10, 10))
# print("15 and 10")
# print(Unknown(15, 10))


##
# ArrayNodes = [[0 for x in range(3)]for y in range(20)]
# RootPointer = -1
# FreeNode = 0

# def AddNode(ArrayNodes, RootPointer, FreeNode):
#     userdata = int(input("Enter the data"))
#     if FreeNode <= 19:
#         ArrayNodes[FreeNode][0] = -1           #LEFTPOINTER
#         ArrayNodes[FreeNode][1] = userdata     #DATA(user data stored in this others are empty)
#         ArrayNodes[FreeNode][2] = -1           #RIGHTPOINTER(-1 means that they dont exist yet)
#         if RootPointer == -1:
#             RootPointer = 0
#         else:
#             flag = False
#             CurrentNode = RootPointer
#             while not flag:
#                 if userdata < ArrayNodes[CurrentNode][1]:        #checks if given data is less than the root(in the left)
#                     if ArrayNodes[CurrentNode][0] == -1:         #if the left is empty
#                         ArrayNodes[CurrentNode][0] = FreeNode    #makes it the next empty space(FREENODE)
#                         flag = True                             
#                     else:
#                         CurrentNode = ArrayNodes[CurrentNode][0]   #orelse it makes the left value root and checks if its left value is less than uerdata
#                 else:
#                     if ArrayNodes[CurrentNode][2] == -1:            #checks if given data is greater than root (in the right)if empty then
#                         ArrayNodes[CurrentNode][2] = FreeNode       #makes it the next empty space(FREENODE)
#                         flag = True
#                     else:
#                         CurrentNode = ArrayNodes[CurrentNode][2]    #orelse it makes the right value root and checks if its right value is greater than userdata
#         FreeNode+=1 
#     else:
#         print("Tree is full")
#     return ArrayNodes, RootPointer, FreeNode

# def PrintAll(ArrayNodes):
#     for x in range(20): 
#         print(ArrayNodes[x][0], " ", ArrayNodes[x][1], " ", ArrayNodes[x][2])

# for i in range(0, 10):
#     ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
# PrintAll(ArrayNodes)

# def InOrder(ArrayNodes, RootNode):                   #Left>>Root>>Right
#     if ArrayNodes[RootNode][0] != -1:                   #Checks if there is a left value
#         InOrder(ArrayNodes, ArrayNodes[RootNode][0])    #Go left
#     print(ArrayNodes[RootNode][1])                      #Visit Node
#     if ArrayNodes[RootNode][2] != -1:                   #check if there is right value
#         InOrder(ArrayNodes, ArrayNodes[RootNode][2])    #Go right
# InOrder(ArrayNodes, RootPointer)

##9618/43/o/n/23
##1.
# def IterativeVowels(Value):
#     Total = 0
#     LengthString = len(Value)
#     for x in range(0, LengthString):
#         FirstCharacter = Value[0]
#         if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
#             Total += 1
#         Value = Value[1:len(Value)]
#     return Total

# print(IterativeVowels("house"))

# def RecursiveVowels(Value):
#     if len(Value) == 0:
#         return 0
#     else:
#         FirstCharacter = Value[0]
#         if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
#             return 1 + RecursiveVowels(Value[1:len(Value)])
#         else:
#             return RecursiveVowels(Value[1:len(Value)])

# print(RecursiveVowels("imagine"))


##2.
# Queue = [""]*50
# HeadPointer = -1
# TailPointer = 0

# def Enqueue(value):
#     global Queue
#     global HeadPointer
#     global TailPointer
#     if TailPointer >= 50:
#         print("Queue is full")
#     else:
#         Queue.append(value)
#         TailPointer += 1
#         if HeadPointer == -1:
#             HeadPointer = 0

# def Dequeue():
#     global Queue
#     global HeadPointer
#     global TailPointer
#     if HeadPointer == -1 or HeadPointer == TailPointer:
#         print("Empty")
#     else:
#         HeadPointer += 1   #Moves the front of the queue to the next item (because you’re removing the current one)
#         return Queue[HeadPointer - 1]  #Returns the item that was just removed — which is the one just before the updated HeadPointer.

# def ReadData():
#     global Queue
#     global HeadPointer
#     global TailPointer   
#     try:
#         with open("QueueData.txt", 'r') as file:
#             for line in file:
#                 Enqueue(line.strip())
#         file.close()
#     except FileNotFoundError:
#         print("File not found")

# class RecordData:
#     def __init__(self, ID, Total):
#         self.__ID = ID
#         self.__Total = Total

# Records = [None] * 50   

# def TotalData():
#     DataAccessed = Dequeue()
#     flag = False
#     if NumberRecords == 0:
#         Records[NumberRecords].self.__ID = DataAccessed
#         Records[NumberRecords].self.__Total = 1
#         flag = True
#         NumberRecords += 1
#     else:
#         for x in range(0, NumberRecords):
#             if Records[x] == DataAccessed:
#                 Records[x].self.__Total += 1
#                 flag= True
#     if flag == False:
#         Records[NumberRecords].self.__ID = DataAccessed
#         Records[NumberRecords].self.__Total = 1
#         NumberRecords += 1
        
# def OutputRecords(self):
#     print(f"ID: {self.__ID} Total: {self.__Total}")

# ReadData()


# Initialize the queue with a fixed size of 50
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

# Enqueue function to add an item to the queue
def Enqueue(value):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 50:
        print("Queue is full")
        return
    Queue[TailPointer] = value
    TailPointer += 1
    if HeadPointer == -1:
        HeadPointer = 0

# Dequeue function to remove an item from the queue
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue is empty")
        return "Empty"
    item = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
    return item

# ReadData function to enqueue data from QueueData.txt
def ReadData():
    try:
        with open("QueueData.txt", 'r') as file:
            for line in file:
                Enqueue(line.strip())
    except FileNotFoundError:
        print("QueueData.txt not found.")

# RecordData class to hold game ID and its total count
class RecordData:
    def _init_(self, ID, Total):
        self.ID = ID
        self.Total = Total

# Global variables to store records and count
Records = [None] * 50
NumberRecords = 0

# TotalData function to process queue and update frequency counts
def TotalData():
    global Records, NumberRecords
    DataAccessed = Dequeue()
    if DataAccessed == "Empty":
        return
    flag = False
    for x in range(NumberRecords):
        if Records[x].ID == DataAccessed:
            Records[x].Total += 1
            flag = True
            break
    if not flag:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        NumberRecords += 1

# OutputRecords function to display the ID and total count for each record
def OutputRecords():
    for i in range(NumberRecords):
        print(f"ID: {Records[i].ID} Total: {Records[i].Total}")
ReadData()
TotalData()
OutputRecords()

##3.
# class Character:
#     def __init__(self, Name, Xposition, YPosition):
#         self.__Name = Name
#         self.__XPosition = Xposition
#         self.__YPosition = YPosition
    
#     def GetXPosition(self):
#         return self.__XPosition
    
#     def GetYPosition(self):
#         return self.__YPosition
    
#     def SetXPosition(self,x):
#         self.__XPosition += x
#         if self.__XPosition > 10000:
#             self.__XPosition = 10000
#         elif self.__XPosition < 0:
#             self.__XPosition = 0

#     def SetYPosition(self, y):
#         self.__YPosition += y
#         if self.__YPosition > 10000:
#             self.__YPosition = 10000
#         elif self.__YPosition < 0:
#             self.__YPosition = 0

#     def Move(self, direction):
#         if direction == "up":
#             self.__YPosition(10)
#         elif direction == "down":
#             self.__YPosition(-10)
#         elif direction == "left":
#             self.__XPosition(-10)
#         else:
#             self.__XPosition(10)

# Jack = Character("Jack", 50, 50)
        