import sys
import time

# Generate every possible IC number for people born on the year of 2006

def generateCombine(L): 
      
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
                                            # Change the first two arguments here to change the birth year
                                            print(str(0) + str(6) + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))

generateCombine([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])                                       

# Output the entire list into a .txt file
# WARNING: File size may be ridiculously large

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

comb([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

sys.stdout = orig_stdout
f.close() 
         
