# fruits = ["apple","banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index = {index} Fruit = {fruit}")
    
#RECURSIVE
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))
# x = 13//2
# print(x)

# Initialize the queue with a fixed size of 50
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

# Enqueue function to add an item to the queue
def Enqueue(value):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 50:
        print("Queue is full")
    else:
        Queue[TailPointer] = value  # Insert value at the correct position
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0  # Set the head pointer to 0 if the first item is inserted

# Dequeue function to remove an item from the queue
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue is empty")
        return "Empty"
    else:
        item = Queue[HeadPointer]  # Get the front item
        HeadPointer += 1  # Move the head pointer forward
        if HeadPointer == TailPointer:  # Reset if the queue is empty after dequeue
            HeadPointer = -1
            TailPointer = 0
        return item

# ReadData function to enqueue data from QueueData.txt
def ReadData():
    global Queue, HeadPointer, TailPointer
    try:
        with open("QueueData.txt", 'r') as file:
            for line in file:
                Enqueue(line.strip())  # Enqueue each line after stripping whitespace
    except FileNotFoundError:
        print("QueueData.txt not found.")

# RecordData class to hold game ID and its total count
class RecordData:
    def _init_(self, ID, Total):
        self.ID = ID        # Game ID
        self.Total = Total  # Frequency count


Records = [None] * 50
NumberRecords = 0


def TotalData():
    global Records, NumberRecords
    DataAccessed = Dequeue()
    flag = False

    if DataAccessed == "Empty":
        return  # Exit if the queue is empty

    if NumberRecords == 0:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        flag = True
        NumberRecords += 1
    else:
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