ms1=0
ms2=0
kostyl=0
f=open('mat_dv.txt','r')
for i in f:
    l=i.split()
    kostyl+=1
    if (int(l[3])>ms1):
        ms1=int(l[3])
        ms1n=kostyl
    if (int(l[4])>ms2):
        ms2=int(l[4])
        ms2n=kostyl
f.seek(ms1n)
msfi=f.readline()
print('Algebra:',msfi)
f.seek(ms2n)
msfi=f.readline()
print('Geometry:',msfi)
f.close()