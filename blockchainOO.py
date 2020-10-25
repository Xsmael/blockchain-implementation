import hashlib
from time import time
import json


class Block:
    content= {}
    isFull= False
    def __init__(self, index,previousHash, blockSize=3):
        self.size=blockSize
        Block.content= {
            'index':index,
            'hash': '',
            'transactions':[],
            'nonce':0,
            'previousHash': previousHash,
            'timestamp': time()
        }
    
    def addTransaction(self):
        """
        adds a transaction to the block
        """
        transaction= {
            'sender': input('Expéditeur: '),
            'receiver': input('Destinataire: '),
            'amount': int(input('Montant: '))
        }
        Block.content.transactions.append(transaction)

    def addTransaction(self,sender, receiver, amount):
        """
        Overloaded Transaction method
        """
        transaction= {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        Block.content['transactions'].append(transaction)
    
    def removeTransaction(self, idx):
        """
        Removes the transaction at idx returns the removed transaction
        """
        t= Block.content['transactions']
        del Block.content['transactions']
        return t
    
    def editTransaction(self, idx, sender, receiver, amount):
        """
        edits a transaction
        """
        Block.content['transactions'][idx]['sender']= sender
        Block.content['transactions'][idx]['receiver']= receiver
        Block.content['transactions'][idx]['amount']= amount

    def isFull(self):
        return len( Block.content['transactions']) ==  self.size 


BLOCK_SIZE=3
BLOCKCHAIN=[]
MENU_STRING="1- Continuer\n2- Afficher la blockhain\n0- Quittter"
pendingBlock={}
makeDecision=1
currentIndex=0

def init():
    global currentIndex
    global pendingBlock
    block_0= {
        'index':currentIndex,
        'hash': '',
        'transactions':[],
        'nonce':0,
        'previousHash': 'NULL',
        'timestamp': time()
    }
    block_0['hash']=  hashlib.sha256(str(block_0).encode()).hexdigest()
    blockchain= [block_0]
    pendingBlock= block_0
    currentIndex+=1
    print("Genesis block initialised!")
    newPendingBlock()

init()


def newTransaction():
    """
    Adds a new transaction to the pending block
    """
    global pendingBlock
    global makeDecision
    transaction= {
        'sender': input('Expéditeur: '),
        'receiver': input('Destinataire: '),
        'amount': int(input('Montant: '))
    }
    pendingBlock['transactions'].append(transaction)
    print("Transaction ajouté!")
    if( len(pendingBlock['transactions']) == BLOCK_SIZE  ): 
        print("Block complet\n")
        mining()
        makeDecision=  int(input(MENU_STRING))
    
    return 

def newPendingBlock():
    """
    New block
    """
    global currentIndex
    global pendingBlock
    block= {
        'index':currentIndex,
        'hash': '',
        'transactions':[],
        'nonce':0,
        'previousHash': '',
        'timestamp': time()
    }
    block['previousHash']=  pendingBlock['hash']
    pendingBlock= block
    currentIndex+=1
    print("\n\nNouveau block initialisé!")
    return


def mining():
    """
    Mining Funciton 
    """
    print("Minage.... :P")
    global BLOCKCHAIN
    validHash= computeHash(pendingBlock)
    pendingBlock['hash']= validHash
    BLOCKCHAIN.append(pendingBlock)
    print("Minage Terminé\nBlock ajouté à la chaine:")
    printty(pendingBlock)
    newPendingBlock()

    return


def computeHash(block):
    """
    Hash Function
    """
    b= str(block)
    while 1:
        data= str(block)+ str(block['nonce'])
        block['nonce']+=1
        h= hashlib.sha256(data.encode()).hexdigest()
        if(h[0]=='0' and h[1]=='0'  and h[2]=='0'):
            print("Hash valide trouvé! avec un nonce de "+ str(block['nonce']))
            break
    
    return h

def displayBlockchain():
    """
    Displayin func
    """
    printty(BLOCKCHAIN)
    return

def editBlock():
    idx= int(input("Entrez l'index du bloc à modifer: "))
    block= BLOCKCHAIN[idx]
    printty(block)
    idx= int(input("Entrez l'index de la transaction à modifer: "))
    printty(block['transactions'][idx])
    block['transactions'][idx]= {
        'sender': input('Expéditeur: '),
        'receiver': input('Destinataire: '),
        'amount': int(input('Montant: '))
    }


def printty(obj):
   print (json.dumps(obj, indent=4))


while 1:
    if(makeDecision==1):
        newTransaction()
    elif (makeDecision==2):
        displayBlockchain()
        makeDecision=  int(input(MENU_STRING))
    else:
        print("Why so soon ??\nbye!")
        break