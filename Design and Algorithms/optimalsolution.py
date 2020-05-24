a=[22,34,57,8,30,-45,7,30,-7,40]
b=a[::-1]
c=[]
for i in range(0,int(len(a)/2)):
c.append([a[i],b[i],a[i]+b[i]])
print(c[i])
m=min([c[j][2] for j in range(0,len(c))])
for i in range(0,len(c)):
try:
if(c[i].index(m)):
print("Optimal solution is:")
print(c[i])
except:
continue