class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название : {self.name} , кол-во этажей : {self.number_of_floors}'


    def __eq__(self, other):
       return self.number_of_floors == other

    def __add__(self, other):
        if not isinstance(self.number_of_floors,int):
            print(f'Type. error : {self.number_of_floors},не целое число')
        return House(self.name ,self.number_of_floors + other)

    def __iadd__(self, other):
        if not isinstance(self.number_of_floors,int):
            print(f'Type. error : {self.number_of_floors},не целое число')
        return House(self.name, self.number_of_floors + other)

    def __radd__(self, other):
        if not isinstance(self.number_of_floors,int):
            print(f'Type. error : {self.number_of_floors},не целое число')
        return House(self.name, self.number_of_floors + other)


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors



hous1 = House('Бунино-парк', 45)
hous2 = House('Городские поляны', 35)
hous3 = House('Москва-сити', 94)
print(str(hous1))
print(str(hous2))
print(str(hous3))
print(len(hous1))
print(len(hous2))
print(len(hous3))
print (hous1)
print (hous3)
print(hous3 == hous1)
hous3 = hous3 + 10
print(hous3)
print(hous3 == hous1)
hous3 += 10
print(hous3)
hous1 = 15 + hous1
print(hous1)
print(hous3 > hous2)
print(hous3 >= hous2)
print(hous3 < hous2)
print(hous3 <= hous2)
print(hous3 != hous2)
