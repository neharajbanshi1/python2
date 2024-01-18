#encapsulation 
 
class EncapsulatedClass:
    def __init__(self, name ,age):
        self.name =name
        self._age =age #protected attribute
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age>0:
            self._age =age
my_entry =EncapsulatedClass("Hari",23)
print(f"Name:{my_entry.name}")
print(f"Age:{my_entry._age}")
print(f"Age:{my_entry.get_age()}")