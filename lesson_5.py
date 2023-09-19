# CREATING CLASS --------------------------------
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

    def walk(self):
        return 'I can walk!'

# USING CLASS --------------------------------
person_1 = Person('Alex', 'Baker')
print(person_1.name)
print(person_1.surname)
person_1.name = 'Alexander'
person_1.surname = 'Bakerman'
print(person_1.hello())
print(person_1.walk())


person_2 = Person('Anna', 'Smith')
print(person_2.name)
print(person_2.surname)
print(person_2.hello())
print(person_2.walk())
print(person_2.__dict__)
print(Person.__dict__)

# CLASS INHERITANCE --------------------------------
class Tester(Person):
    def __init__(self, name, surname, framework):
        super().__init__(name, surname)
        self.framework = framework

    def test(self):
        return 'I love testing'

tester_1 = Tester('Max', 'Hunter', 'Java')
print(tester_1.name)
print(tester_1.surname)
print(tester_1.framework)
print(tester_1.hello())
print(tester_1.test())

# PRIVATE PROPERTIES --------------------------------
class Person_new:
    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self._sex = sex
        self.__age = age

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

    def set_name(self, new_name):
        self.name = new_name

person_3 = Person_new('Alex', 'Baker', 'Female', 30)
print(Person_new.__dict__)
print(person_3.__dict__)
print(person_3.name)
print(person_3.surname)
print(person_3._sex)
print(person_3._Person_new__age)

person_3.set_name('Sanja')
print(person_3.hello())
