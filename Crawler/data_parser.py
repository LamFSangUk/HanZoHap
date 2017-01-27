f=open("result.txt","r")

data=f.read()
lines=data.split('\n')

for l in lines:
    print(l)
    l=l.replace(')','|')

    l=l.split('|')
    l[0]=l[0].replace('(','')
    l[1]=l[1].replace('}','')

    print(l[0],l[1])
f.close()