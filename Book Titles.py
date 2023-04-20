file1 = open('/usercode/files/books.txt', 'r') 
count = 0
n = 0
sc = 0
  
while True: 

    line = file1.readline() 
    count = len(line.strip())

    if not line: 
        break
    
    print("{}{}".format(line[0], count))
  
file1.close() 
