import json
from hashlib import sha256


# this function solves the hash puzzle as miners do
def miner(_block,_prefix):
    for i in range(10000000):
        puzzle_input = str(_block) + str(i)
        digest = sha256(puzzle_input.encode()).hexdigest()
        if digest.startswith(_prefix):
            nonce = str(i)
            return nonce
        
def block_printer(_block,_current_block_hash,_block_number):
    
    # output_block = {'Block Number' : _block_number,
    #                 'Hash' : _current_block_hash,
    #                 'Previous Hash' : _block['previous_hash'],
    #                 'Nonce' : _block['Nonce']}
    
    print(' Block Number : {}\n Hash : {}\n Previous Hash : {}\n Nonce : {}\n'
    .format(_block_number,_current_block_hash,_block['previous_hash'],_block['Nonce']))
    print('-'*20)

    


# GenesisBlock
genesis_fd = open('GenesisBlock/GenesisBlock/GenesisBlock.json')
genesis_dict = json.load(genesis_fd)

# Ledgers
ledgers = [] 
for i in range(0,15):
    tempJson = open('Ledgers/Ledgers/Ledger_Number{}.json'.format(i+2))
    ledgers_fd = json.load(tempJson)
    ledgers.append(ledgers_fd)

# Math_Problems
problems = [] 
for i in range(0,15):
    tempJson = open('Math_Problems/Math_Problems/Math_Problem_Number{}.json'.format(i+2))
    problems_fd = json.load(tempJson)
    problems.append(problems_fd)
    

# initalization of blockchain by adding Genesis Block to it
genesis_block = {'blockNumber' : 1 ,'main' : genesis_dict,'Nonce' : None, 'previous_hash' : None}
blockchain = []
blockchain.append(genesis_block)
# this var is used to store last hash
last_block_hash = sha256(str(genesis_block).encode()).hexdigest()
block_printer(genesis_block,last_block_hash,1)

# loop that builds blocks and try to find nonce for them to add them to blockchain successfully
# except for last block because of its hard problem -> range(0,15)
for index in range(0,15):
    
    temp_block = {'main' : ledgers[index],
                  'Nonce' : None,
                  'previous_hash' : last_block_hash}
    
    temp_prefix = problems[index]['mathProblem']
    
    # this is where the nonce is computed
    temp_nonce = miner(temp_block,temp_prefix)
     
    temp_block.update({'Nonce' : temp_nonce})
    blockchain.append(temp_block)
    current_block_hash = sha256(str(temp_block).encode()).hexdigest()
    last_block_hash = current_block_hash

    block_printer(temp_block,current_block_hash,index+2)






 


