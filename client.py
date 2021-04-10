import sys

import db
import blockchain
import block
 
def command():
    database = db.DB('db.pickle')
    Blockchain = database.load()
    if len(sys.argv) == 2 and sys.argv[1] == 'printchain':
        for i in range(len(Blockchain.blocks)):
            print('%s\n'%Blockchain.blocks[i])
    elif (len(sys.argv) == 4) and (str(sys.argv[1]) == 'addblock') and (str(sys.argv[2]) == '-transaction'):
        Blockchain.Mine_Block(sys.argv[3])
        database.save(Blockchain)
    elif (len(sys.argv) == 4) and (str(sys.argv[1]) == 'printblock') and (str(sys.argv[2]) == '-height'):
        print(Blockchain.blocks[int(sys.argv[3])])
    else:
        help()
def help():
    print('Client usable command:\n\
            python client.py addblock –transaction {“blablabla”}\n\
            python client.py printchain\n\
            python client.py printblock –height { height }')
    
if __name__ == '__main__':
    command()

    