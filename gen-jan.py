import sys
import time

def comb(L): 
                    for e in range(2):
                        for f in range(7):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        for j in range(10):
                                            print(str(0) + str(7) + str(0) + str(1) + str(0) + str(1) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
                                    

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

comb([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

sys.stdout = orig_stdout
f.close() 
         
