import hashlib

"""
s="HAHAHA"
digest= hashlib.sha256(s.encode()).hexdigest();
print(digest);
<>
"""


lastNode=""
block0={"name":"", "age":"", "previousHash":hashlib.sha256("000".encode()).hexdigest(), "blockHash":""}
block0['blockHash']=  hashlib.sha256(str(block0).encode()).hexdigest()
blockchain= [block0]

def createBlock():
    age= int(input("age: "))
    name= input("name: ")
    block={'age':age, 'name':name}
    print("\nBlock successfully created!")
    print(block)
    return block
    

def addBlock(block):
    if(block['age'] > 50 or len(block['name']) > 5): 
        print("Invalid Block\nRejected!")
        return

    block["previousHash"]= blockchain[-1]["blockHash"]
    block["blockHash"]= hashlib.sha256( str(block).encode() ).hexdigest()
    blockchain.append(block)
    print("\nNew block added!")
    print("hash:")
    print(block["blockHash"])
    print("\n B L O C K C H A I N:")
    print(blockchain)
"""
def verify():
    print("\n Verification:\n ")
    age= int(input("age: "))
    name= input("name: ")
    block={'age':age, 'name':name}
    blockHash= hashlib.sha256( str(block).encode() ).hexdigest()
    if(blockchain[blockHash] == block):
        print("OK")
    else:
        print("ERROR")
"""
while 1:
    addBlock(createBlock())
    if(input("Continue ? ") != "y"):
        break

verify()