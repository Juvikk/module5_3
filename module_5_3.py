class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self,new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor ):
                print(floor)
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.number_of_floors}"
    def __eq__(self,other):
       if isinstance(other, House):
         return self.number_of_floors == other.number_of_floors
       elif isinstance(other,int):
         return self.number_of_floors == other
    def __lt__(self,other): # __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) одинаковы просто с различием 1 элемента
        if isinstance(self.number_of_floors,int):
            return self.number_of_floors < other.number_of_floors


    def __add__(self,value):
        if isinstance(value,int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self,value):#
        if isinstance(value, int):
            self.number_of_floors += value
        return self





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 10)
h2.go_to(5)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print(h1)
print(h2)

print (h1==11)
print(h1<h2)
print(h1.__add__(8))