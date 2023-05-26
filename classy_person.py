'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

    def say_greeting(self):
        print("Hello world! My name is", self.name + "!")

    def count_to_age(self):
        for i in range(1, self.age + 1):
            print(i)

# You won't need to call anything here.