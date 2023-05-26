class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

    def say_greeting(self):
        print("Hello world! My name is {}!".format(self.name))

    def count_to_age(self):
        for i in range(1, self.age + 1):
            print(i)
