Merge Sort for descending order
def merge(left,right):
result=[]
i,j=0,0
while i<len(left) and j<len(right):
if(left[i]>right[j]):
result.append(left[i])
i+=1
else:
result.append(right[j])
j+=1
result+=left[i:]
result+=right[j:]
return result
def mergesort(list):
if(len(list)<=1):
return list
mid=int(len(list)/2)
left=mergesort(list[:mid])
right=mergesort(list[mid:])
return merge(left,right)
a=[-1,56,34,50,-2,30,-67]
print(mergesort(a))