# #9618/42/o/n/23(v2)
# ##3.
# from datetime import date
# class Character:
#     def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed):
#         self.__CharacterName = CharacterName
#         self.__DateOfBirth = DateOfBirth
#         self.__Intelligence = Intelligence
#         self.__Speed = Speed
    
#     def GetIntelligence(self):
#         return self.__Intelligence
    
#     def GetName(self):
#         return self.__CharacterName
    
#     def SetIntelligence(self, newvalue):
#         self.__Intelligence = newvalue
    
#     def Learn(self):
#         self.__Intelligence *= 1.1

#     def ReturnAge(self):
#         currentyear = 2023
#         age = currentyear - self.__DateOfBirth.year
#         return age
# FirstCharacter = Character("Royal", date(2019,1,1), 70, 30)
# FirstCharacter.Learn()
# print(FirstCharacter.GetName(), "is", FirstCharacter.ReturnAge(), "years old and has intelligence", FirstCharacter.GetIntelligence())

# class MagicCharacter(Character):
#     def __init__(self, CharacterName, DateOfBirth, Intelligence, Speed, Element):
#         super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
#         self.__Element = Element

#     def Learn(self):
#         if self.__Element == "Fire" or self.__Element == "Water":
#             super().SetIntelligence(super().GetIntelligence()*1.2)
#         elif self.__Element == "Earth":
#             super().SetIntelligence(super().GetIntelligence()*1.3)
#         else:
#             super().SetIntelligence(super().GetIntelligence()*1.2)

# FirstMagic = MagicCharacter("Light", date(2018,3,3), 75, 22, "Fire")
# FirstMagic.Learn()
# print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence", FirstMagic.GetIntelligence())

##9618/42/o/n/23(v1)
##3.
# class Character:
#     def __init__(self, Name, XPosition, YPosition):
#         self.__Name = Name
#         self.__XPosition = XPosition
#         self.__YPosition = YPosition

#     def GetXPosition(self):
#         return self.__XPosition
    
#     def GetYPosition(self):
#         return self.__YPosition
    
#     def SetXPosition(self, value):
#         self.__XPosition += value
#         if self.__XPosition > 10000:
#             self.__XPosition = 10000
#         elif self.__XPosition < 0:
#             self.__XPosition = 0
        
#     def SetYPosition(self, value):
#         self.__YPosition += value
#         if self.__YPosition > 10000:
#             self.__YPosition = 10000
#         elif self.__YPosition < 0:
#             self.__YPosition = 0

#     def Move(self, direction):
#         if direction == "up":
#             self.__SetYPosition(10)
#         elif direction == "down":
#             self.__SetYPosition(-10)
#         elif direction == "right":
#             self.__SetXPosition(10)
#         else:
#             self.__SetXPosition(-10)
# Jack = Character("Jack", 50, 50)

# class BikeCharacter(Character):
#     def __init__(self, Name, XPosition, YPosition):
#         super().__init__(Name, XPosition, YPosition)
    
#     def Move(self, direction):
#         if direction == "up":
#             super().SetYPosition(20)
#         elif direction == "down":
#             super().SetYPosition(-20)
#         elif direction == "right":
#             super().SetXPosition(20)
#         else:
#             super().SetXPosition(-20)
# Karla = BikeCharacter("Karla", 100, 50)

# CharacterToMove = input("Which character would you like to move, Jack or Karla?").lower()
# while CharacterToMove != "jack" and CharacterToMove != "karla":
#     CharacterToMove = input("Invalid input")
# Direction = input("Enter direction to move: up, down, right, left").lower()
# while Direction != "up" and Direction != "down" and Direction != "right" and Direction != "left":
#     Direction = input("Invalid direction")
#     if CharacterToMove == "Jack":
#         Jack.Move(Direction)
#         print("Jack's new position is X=", Jack.GetXPosition(), "Y=", Jack.GetYPosition())
# else:
#     Karla.Move(Direction)
# print("Karla's new position is X=", Karla.GetXPosition(), "Y=", Karla.GetYPosition())


