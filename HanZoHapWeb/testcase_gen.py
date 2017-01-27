import random

num_len = int(input('range : '))
file_name = 'sample.bin'

with open(file_name, 'w') as fw:
    for a in range(1, num_len+1):
        for b in range(a+1, num_len+1):
            for c in range(b+1, num_len+1):
                for d in range(c+1, num_len+1):
                    for e in range(d+1, num_len+1):
                        line = str(a)+ '|' + str(b) + '|'+ str(c) + '|' + str(d) + '|' + str(e) + '|' + str((random.uniform(0.25, 0.6)*100+ random.uniform(0.45,0.55)*45 )* 2 / 3) + '\n'
                        fw.write(line)
                        
