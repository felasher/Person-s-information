# Python class named Person
class Person:
    # Initialize the attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Implement the introduce method
    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class
person = Person("John Doe", 25, "Male")

# Call the introduce method to display the person's information
person.introduce()