import random

num_len = int(input('range : '))
file_name = 'sample.bin'

with open(file_name, 'wb') as fw:
    for a in range(1, num_len+1):
        for b in range(a+1, num_len+1):
            for c in range(b+1, num_len+1):
                for d in range(c+1, num_len+1):
                    for e in range(d+1, num_len+1):
                        print(str(a) + '|' + str(b) + '|' + str(c) + '|' + str(d) + '|' + str(e) + '|' + str(random.random()*100.), file=fw)
