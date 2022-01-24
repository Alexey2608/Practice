math = {'8':['',0],'9':['',0],'10':['',0],'11':['',0]}
alg = ['',0]
geo = ['',0]
f = open('mat_dv.txt')
for i in f:
    l=i.split()
    if int(l[3])+int(l[4]) > math[l[2]][1]:
        math[l[2]][1]= int(l[3])+int(l[4])
        math[l[2]][0] = l[0]+' ' + l[1]
    elif  int(l[3])+int(l[4]) == math[l[2]][1]:
        math[l[2]][0] +=' и '+ l[0]+' ' + l[1]
    if int(l[3]) > alg[1]:
        alg[1] = int(l[3])
        alg[0] = l[0]+' ' + l[1]
    elif  int(l[3]) == alg[1]:
        algebra[0] +=' и '+ l[0]+' ' + l[1]
    if int(l[4]) > geo[1]:
        geo[1] = int(l[4])
        geo[0] = l[0]+' ' + l[1]
    elif  int(l[3]) == geo[1]:
        geo[0] +=' и '+ l[0]+' ' + l[1]
print(math)
print(alg)
print(geo)


