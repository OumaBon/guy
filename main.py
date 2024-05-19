class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def json(self):
        return{
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

student_1  = Student('Liam',45, 'male')
print(student_1.name)
print(student_1.gender)
