print("hey folks!")

#classes

class Employee(object):
    # attribute = age, address, name
    # behaviour = pass
    pass
#####################
class Basketballer:
    club = "Chicago Bulls"
    age = 29
    
f1 = Basketballer()
print(f1)
print(f1.age)
print(f1.club)

#################

class Square(object):
    edge = 5 # meter
    area = 0
    def area1(self):
        self.area = self.edge*self.edge # 5*5
        print("Area :", self.area)


s1 = Square()

print(s1)
print(s1.edge)

print(s1.area1()) 


s1.edge = 7
s1.area1()
