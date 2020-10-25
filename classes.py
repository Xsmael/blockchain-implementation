class Employee:
    empCount= 0

    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
        Employee.empCount+=1
    
    def displayCount(self):
        print("Total employees= "+str(Employee.empCount))
    
    def displayEmployee(self):
        print("Employee Name: "+ self.name)
        print("Employee Name: "+ str( self.salary))





e1= Employee("Jonh McCain",2500)
e2= Employee("Sylvester",32500)


e2.jobTitle="Clown"
setattr(e1,"dynamicAttr","Setting attr dynamically on fly! so cooool!")

print(e2.jobTitle)
print(e1.dynamicAttr)

print(hasattr(e1,"dynamicAttr"))
print(hasattr(e2,"dynamicAttr"))

del e1.dynamicAttr
delattr(e2,"jobTitle")

getattr(e1,"salary",)

e2.displayCount()
e2.displayEmployee()


print( 0 == 0)