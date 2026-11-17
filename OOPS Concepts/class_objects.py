class student:
    # Attributes
    roll_no = 0
    name = ""
    age = 0
    gender = ""

    # Methods 

    def set_details(self, roll_no: int, name: str, age: int, gender: str) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
    
    # def set_details(self):
    #     self.roll_no = int(input("Enter your roll no = "))
    #     self.name = input("Enter your name = ")
    #     self.age = int(input("Enter your age = "))
    #     self.gender = input("Enter your gender = ")

    def display_details(self) -> None:
        print(f"Roll No = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

# object/instance
student1 = student()
student1.set_details(1, "Mano Billi", 20, "Female")
student1.display_details()

student2 = student()
student2.display_details()