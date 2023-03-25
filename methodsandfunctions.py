
#method
class Emp(object):
    age = 25 #
    salary = 1000 # $

    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("method: ", a) 

#-------------------------------
#function

def ageSalaryRatio(age, salary):
    a = age / salary
    print("function :", a)




e1 = Emp()
e1.ageSalaryRatio()

ageSalaryRatio(30, 30000)


#-------------------------------

pi = 3.14
r = 5
area = pi*r**2

def findArea(pi, r):
    area = pi*r**2
    print(area)
    return area

result1 = findArea(pi, r)

result2 = findArea(pi , 10)

print(result1+result2)



class Animal(object):
    

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age
    

a1 = Animal("fish", 3)

