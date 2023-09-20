class Person:
    def __init__(self, name, surname, id, age, sex):
        self.name = name
        self.surname = surname
        self.__id = id
        self._age = age
        self._sex = sex

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name


    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_surname(self):
        return self.surname

    def set_id(self, new_person_id):
        self._Person__id = new_person_id

    def get_id(self):
        return self._Person__id

    def set_age(self, new_age):
        self._age = new_age

    def get_age(self):
        return self._age

    def set_sex(self, new_sex):
        self._sex = new_sex

    def set_sex(self, new_sex):
        self._sex = new_sex

    def get_sex(self):
        return self._sex


person = Person('Alex', 'Baker', '121272-12345', 30, 'Male')
print(person.__dict__)
print(person.get_name())
print(person.get_surname())
print(person.get_id())
print(person.get_age())
print(person.get_sex())

person.set_name('Alexander')
person.set_id('030373-54321')
person.set_age(32)
print(person.__dict__)