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
Jobs = []
def Initialise():
    global Jobs
    global NumberofJobs
    for i in range(0,100):
        Jobs.append([-1,-1])
    NumberofJobs = 0

def AddJob(JobN, priority):
    global NumberofJobs
    global Jobs
    if NumberofJobs == 100:
        print("Not Added")
    else:
        Jobs[NumberofJobs] = [JobN, priority]
        print("Added")
        NumberofJobs += 1

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
# print(Jobs)
def InsertionSort():
    global Jobs
    global NumberofJobs
    for i in range(1, NumberofJobs):
        CurrentJob = Jobs[i]
        j = i-1      #shifts elements towards the right side
        while j >= 0 and Jobs[j][1]>CurrentJob[1]:
            Jobs[j+1] = Jobs[j]
            j -= 1
            Jobs[j+1] = CurrentJob

def PrintArray():
    global Jobs
    global NumberofJobs
    print("Jobs sorted in ascending order")
    for i in range(NumberofJobs):
        print(f"Job Number = {Jobs[i][0]} and Priority = {Jobs[i][1]}")
InsertionSort()
PrintArray()

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

