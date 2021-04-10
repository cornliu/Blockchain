import sys

import db
import blockchain
import block
 



def command():
    print(sys.argv)
    try:
        database = db.DB('db.pickle')
        Blockchain = db.load()
    except:
        database = db.DB('db.pickle')
        Blockchain = blockchain.Blockchain()

    if len(sys.argv) == 2 and sys.argv[1] == 'printchain':
        for i in range(len(Blockchain.blocks)):
            print('%s\n'%Blockchain.blocks[i])
    elif (len(sys.argv) == 4) and (sys.argv[1] == 'addblock') and (sys.argv[2] == '-transaction'):
        transaction = sys.argv[3][1:-1]  
        counter = len(Blockchain.blocks)
        Blockchain.Mine_Block('Block %i'%counter)
        Blockchain.Print_BlockChain()


        database.save(Blockchain)
    else:
        help()
def help():
    print('Client usable command:\n\
            python client.py addblock –transaction {“blablabla”}\n\
            python client.py printchain\n\
            python client.py printblock –height { height }')
    
if __name__ == '__main__':
    command()
    # try:
    #     db = db.DB('db.pickle')
    #     blockchain = db.load()
    #     for i in range(len(blockchain.blocks)):
    #         print(blockchain.blocks[i])
    # except:
    #     blockchain = Blockchain()
    # counter = len(blockchain.blocks)
    # while True:
    #     flag = input('Mining??(Y/N/Reset) :')
    #     if flag.lower() == 'y':
    #         blockchain.Mine_Block('Block %i'%counter)
    #         counter+=1
    #     elif flag.lower() == 'r':
    #         db.reset()
    #         break
    #     else:    
    #         db.save(blockchain)
    #         break
    # new_parser()

    