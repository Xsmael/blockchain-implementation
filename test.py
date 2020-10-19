
nom= "Johnnie Dohnnie"
age=29

# nom= input("Quel est ton nom ? ")
# age= int( input("Quel est ton age ? ") )

list= ["name",10,5.2,"alright"] # A python list is just a junk array, it takes all sorts of things
print(list)
print(list[-1])  #Easy way to get the last item

def display(nom, age):
    print("Vous êtes "+nom+" et vous avez "+ str(age) +" ans" )
    return

def decennies(age):
    print("vous avez vécu "+ str(age/10) +" décennies")
    
    return

display(nom, age)
decennies(age)

