
def getData():
    age= int(input("age: "))
    name= input("name: ")
    obj={'age':age, 'name':name}
    writePersonnalData(obj)
    
    return 

def writePersonnalData(pObj):
    _of= open("people.json", mode="a")
    _of.write(str(pObj)+"\n")
    _of.close()
    print("File saved!")
    
    return 
    

getData()

_if= open("people.json", mode="r")
print(_if.read())
_if.close()

# _if.read()
# _if.readLine()