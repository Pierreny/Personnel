#creating a general Personnel class for doctor, surgeon and nurse
class Personnel:

    def __init__(self, name, age,hourlyrate):
        self.name = name
        self.age = age
        self.hourlyRate = hourlyrate
#Using display method to display age and name attributes in personnel class

    def display(self):
        print(f"Employee name is {self.name} and is {self.age} years old")

# creating doctor child class and passing personel attributes through inheritance

class Doctor(Personnel):
    def __init__(self, name, age, hourlyrate, speciality):
        super().__init__(name, age, hourlyrate)
        self.speciality = speciality

    def displayDoctor(self):
        print( f"{self.name} is a {self.age} doctor paid $ {self.hourlyRate} per hour and  specializes in {self.speciality} ")

# creating surgeon  child class and passing personel attributes through inheritance
class Surgeon(Personnel):
    def __init__(self, name, age, hourlyrate, boardCertified):
        super().__init__(name, age, hourlyrate)
        self.boardCertified = boardCertified

    def displaySurgeon(self):
        print(
            f"{self.name} is a {self.age} Surgeon paid  $ {self.hourlyRate} board certified {self.boardCertified} ")

# creating nurse child class and passing personel attributes through inheritance
class Nurse(Personnel):
    def __init__(self, name, age, hourlyrate, rank, ):
        super().__init__(name, age, hourlyrate)
        self.rank = rank
#Using display method to display age  attributes in child class nurse
    def displayNurse(self):
        print(f"{self.name} is a {self.age} Nurse paid $ {self.hourlyRate} per hour is a {self.rank}  Nurse")


#create a object and displaying
Personnel1 = Personnel("Jerry", 50, 60)
Personnel1.display()

#creating instances of the doctor, nurse and Surgeon classes and
Doctor1 = Doctor("Anthony","25","60","Heart Diseases")
Doctor1.displayDoctor()
Surgeon1 = Surgeon("Judith","30","80","Certified")
Surgeon1.displaySurgeon()
Nurse1 = Nurse("Shayla","28","45","Junior")
Nurse1.displayNurse()

