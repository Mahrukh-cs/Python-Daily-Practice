class student:
    # Methods 
    def __init__(self, roll_no: int, name: str, age: int, gender: str) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender        

    def display_details(self) -> None:
        print(f"Roll No = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

# object/instance
student1 = student(1, "Mano Billi", 20, "Female")
student1.display_details()