import time
import threading
from random import random, randint

# global constants
size = 20       # matrix size in each dimension
factor = 2      # number of threads is size/factor

# class for threads to do matrix multiplication
class MultThread(threading.Thread):
    num_threads = size/factor
        
    # id is simply an integer identifier
    # should be assigned sequentially starting at 0
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.daemon = False
        self.id = id
        
    def run(self):
        multiply(self.id)
    

# let's do some matrix multiplication using threads.
# we need to know which thread so that we know which rows
# it will calculate.
def multiply(id):
    global size, factor
     # iterate through columns of Y
    for j in range(len(m2[0])):
        # iterate through rows of Y
        for k in range(len(m2)):
            m3[id][j] += m1[id][k] * m2[k][j]
            fact = id + int(size/factor)
            m3[fact][j] += m1[fact][k] * m2[k][j]
def main():
    print('\nmain is starting\n')
    
    # create the threads and run them
    global size, factor
    num_threads = int(size/factor)
    threads = [MultThread(i) for i in range(num_threads)]

    for t in threads:
        t.run()

    # output the result
    print(m3)
    
    print('\nmain is finishing\n')
    
    
if __name__ == '__main__':
    # create global matrices
    # m1 and m2 contain random data and are the operands
    # m3 contains all 0 and is the result
    m1 = [[1 for _ in range(size)] for _ in range(size)]
    m2 = [[1 for _ in range(size)] for _ in range(size)]
    m3 = [[0 for _ in range(size)] for _ in range(size)]
                
    main()
    