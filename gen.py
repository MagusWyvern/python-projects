import sys
import time

def comb(L): 
      
    for a in range(2): 
        for b in range(10): 
            for c in range(4): 
                for d in range(10):
                    for e in range(2):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        for j in range(10):
                                            print(str(0) + str(6) + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
comb([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])                                       

# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f

# comb([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# sys.stdout = orig_stdout
# f.close() 
         
