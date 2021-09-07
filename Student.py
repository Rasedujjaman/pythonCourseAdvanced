# This is a Student class

class Student:
    
    # The constructor
    def __init__(self, student_name, student_id, result):
        self.student_name = student_name
        self.student_id = student_id
        self.result = result
 
 
    def getInfos(self):
        print(f"Name: {self.student_name}")
        print(f"ID: {self.student_id}")
        print(f"CGPA: {self.result}")
        

    def getName(self):
        print(f"Name: {self.student_name}")
        
    def setName(self, name):
        self.name = name
        
    def setID(self, student_id):
        self.student_id = student_id
    
    def setResult(self, result):
        self.result = result
        
    def setInfos(self, student_name, student_id, result):
        self.student_name = student_name
        self.student_id = student_id
        self.result = result
        


    def __del__(self):
        class_name = self.__class__.__name__
        print (f"{class_name} destroyed")


s1 = Student("karim", 23, 3.44)
s1.getInfos()  # display all the informations


s2 = Student("put the name", 000, 0.0000)
s2.setInfos("Edward", 1, 3.50)
s2.getInfos()


del s1
del s2
